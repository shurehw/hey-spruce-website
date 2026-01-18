## GroundOps intent map (cannibalization control)

Goal: **one primary page per primary query cluster**. Supporting pages should link *to* the primary page and avoid competing Titles/H1s.

### Primary pages (money pages + hubs)

- **`/` (homepage)**: GroundOps brand + **platform-backed facilities execution** for multi-location restaurant operators
  - **Primary intent**: facilities execution / facilities ops system-of-record for multi-location restaurants
  - **Must not primarily target**: “restaurant cleaning los angeles” (that belongs on `/restaurant-cleaning-los-angeles`)
  - **Support with links to**: `/platform`, `/case-studies`, `/vendor-management`, `/restaurant-cleaning-los-angeles`

- **`/platform`**: GroundOps platform (software modules + artifacts)
  - **Primary intent**: work orders + dispatch + QA + reporting platform for restaurant facilities
  - **Support with links to**: `/vendor-management`, `/case-studies`, and the 2–4 most important services (`/restaurant-cleaning-los-angeles`, `/preventive-maintenance`, `/commercial-kitchen-cleaning`)

- **`/vendor-management`**: vendor coordination + SLA governance + scorecards
  - **Primary intent**: vendor management for multi-location restaurants (cleaning/PM/repairs)
  - **Support with links to**: `/platform#scorecard-sample`, `/case-studies`, and relevant services

- **`/restaurant-cleaning-los-angeles`**: umbrella “restaurant cleaning in LA” service page
  - **Primary intent**: restaurant cleaning services in Los Angeles (overview page)
  - **Support with links to**: sub-services (`/nightly-cleaning`, `/commercial-kitchen-cleaning`, `/deep-kitchen-cleaning`, `/restroom-cleaning`, `/floor-scrubbing`, `/boh-cleaning`, `/foh-cleaning`)
  - **Differentiator links to**: `/platform`, `/vendor-management`, `/case-studies`

- **`/commercial-kitchen-cleaning`**: BOH deep degreasing / kitchen cleaning
  - **Primary intent**: commercial kitchen cleaning Los Angeles
  - **Avoid competing with**: `/deep-kitchen-cleaning` (one-time/quarterly “reset”)

- **`/deep-kitchen-cleaning`**: “reset” / equipment pull-outs / quarterly programs
  - **Primary intent**: deep kitchen cleaning Los Angeles

- **`/nightly-cleaning`**: nightly restaurant cleaning
  - **Primary intent**: nightly restaurant cleaning Los Angeles

- **`/multi-location-cleaning`**: chains / portfolio cleaning ops
  - **Primary intent**: multi-location restaurant cleaning (chains)

- **`/preventive-maintenance`**: restaurant PM programs
  - **Primary intent**: restaurant preventive maintenance Los Angeles

- **`/hood-exhaust-cleaning`**: hood/exhaust coordination + documentation
  - **Primary intent**: hood/exhaust cleaning coordination (NFPA 96 documentation)

- **`/case-studies`**: proof hub
  - **Primary intent**: case studies / proof of standardized execution

- **`/blog`**: ops guides hub
  - **Primary intent**: ops guides / operational how-tos

### Local modifiers (supporting pages)

- **`/restaurant-cleaning-downtown-los-angeles`** (DTLA local): support page for “DTLA restaurant cleaning”
  - **Must link up to**: `/restaurant-cleaning-los-angeles` as the umbrella LA page

### Implementation rules (how we prevent cannibalization)

- **Title/H1 uniqueness**: homepage titles should not lead with “Restaurant Cleaning Los Angeles”.
- **First-scroll focus**: hero headline + lead paragraph should match the page’s primary intent.
- **Internal linking**: supporting pages link to the primary page with descriptive anchors (not “click here”).
- **Don’t duplicate “near me” blocks sitewide**: keep those on the *service* landing page, not the homepage.
