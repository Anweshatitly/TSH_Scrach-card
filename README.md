# The Stationery Hub — Scratch Card (bug-fixed)

## Fix in this version
Scratch card links occasionally showed "This card link isn't valid" even
when generated correctly — a base64 padding bug in the decoding step that
depended on the length of the customer's name/phone/gift text. Fixed in
`index.html`.

## Files
- `index.html` — Customer card, deploy at the site root.
- `counter.html` — Staff page. **No database on Netlify** — see prior README for details.
- `logo.png` — Shop logo (already embedded in both HTML files).

## Deploying
1. Push to GitHub, connect the repo in Netlify (no build command, publish directory `/`).
2. After deploy, open `counter.html`, update:
   ```js
   const CARD_URL = "https://your-site-name.netlify.app";
   ```
   (no trailing slash), then commit and push again.

## Gift slabs
- ₹399 and above: Hauser roller pen / Stationery kit / Apsara Zesta pencils / Fancy eraser / Small notebook
- ₹699 and above: Handmade keyring / Camera keychain / Whitener pen / Whitener tape / Stationery kit
- ₹1000 and above: 20% off next order / Stationery kit / A5 spiral notebook / Pen
