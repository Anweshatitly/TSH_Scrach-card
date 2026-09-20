The Stationery Hub — Scratch Card Files
========================================

Files in this zip:
- counter.html  -> Staff page: enter customer + bill, get a card link to send
- card.html     -> Customer page: what you send them, they scratch to reveal
- logo.png      -> Your original logo (already baked into both HTML files too)

IMPORTANT — about the database:
Both HTML files already have the logo embedded, so they work as single
files with no other assets needed.

However: counter.html's "Records" tab and its ability to save each card
only work when it's opened as the claude.ai artifact link (not this raw
file). If you host counter.html yourself (GitHub Pages, etc.), the record
-keeping will not function — the database is tied to the published
claude.ai page, not the file itself.

card.html has no database dependency — it works fine hosted anywhere
(GitHub Pages, Netlify, your own server), since each customer's details
are carried inside the link you send them, not stored on the page.

If you host card.html yourself, note the CARD_URL variable near the top
of counter.html's <script> — update it to point to wherever you end up
hosting card.html, so the links the counter page generates go to the
right address.
