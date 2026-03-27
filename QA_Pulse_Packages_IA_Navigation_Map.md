# QA Pulse — Packages Module: Information Architecture & Navigation Map

> **Scope:** Packages (Alpha) section only — starting from the second nav item (Bookings), tracing all flows to depth ≥ 10.
> **Base URL:** `https://qa-marketplace-pulse.osmos.ai`
> **Date Traced:** 27 Mar 2026

---

## Left Navigation — Packages Structure

```
Packages (Alpha)  [icon: stacked layers]
├── 1. Packages                (SKIPPED — user instruction: do not use first package name)
├── 2. Bookings                → /packages/bookings
├── 3. Analytics               (section header)
│   ├── 3.1 Package Analytics  → /packages/flexiAnalytics/package
│   ├── 3.2 Sales Analytics    → /packages/flexiAnalytics/sales
│   └── 3.3 Live Analytics     → /packages/flexiAnalytics/liveAnalytics
├── 4. Packages                → /packages/flexiPackages
├── 5. Sales Planner           → /packages/salesPlanner
└── 6. All Bookings            (section header)
    ├── 6.1 Bookings           → /packages/flexiBookings/list
    └── 6.2 Line Item Review   → /packages/flexiBookings/review
```

---

## 2. Bookings Flow
**URL:** `/packages/bookings`
**Breadcrumb:** Packages → Bookings

### 2.1 Page-Level KPI Cards
| Metric | Description |
|---|---|
| Total Bookings | Count of all bookings (e.g., 306) |
| Active Bookings | Currently active (e.g., 16) |
| Delivered Bookings | Completed deliveries (e.g., 274) |

### 2.2 Bookings Table
**Toolbar:**
- Refresh (↻)
- Download (↓)
- Column Selector (grid icon)
- Search by Name
- Add Filter
- View Mode: Osmos View (toggle)

**Table Columns:**
`Status | Name | Brand | Booking Cost | Flight Start Date | Flight End Date`

**Row Status Values:** Scheduled, Active, Delivered, Cancelled

---

### 2.3 Booking Row — Actions

#### 2.3.1 View Button → Booking Detail Drawer
**URL pattern:** `/packages/bookings/drawer/GOAL_LAUNCHER/PRE_AUCTION_BOOKINGS?defaultCardToOpen=CREATIVE_SELECTION&goalId={id}&isEditMode=true&isViewOnlyMode=true&clientId={clientId}&bookingId={bookingId}`

**Drawer Header:**
- Booking Name
- Status Badge (e.g., Scheduled)
- Flight Dates (e.g., 01 Apr 26 – 05 Apr 26)
- Biddable CPM (e.g., ₹600)
- Base Price (e.g., ₹50,000)

**Step Tabs (3-step wizard):**

##### Step 1: Inventory Selection
- Shows selected Pages (e.g., "1 Page selected: Home Page")
- Inventory Name
- Tags
- Ad Slot Type (e.g., Text Ad Box-1)

##### Step 2: Keywords
- Keywords Targeted count (e.g., "1 KEYWORDS TARGETED")
- Search bar for keywords
- Keyword list table
  - Column: Keyword (e.g., "Hello")

##### Step 3: Ads Upload
- Shows creative upload status
- State: "No Ads Created" (if empty)

**Bid Details Panel (shown below tabs):**
- Base Price
- Total Bidders
- Highest Bid
- Highest Bidder

**Footer:** Done button

---

#### 2.3.2 Kebab Menu (⋮) on Booking Row
- **Analytics** → Opens analytics drawer
- **Change History** → Opens change history drawer

##### 2.3.2.1 Analytics Drawer
**URL:** `/packages/bookings/drawer/GOAL_LAUNCHER/INVENTORY_AUCTION?defaultCardToOpen=PRE_AUCTION_PERFORMANCE&cardsToShow=["PRE_AUCTION_PERFORMANCE"]&clientId={id}&goalId={id}`

**Header:**
- Booking name + status indicator (coloured dot)
- Date range picker (e.g., 20 Mar 26 – 26 Mar 26)

**KPI Cards:**
`Ad Revenue | Ad Impressions | CTR | CPC | Ad Clicks`

**Performance Summary Chart:**
- Highcharts line chart
- Axes: Ad Revenue vs Ad Impressions
- X-axis: daily dates
- Filter Applicable: Date

