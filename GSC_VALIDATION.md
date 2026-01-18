## GroundOps — GSC validation checklist (post-P0 / post-canonicalization)

This is the “now we watch the machine” step from the audit. The goal is to confirm Google is:
- Crawling the right URLs
- Indexing the right URLs
- Consolidating duplicates (no `.html`, no trailing slash, no old slugs)
- Ranking the *intended* pages for each intent

### Before you start (one-time)
- **Submit sitemap**: in Google Search Console → **Sitemaps** → submit `https://www.groundops.com/sitemap.xml`
- **Confirm robots**: `robots.txt` references the same sitemap URL.
- **Run local sitemap sanity check** (prevents “submitted URL not found (404)” noise):

```bash
python validate_sitemap.py
```

If it returns non‑zero, fix missing files / wrong slugs before expecting clean GSC data.

---

## What to monitor (0–14 days)

### 1) Sitemaps (Day 0–2)
In **Sitemaps**:
- **Sitemap status**: should be “Success”
- **Discovered URLs**: should roughly match the count of URLs in `sitemap.xml`

If you see errors:
- **Submitted URL not found (404)**: sitemap contains a URL that doesn’t map to a real page (fix the file/slug, then re-submit).
- **Redirect error**: a redirect chain is too long or loops (fix `vercel.json` redirects).

### 2) Pages / Indexing (Day 2–14)
In **Pages** (Indexing):
- **Not indexed → Duplicate, Google chose different canonical**
  - Spot-check the affected URL using **URL Inspection**
  - Confirm the page’s `<link rel="canonical">` is correct and consistent with your redirects
- **Not indexed → Soft 404**
  - Usually thin content or “no real page”; ensure the page has substantive copy + internal links
- **Not indexed → Blocked by robots.txt**
  - Expected only for intentionally blocked pages (e.g. `supplier-portal.html`, internal/legacy files)

Target outcome:
- Money pages and hubs (`/`, `/platform`, `/vendor-management`, `/case-studies`, `/blog`, core services) move to **Indexed**
- Legacy/internal pages stay **Not indexed**

### 3) Crawl stats (ongoing)
In **Settings → Crawl stats**:
- Watch for spikes in **404**, **redirect**, **server error**
- If 404s spike, export examples and fix:
  - Sitemap mismatches
  - Internal links
  - Redirects in `vercel.json`

### 4) Performance (Day 7–14)
In **Performance → Search results** (filter to last 7/14 days):
- **Top pages**: confirm the correct page is earning clicks for each intent
- **Top queries**: check for cannibalization (multiple pages swapping for same query)

If cannibalization shows up:
- Strengthen the “unique intent” in the first scroll of each competing page
- Add explicit internal links from supporting pages → the primary page for that intent

---

## Quick URL Inspection spot-check (recommended)
Run URL Inspection for:
- `https://www.groundops.com/`
- `https://www.groundops.com/platform`
- `https://www.groundops.com/vendor-management`
- `https://www.groundops.com/case-studies`
- `https://www.groundops.com/blog`

Confirm:
- **Canonical** is the clean URL (no `.html`, no trailing slash)
- **Last crawl** is recent (after deployment)
- **Page is indexable** (no accidental `noindex`)

---

## Change freeze rule (important)
Per the audit: once GSC is processing these changes, avoid large structural/schema changes for **~1–2 weeks**. Let Google settle on canonicals and indexing first.

