# The Stationery Hub — Scratch Card

## Files
- `index.html` — Customer card. Opened via a link with data after `#`. Shows the customer's name, phone and bill (read-only) and a scratch panel that reveals a gift.
- `counter.html` — Staff page. Enter a bill, get a gift + a shareable card link. **No database on Netlify** — see note below.
- `logo.png` — Shop logo (already embedded inside both HTML files, so this file itself isn't required for the site to work).

## Deploying
1. Push this repo to GitHub.
2. In Netlify: **Add new site → Import an existing project → connect this repo**.
3. Build settings: none needed — leave build command blank, publish directory `/` (root).
4. Deploy. Netlify gives you a URL like `https://your-site-name.netlify.app`.
5. Your customer card will be at the root: `https://your-site-name.netlify.app/`
6. Your counter page will be at: `https://your-site-name.netlify.app/counter.html`

## After deploying — one edit required
Open `counter.html`, find this line near the top of the `<script>` section:

```js
const CARD_URL = "https://anweshatitly.github.io/TSH_Scrach-card";
```

Change it to your new Netlify URL (no trailing slash), e.g.:

```js
const CARD_URL = "https://your-site-name.netlify.app";
```

Commit and push that change so future card links point to the right place.

## About the database (important)
`counter.html` was originally built to save every card to a database, but that
database only exists when the page is opened through its claude.ai artifact link —
it does NOT work when the file is hosted on Netlify, GitHub Pages, or anywhere else.

Hosted on Netlify, `counter.html` will still:
- pick the correct gift slab for a bill amount
- generate a working scratch-card link for the customer
- let you copy the link or send it on WhatsApp

It will NOT:
- keep a Records tab of past cards
- track "given" status
- export a CSV
- remember anything after you close the tab

If you want the record-keeping back, use the claude.ai-hosted version of counter.html
instead of the Netlify one for that page specifically. You can run both at once:
customers always use the Netlify-hosted `index.html`, while staff use whichever
version of `counter.html` suits the moment.

## Gift slabs
Edit the `SLABS` array near the top of each file's `<script>` if these ever change.
Keep both files' slab lists identical.

- ₹399 and above: Hauser roller pen / Stationery kit / Apsara Zesta pencils / Fancy eraser / Small notebook
- ₹699 and above: Handmade keyring / Camera keychain / Whitener pen / Whitener tape / Stationery kit
- ₹1000 and above: 20% off next order / Stationery kit / A5 spiral notebook / Pen