**Keyword Performance Table:**
- Columns: Keyword | Ad Revenue | Ad Clicks | Ad Impressions | CPC | CPM | CTR
- State: "No Data Available" (if no data)
- Filter Applicable: Date

**Footer:** Done button

---

##### 2.3.2.2 Change History Drawer
**URL:** `/packages/bookings/drawer/CHANGE_HISTORY_V2?id={bookingId}&clientId={clientId}&scope=Booking&isClientLevel=true`

**Toolbar:**
- Filter chips: "Impact equals (=) High", "Entity has any of Booking"
- Refresh (↻)
- Download (↓)
- Column Selector
- Date Range (e.g., 25 Feb 26 – 27 Mar 26)

**Table Columns:**
`Date | Entity | Change Level | Change Type | Changed By`

**Sample Row:**
- Date: 26 Mar 26 12:05:38 AM +05:30
- Entity: Booking
- Change Level: Status
- Change Type: Booking Status Updated
- Changed By: System

**Workflow End:** ✅ All changes listed chronologically.

---

## 3. Analytics — Package Analytics
**URL:** `/packages/flexiAnalytics/package`
**Breadcrumb:** Packages → Analytics → Package Analytics

**Top Bar:**
- Date range picker with comparison mode
- Refresh, Search, Person icon

### 3.1 Package Level Report
**Toolbar:** Add Filter | Search Package Name | Download
**Table Columns:**
`Package Name | Ad Impressions | Ad Clicks | CTR | Add to Cart | Attributed Orders (SKU) | Attributed GMV`
**State:** No Data Available (filter applicable: Date)

### 3.2 Booking Snapshot
**Toolbar:** Add Filter
**Table Columns:**
`Booking Name | Package Name | Flight Start Date | Flight End Date | Line Items Count | Ad Impressions | Ad Clicks | CTR | Add to Cart | Attributed GMV | Attributed Orders (SKU)`
**State:** No Data (filter applicable: Date)

### 3.3 Line Items Performance Snapshot
**Toolbar:** Add Filter
**Table Columns:**
`Line Items | Line Items Type | Package Name | Flight Start Date | Flight End Date | Ad Impressions | Ad Clicks | CTR | Add to Cart | Attributed Orders (SKU) | Attributed GMV`
**State:** No Data (filter applicable: Date)

**Workflow End:** ✅ Read-only analytics; download available.

---

## 4. Analytics — Sales Analytics
**URL:** `/packages/flexiAnalytics/sales`
**Breadcrumb:** Packages → Analytics → Sales Analytics

**Top Bar:**
- Date range with comparison mode

### 4.1 KPI Cards
| Metric | Value (example) | vs Previous |
|---|---|---|
| Package Quantity Sold | 23 | +10 (+130%) |
| Revenue Booked | ₹13.6K | ₹50.1K (−72.8%) |

### 4.2 Performance Trends Chart
- Dual-axis Highcharts line chart
- Metrics: Package Quantity Sold, Revenue Booked
- X-axis: daily dates
- Filter Applicable: Date

### 4.3 Package Sales Report
**Toolbar:** Add Filter | (no separate search)
**Table Columns:**
`Booking Name | Package Name | Advertiser | Flight Start Date | Flight End Date | Booking Cost | Purchased Date | Purchased By`

**Sample Rows:** QaBooking_09TBC | QA_Test(Automation) | Whitakers | …

**Footer note:** Comparison mode not applicable

**Workflow End:** ✅ Downloadable sales report.

---

## 5. Analytics — Live Analytics
**URL:** `/packages/flexiAnalytics/liveAnalytics`
**Breadcrumb:** Packages → Analytics → Live Analytics

### 5.1 KPI Cards (Live / Today)
`Ad Impressions | Ad Clicks | CTR`

