import os
import uuid
import sqlite3
import random
import json
from flask import Flask, request, jsonify, send_from_directory

# ===== APP SETUP =====
app = Flask(__name__, static_folder='public', static_url_path='')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'scratch_cards.db')

# ===== DATABASE =====
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS customers (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            amount REAL NOT NULL,
            tier TEXT NOT NULL,
            prize_emoji TEXT NOT NULL,
            prize_text TEXT NOT NULL,
            revealed INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# ===== PRIZE DATA =====
TIER_PRIZES = {
    'bronze': [
        {'emoji': '🖊️', 'text': 'Hauser Roller Pen'},
        {'emoji': '🎒', 'text': 'Stationery Kit'},
        {'emoji': '✏️', 'text': 'Apsara Zesta Pen'},
        {'emoji': '🧽', 'text': 'Fancy Eraser'},
        {'emoji': '📓', 'text': 'Small Notebook'},
    ],
    'silver': [
        {'emoji': '🔑', 'text': 'Handmade Keyring'},
        {'emoji': '📸', 'text': 'Camera Keychain'},
        {'emoji': '✨', 'text': 'Whitener'},
        {'emoji': '📋', 'text': 'Tape Whitener'},
        {'emoji': '🎒', 'text': 'Stationery Kit'},
    ],
    'gold': [
        {'emoji': '💰', 'text': '20% Discount on Next Order'},
        {'emoji': '🎒', 'text': 'Stationery Kit'},
        {'emoji': '📒', 'text': 'A5 Spiral Binding Notebook'},
        {'emoji': '🖋️', 'text': 'Premium Pen'},
    ]
}

def get_tier(amount):
    if amount >= 1000:
        return 'gold'
    elif amount >= 699:
        return 'silver'
    elif amount >= 399:
        return 'bronze'
    return None

def pick_random_prize(tier):
    return random.choice(TIER_PRIZES[tier])

# ===== ROUTES — STATIC PAGES =====

@app.route('/')
def index():
    return send_from_directory('public', 'admin.html')

@app.route('/admin.html')
def admin_page():
    return send_from_directory('public', 'admin.html')

@app.route('/scratch.html')
def scratch_page():
    return send_from_directory('public', 'scratch.html')

# ===== API ROUTES =====

@app.route('/api/customers', methods=['POST'])
def create_customer():
    """Admin creates a new scratch card for a customer."""
    data = request.get_json()

    name = data.get('name', '').strip()
    phone = data.get('phone', '').strip()
    amount = data.get('amount')

    if not name or not phone or not amount:
        return jsonify({'error': 'Name, phone, and amount are required'}), 400

    try:
        amount = float(amount)
    except (ValueError, TypeError):
        return jsonify({'error': 'Invalid amount'}), 400

    if amount < 399:
        return jsonify({'error': 'Minimum purchase amount is ₹399'}), 400

    tier = get_tier(amount)
    prize = pick_random_prize(tier)
    customer_id = str(uuid.uuid4())

    conn = get_db()
    conn.execute(
        'INSERT INTO customers (id, name, phone, amount, tier, prize_emoji, prize_text) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (customer_id, name, phone, amount, tier, prize['emoji'], prize['text'])
    )
    conn.commit()
    conn.close()

    return jsonify({
        'success': True,
        'id': customer_id,
        'link': f'/scratch.html?id={customer_id}',
        'tier': tier,
        'customer': {
            'id': customer_id,
            'name': name,
            'phone': phone,
            'amount': amount,
            'tier': tier
        }
    })

@app.route('/api/customers/<customer_id>', methods=['GET'])
def get_customer(customer_id):
    """Get customer data for the scratch card page."""
    conn = get_db()
    customer = conn.execute('SELECT * FROM customers WHERE id = ?', (customer_id,)).fetchone()
    conn.close()

    if not customer:
        return jsonify({'error': 'Scratch card not found'}), 404

    # Only send prize info if already revealed
    result = {
        'id': customer['id'],
        'name': customer['name'],
        'phone': customer['phone'],
        'amount': customer['amount'],
        'tier': customer['tier'],
        'revealed': customer['revealed'] == 1,
        'prize_emoji': customer['prize_emoji'] if customer['revealed'] == 1 else None,
        'prize_text': customer['prize_text'] if customer['revealed'] == 1 else None,
        'created_at': customer['created_at']
    }

    return jsonify(result)

@app.route('/api/customers/<customer_id>/reveal', methods=['POST'])
def reveal_card(customer_id):
    """Customer scratches the card — mark as revealed."""
    conn = get_db()
    customer = conn.execute('SELECT * FROM customers WHERE id = ?', (customer_id,)).fetchone()

    if not customer:
        conn.close()
        return jsonify({'error': 'Scratch card not found'}), 404

    if customer['revealed'] == 1:
        conn.close()
        return jsonify({
            'already_revealed': True,
            'prize_emoji': customer['prize_emoji'],
            'prize_text': customer['prize_text']
        })

    conn.execute('UPDATE customers SET revealed = 1 WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()

    return jsonify({
        'success': True,
        'prize_emoji': customer['prize_emoji'],
        'prize_text': customer['prize_text']
    })

@app.route('/api/admin/customers', methods=['GET'])
def list_customers():
    """Admin: Get all customers."""
    conn = get_db()
    customers = conn.execute('SELECT * FROM customers ORDER BY created_at DESC').fetchall()
    conn.close()

    result = []
    for c in customers:
        result.append({
            'id': c['id'],
            'name': c['name'],
            'phone': c['phone'],
            'amount': c['amount'],
            'tier': c['tier'],
            'prize_emoji': c['prize_emoji'],
            'prize_text': c['prize_text'],
            'revealed': c['revealed'] == 1,
            'created_at': c['created_at']
        })

    return jsonify(result)

@app.route('/api/customers/<customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    """Admin: Delete a customer record."""
    conn = get_db()
    cursor = conn.execute('DELETE FROM customers WHERE id = ?', (customer_id,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return jsonify({'error': 'Customer not found'}), 404

    return jsonify({'success': True})

# ===== START =====
if __name__ == '__main__':
    init_db()
    port = int(os.environ.get('PORT', 3000))
    print(f'\n* The Stationery Hub - Scratch Card Server')
    print(f'  ----------------------------------------')
    print(f'  Server running at: http://localhost:{port}')
    print(f'  Admin Panel:       http://localhost:{port}/admin.html')
    print(f'  Database:          scratch_cards.db\n')
    app.run(host='0.0.0.0', port=port, debug=True)
