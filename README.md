# The Stationery Hub — Scratch & Win Card System 🎫

A web-based scratch card reward system for **The Stationery Hub** stationery business. Built with Python (Flask) + SQLite.

## Features

- 🎫 **Admin Panel** — Create scratch cards by entering customer name, phone number, and purchase amount
- 🎁 **Scratch & Win** — Customers receive a unique link to scratch and reveal their free gift
- 📊 **Dashboard** — View all scratch cards, their status, and prizes
- 📱 **WhatsApp Integration** — One-click share scratch card links via WhatsApp
- 🔒 **Secure** — Prize is hidden until the customer scratches; one-time reveal only

## Reward Tiers

| Tier | Min. Purchase | Possible Gifts |
|------|--------------|----------------|
| 🥉 Bronze | ₹399 | Hauser Roller Pen, Stationery Kit, Apsara Zesta Pen, Fancy Eraser, Small Notebook |
| 🥈 Silver | ₹699 | Handmade Keyring, Camera Keychain, Whitener, Tape Whitener, Stationery Kit |
| 🥇 Gold | ₹1000 | 20% Discount on Next Order, Stationery Kit, A5 Spiral Binding Notebook, Premium Pen |

## Setup & Run

### 1. Install Flask
```bash
pip install flask
```

### 2. Start the Server
```bash
cd TSH
python app.py
```

### 3. Open Admin Panel
Go to **http://localhost:3000/admin.html** in your browser

## How to Use

1. **Add a Customer**: In the admin panel, enter the customer's name, phone, and purchase amount
2. **Get the Link**: Copy the generated scratch card link
3. **Share with Customer**: Click "Send via WhatsApp" or copy the link manually
4. **Customer Scratches**: Customer opens the link and scratches to reveal their gift
5. **Track Results**: View all results in the admin panel dashboard

## Push to GitHub

```bash
cd TSH
git init
git add .
git commit -m "Scratch Card System for The Stationery Hub"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/TSH.git
git push -u origin main
```

## Deploy Free on Render.com

1. Push this project to GitHub
2. Go to [render.com](https://render.com) → **New Web Service**
3. Connect your GitHub repo
4. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
5. Deploy! You'll get a free URL like `https://tsh-scratch.onrender.com`

## Project Structure

```
TSH/
├── app.py              # Flask server & API routes
├── requirements.txt    # Python dependencies (just Flask)
├── .gitignore          # Git ignore rules
├── README.md           # This file
├── logo.jpg            # Business logo
└── public/
    ├── admin.html      # Admin panel
    ├── scratch.html    # Customer scratch card page
    └── logo.jpg        # Logo (served to frontend)
```

## Tech Stack

- **Backend**: Python 3, Flask
- **Database**: SQLite (built-in with Python)
- **Frontend**: Vanilla HTML/CSS/JS