### 5.2 Performance Trend Chart
- Highcharts line chart
- Metric: Ad Impressions (today's hourly)
- X-axis: 00:00 → 21:00

### 5.3 Live Bookings Table
**Toolbar:** Add Filter
**Table Columns:**
`Booking Name | Package Name | Flight Start Date | Flight End Date | Line Items Count | Ad Impressions | Ad Clicks | CTR`
**State:** No Data Available

**Workflow End:** ✅ Real-time monitoring view.

---

## 6. Packages (Create / Manage)
**URL:** `/packages/flexiPackages`
**Breadcrumb:** Packages → Packages

### 6.1 Page-Level KPI Cards
| Metric | Value |
|---|---|
| Total Packages | 496 |
| Total Active Packages | 37 |
| Total Draft Packages | 282 |
| Total Paused Packages | 0 |

### 6.2 Packages Table
**Toolbar:**
- Refresh (↻)
- Download (↓)
- Column Selector
- Search by Package Name
- **+ Create New Package** (CTA button)
- Add Filter

**Table Columns:**
`[Banner Thumbnail] | Status | Package Name | Description | Visibility Start Date | Visibility End Date | Flight Window Start Date | Flight Window End Date | No. of Packages Sold | Total Used Count | Total Booked Revenue | View | ⋮`

**Status Values:** Active, Draft, Paused

---

### 6.3 Package Row — Actions

#### 6.3.1 Package Name Link / View → Package Detail Drawer
**URL:** `/packages/flexiPackages/drawer/FLEXI_PACKAGE_LAUNCHER?id={packageId}`

**Info Banner:** "This package has a booking on hold. Only the Flight Window and Visibility Window can be edited."

##### Section A: Package Details (Expandable)
- Name
- Description
- Banner image (displayed)
- Package Visibility: By Advertiser / By Persona Selection
  - If By Advertiser → Advertiser/Client (multi-select dropdown)
  - If By Persona Selection → Persona Selection (e.g., Beta, Platinum, Silver) → Shows "Includes N advertisers"

##### Section B: Package Configuration (Expandable)
- Visibility Date* — duration for which package is visible for advertisers to book
- Flight Window* — total time span for booking slots
- Package Duration — length of each booking slot (e.g., 10 Days)
- Max Quantity Per Package Duration
- Max Quantity an Advertiser can book per Package Duration
- Package Cost (e.g., ₹1,000)
- Additional Cost (Optional)
- Package quantity for sale (e.g., 60 packages across 6 durations)

##### Section C: Line Items (Expandable)
**Table Columns:** Line Item Name | Line Item Type
**Sample:** "Line Item (23rd Mar | 16:32:45)" | Sponsored Display Ads
- Each line item has a kebab menu (⋮)

##### Section D: Package Commitment (Optional, Expandable)
- Commitment Type dropdown (e.g., "Overall Impression Delivered")
- Line Item selector
- Commitment value (e.g., 1,32,12,32,123)

##### Section E: Package Rules (Optional, Expandable)
- Conditional rules for automatic package management based on performance metrics
- State: "No rules configured yet"

**Footer Actions:** Save | (Preview Package — disabled until filled)

---

#### 6.3.2 Kebab Menu (⋮) on Package Row
- **Edit** → Opens same drawer in edit mode
- **Archive** → Archives the package

---

### 6.4 Create New Package Flow
**URL:** `/packages/flexiPackages/drawer/FLEXI_PACKAGE_LAUNCHER`

Follows the same 5-section accordion as the Package Detail Drawer:

| Step | Section | Required Fields |
|---|---|---|
| 1 | Package Details | Name*, Description*, Banner* (upload/library), Package Visibility* (By Advertiser / By Persona), Advertiser/Client* |
| | | → Click **Next** to unlock Section 2 |
| 2 | Package Configuration | Visibility Date*, Flight Window*, Package Duration, Max Qty/Duration, Max Qty/Advertiser, Package Cost |
| 3 | Line Items | Add campaign types (e.g., Sponsored Display Ads) |
| 4 | Package Commitment (Optional) | Commitment Type + Line Item + Target Value |
| 5 | Package Rules (Optional) | Define performance-based automation rules |

**Banner Upload:**
- Drag and drop OR upload image file
- OR "Choose creative from library"
- Max size: 5MB, Min: 0.01MB, Aspect Ratio: 1:1

**Bottom Actions:** Save As Draft | Preview Package

**Workflow End:** ✅ Package created → appears in Packages list.

---

## 7. Sales Planner
**URL:** `/packages/salesPlanner`
**Breadcrumb:** Packages → Sales Planner

### 7.1 Sales Planner Table
**Toolbar:** Refresh | Column Selector | Search Package Name | Download | Add Filter
**Table Columns:**
`Package Name | Flight Window Start Date | Flight Window End Date | Days to start | View Details`

---

### 7.2 View Details → Package Duration Detail Drawer

**Drawer:** "Bookings By Package Duration"
**Header:** Flight Window dates

#### 7.2.1 Package Duration Cards (horizontal scroll)
Each card shows:
- Duration label (e.g., "13 Nov 25 – 14 Nov 25")
- Booked: X/Y (e.g., 1/1)
- On Hold: -
- Fill Rate (e.g., 100%)
- Revenue (e.g., ₹4,850)

#### 7.2.2 Bookings Table (within drawer)
**Toolbar:** Add Filter | Refresh | Column Selector | Search Booking Name
**Table Columns:**
`Status | Booking ID | Booking Name (link) | Note | Flight Start Date | Flight End Date | Booking Cost`

**Status Values:** DELIVERED, ACTIVE, SCHEDULED, ON HOLD, CANCELLED

---

#### 7.2.3 Booking Name Link → Booking Detail Drawer (nested)
**URL:** `/packages/salesPlanner/drawer/FLEXI_PACKAGE_BOOKING?bookingId={id}&packageId={id}&isBookingPage=true&clientId={id}`

**Drawer Header:**
- Booking Name (e.g., "AN Booking -1")
- Package Banner Image
- Package Name + Status badge (e.g., Delivered)
- Flight Window dates
- Total Line Items
- Payment Status (e.g., Paid)

**Booking Details Section:**
- Booking Name
- Select Duration
- Note

**Line Items (expandable accordion per item):**
Each Line Item shows:
- Line Item Type (e.g., Sponsored Display Ads)
- Page Selected (e.g., Home Page)
- Inventory (link → "3 Inventories")
- Keywords section → "ALL KEYWORDS" link
- Daily Impressions Cap (View Only, e.g., 50,000)
- Close button

**Package Pricing Section:**
- Selected Duration dates
- Apply Discount
- Amount (e.g., ₹50)
- Price Breakdown:
  - Total Cost (e.g., ₹4,000)
  - GST (e.g., ₹500)
  - SGST (e.g., ₹400)
  - (further line items...)

**Footer:** Done button

**Workflow End:** ✅ Booking details fully reviewed.

---

## 8. All Bookings → Bookings
**URL:** `/packages/flexiBookings/list`
**Breadcrumb:** Packages → All Bookings → Bookings

### 8.1 Page-Level KPI Cards
| Metric | Value |
|---|---|
| No. of Scheduled Bookings | 36 |
| No. of Bookings on Hold | 0 |
| No. of Bookings with no creatives | 102 |

### 8.2 Bookings Table
**Toolbar:**
- Clear Multi-Sort
- Refresh (↻)
- Download (↓)
- Column Selector
- Search Booking Name
- Add Filter (with badge for active filters)

**Table Columns:**
`[Banner Thumbnail] | Status | Booking Name (link) | Package Name | Note | Creative Status (progress bar) | View | ⋮`

**Status Values:** Active (●), Cancelled (✗), Delivered (✓), Scheduled (📅), On Hold

---

### 8.3 Booking Row — Actions

#### 8.3.1 Booking Name Link / View → Booking Detail Drawer
**URL:** `/packages/flexiBookings/list/drawer/FLEXI_PACKAGE_BOOKING?bookingId={id}&packageId={id}&isBookingPage=true&clientId={id}`

**Drawer Content:**
- Package Banner image
- Package Name + Status badge
- Flight Window dates
- Total Line Items
- Payment Status
- Booking Name, Select Duration, Note
- **"Add the required details for each line item below"** notice
- Line Items Setup progress bar (e.g., 100%)
- Line Item accordion (Completed badge shown when fully setup)

##### 8.3.1.1 Line Item Accordion Expanded:
- Line Item Type (e.g., Sponsored Display Ads)
- Page Selected (e.g., Home Page)
- Inventory link (e.g., "3 Inventories")
- Keywords targeting details
- Daily Impressions Cap

**Footer:** Done button

**Workflow End:** ✅ Booking creative setup complete.

---

#### 8.3.2 Kebab Menu (⋮) on Booking Row
- **Analytics** → Opens analytics drawer for that booking

##### 8.3.2.1 Analytics Drawer (from All Bookings)
Same structure as Section 2.3.2.1 — Campaign Performance for selected date range with KPI cards, performance summary chart, and keyword breakdown table.

---

## 9. All Bookings → Line Item Review
**URL:** `/packages/flexiBookings/review`
**Breadcrumb:** Packages → All Bookings → Line Item Review

### 9.1 Line Item Review Table
**Toolbar:**
- Refresh (↻)
- Filter icon (with badge — e.g., 4 active filters)
- Column Selector
- Search Line Item Name

**Table Columns:**
`Status | Line Item Name | Campaign Type | Booking Reference (link) | Merchant Name | Line Item Created Date | View`

**Status Values:** Active (●), Under Review (📋)

---

### 9.2 View → Line Item Review Drawer
**URL:** `/packages/flexiBookings/review/drawer/GOAL_LAUNCHER/INVENTORY_AUCTION?defaultCardToOpen=CONFIG&goalId={id}&isEditMode=true&clientId={id}&isReviewMode=true&campaignId={id}`

**Drawer Header:**
- Line Item name (e.g., "Line Item (9th Mar | 14:39:22)")
- Creatives Status badge: "1/2 PENDING REVIEWS" (link)
- Keywords Status badge: "REVIEWED"

#### 9.2.1 Inventory Selection Section
- Pages selected (e.g., "1 Page selected: Home Page")
- **Available Inventory Table:**

| Column | Description |
|---|---|
| Inventory Name | Name of the ad placement |
| Min. CPM bid | Minimum cost per thousand impressions |
| Est. Daily Impressions | Estimated daily reach |
| Tags | Labels/tags for the inventory |

**Sample Inventories:**
- Text Ad Box (₹0)
- Home Page MJ (₹10)
- Pre-acution-automation (₹10K)
- [SDK USE ONLY] Home Page Banner (₹1)
- [SDK USE ONLY] Home Page Image Ad (₹1)
- [SDK USE ONLY] Home Page Interstitial (₹1)
- test sdk image (₹20)
- SDK V2 Auction Inventory (₹20)
- TestInventory (₹100)
- Optional SDK Image (₹30)
- Paypal SDK Image Ad (₹1)
- SDK Testing | Auction (₹10)
- Copy of [Do not use - Test Inventory] (₹0.2)
- [3rd party tracking test] - INV - 002 (₹0.2)
- [3rd party tracking test] - INV - 004 (₹0.1)
- Hyperlink test - INV - 001 - BA (₹0.1)
- Test Deep Paypal (₹1,000)
- [Description test] - Inv (₹0.1)
- Hackathon Vibe (₹10)
- [SDK NEW USE ONLY] Home Page Banner (₹1)
- [SDK NEW USE ONLY] Home Page Interstitial (₹1)

#### 9.2.2 Review Actions
- Reviewer can approve or reject creatives/keywords
- Booking Reference link leads to the full booking detail

**Workflow End:** ✅ Line item reviewed and actioned (Approved/Rejected).

---

## Full Package Flow Summary (End-to-End)

```
[Left Nav: Packages (Alpha)]
│
├─► BOOKINGS  /packages/bookings
│       │
│       ├─ View Booking ──► Booking Detail Drawer
│       │       ├─ Step 1: Inventory Selection  (pages, slots)
│       │       ├─ Step 2: Keywords             (targeted keywords)
│       │       ├─ Step 3: Ads Upload           (creative status)
│       │       └─ Bid Details Panel            (base price, bidders, highest bid)
│       │
│       └─ ⋮ Kebab
│               ├─ Analytics ──► Performance Drawer
│               │       ├─ KPIs: Ad Revenue, Impressions, CTR, CPC, Clicks
│               │       ├─ Performance Summary Chart (daily)
│               │       └─ Keyword Performance Table
│               └─ Change History ──► Change History Drawer
│                       └─ Table: Date, Entity, Level, Type, Changed By
│
├─► ANALYTICS
│       ├─ Package Analytics  /packages/flexiAnalytics/package
│       │       ├─ Package Level Report Table
│       │       ├─ Booking Snapshot Table
│       │       └─ Line Items Performance Snapshot Table
│       │
│       ├─ Sales Analytics  /packages/flexiAnalytics/sales
│       │       ├─ KPIs: Qty Sold, Revenue Booked
│       │       ├─ Performance Trends Chart
│       │       └─ Package Sales Report Table
│       │
│       └─ Live Analytics  /packages/flexiAnalytics/liveAnalytics
│               ├─ KPIs: Ad Impressions, Ad Clicks, CTR
│               ├─ Hourly Performance Trend Chart
│               └─ Live Bookings Table
│
├─► PACKAGES  /packages/flexiPackages
│       │
│       ├─ KPIs: Total, Active, Draft, Paused
│       │
│       ├─ + Create New Package ──► Creation Drawer
│       │       ├─ Section 1: Package Details
│       │       │       ├─ Name*, Description*, Banner* (upload / library)
│       │       │       ├─ Visibility: By Advertiser OR By Persona
│       │       │       └─ Advertiser/Client selector
│       │       ├─ Section 2: Package Configuration
│       │       │       ├─ Visibility Date*
│       │       │       ├─ Flight Window*
│       │       │       ├─ Package Duration (days)
│       │       │       ├─ Max Qty/Duration & Max Qty/Advertiser
│       │       │       ├─ Package Cost
│       │       │       └─ Additional Cost (optional)
│       │       ├─ Section 3: Line Items
│       │       │       └─ Add Line Item (type: Sponsored Display Ads, etc.)
│       │       ├─ Section 4: Package Commitment (optional)
│       │       │       └─ Commitment type + target value
│       │       └─ Section 5: Package Rules (optional)
│       │               └─ Performance-based automation rules
│       │
│       ├─ View Package Name ──► Package Detail Drawer (same sections as above)
│       │
│       └─ ⋮ Kebab
│               ├─ Edit   ──► Edit Drawer
│               └─ Archive ──► Archives package
│
├─► SALES PLANNER  /packages/salesPlanner
│       │
│       └─ View Details ──► Package Duration Drawer
│               ├─ Package Duration Cards (Booked, On Hold, Fill Rate, Revenue)
│               └─ Bookings Table
│                       └─ Booking Name Link ──► Booking Detail Drawer
│                               ├─ Package Info (banner, name, status)
│                               ├─ Booking Details (name, duration, note)
│                               ├─ Line Item Accordion (type, page, inventory, keywords)
│                               └─ Package Pricing (discount, GST, SGST, total)
│
└─► ALL BOOKINGS
        ├─ Bookings  /packages/flexiBookings/list
        │       │
        │       ├─ KPIs: Scheduled, On Hold, No Creatives
        │       │
        │       ├─ View ──► Booking Detail Drawer
        │       │       ├─ Package banner + info
        │       │       ├─ Line Items Setup progress bar
        │       │       └─ Line Item Accordion (expanded details)
        │       │
        │       └─ ⋮ Kebab
        │               └─ Analytics ──► Campaign Performance Drawer
        │                       ├─ KPIs: Ad Revenue, Impressions, CTR, CPC, Clicks
        │                       ├─ Performance Summary Chart
        │                       └─ Keyword Performance Table
        │
        └─ Line Item Review  /packages/flexiBookings/review
                │
                ├─ Table: Status, Line Item Name, Campaign Type, Booking Ref, Merchant
                │
                └─ View ──► Line Item Review Drawer
                        ├─ Creatives Status: X/Y PENDING REVIEWS
                        ├─ Keywords Status: REVIEWED / PENDING
                        ├─ Inventory Selection Section
                        │       └─ Available Inventories Table
                        │               (Inventory Name, Min CPM bid, Est. Daily Impressions, Tags)
                        └─ Review Actions: Approve / Reject creatives & keywords
                                └─ ✅ WORKFLOW COMPLETE
```

---

## URL Reference Map

| Page | URL Path |
|---|---|
| Bookings | `/packages/bookings` |
| Booking Detail Drawer | `/packages/bookings/drawer/GOAL_LAUNCHER/PRE_AUCTION_BOOKINGS` |
| Booking Analytics Drawer | `/packages/bookings/drawer/GOAL_LAUNCHER/INVENTORY_AUCTION` |
| Booking Change History | `/packages/bookings/drawer/CHANGE_HISTORY_V2` |
| Package Analytics | `/packages/flexiAnalytics/package` |
| Sales Analytics | `/packages/flexiAnalytics/sales` |
| Live Analytics | `/packages/flexiAnalytics/liveAnalytics` |
| Packages List | `/packages/flexiPackages` |
| Package Detail/Create Drawer | `/packages/flexiPackages/drawer/FLEXI_PACKAGE_LAUNCHER` |
| Sales Planner | `/packages/salesPlanner` |
| Sales Planner Booking Detail | `/packages/salesPlanner/drawer/FLEXI_PACKAGE_BOOKING` |
| All Bookings — Bookings | `/packages/flexiBookings/list` |
| All Bookings — Booking Detail | `/packages/flexiBookings/list/drawer/FLEXI_PACKAGE_BOOKING` |
| Line Item Review | `/packages/flexiBookings/review` |
| Line Item Review Drawer | `/packages/flexiBookings/review/drawer/GOAL_LAUNCHER/INVENTORY_AUCTION` |

---

*Generated by tracing the QA Pulse web application — Packages (Alpha) module — 27 Mar 2026.*
