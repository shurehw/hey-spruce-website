# GroundOps Website Image Setup Guide

## Required Images List

Based on the original GroundOps website, here are the images you need to add to your `images/` folder:

### 1. Logo Files (Priority: HIGH)
- `logo.png` - Main logo for header (recommended: 300x100px, transparent background)
- `logo-white.png` - White version for footer/dark backgrounds
- `favicon.ico` - Small icon for browser tabs (16x16px or 32x32px)
- `apple-touch-icon.png` - For mobile devices (180x180px)

### 2. Hero/Header Images (Priority: HIGH)
- `hero-kitchen-cleaning.jpg` - Main hero background (1920x800px minimum)
  - Should show: Professional kitchen cleaning in action or pristine commercial kitchen
  - Style: Bright, professional, with overlay capability

### 3. Service Images (Priority: HIGH)
Place these in the services section - recommended size: 600x400px each:
- `kitchen-deep-cleaning.jpg` - Kitchen deep cleaning service
- `hood-exhaust-cleaning.jpg` - Hood and exhaust system cleaning
- `floor-cleaning.jpg` - Industrial floor cleaning/scrubbing
- `emergency-cleaning.jpg` - Emergency/rapid response cleaning
- `grease-trap-cleaning.jpg` - Grease trap cleaning service
- `nightly-cleaning.jpg` - Nightly porter/bar cleaning service

### 4. Additional Service Images (Priority: MEDIUM)
- `fryer-oil-collection.jpg` - Fryer oil disposal/collection
- `maintenance.jpg` - Kitchen equipment maintenance
- `organic-waste.jpg` - Waste management service
- `pressure-washing.jpg` - Exterior pressure washing

### 5. Before/After Gallery (Priority: HIGH for SEO)
Create a `gallery/` subfolder with:
- `before-kitchen-1.jpg` and `after-kitchen-1.jpg`
- `before-kitchen-2.jpg` and `after-kitchen-2.jpg`
- `before-hood-1.jpg` and `after-hood-1.jpg`
- `before-floor-1.jpg` and `after-floor-1.jpg`

### 6. Team/About Images (Priority: MEDIUM)
- `team-cleaning.jpg` - Team in action wearing GroundOps uniforms
- `team-photo.jpg` - Professional team photo
- `owner.jpg` - Owner/founder photo (if comfortable)

### 7. Trust/Certification Badges (Priority: HIGH)
- `ikeca-certified.png` - IKECA certification badge
- `bbb-accredited.png` - BBB accreditation
- `licensed-insured.png` - Licensed & insured badge
- `health-inspector-approved.png` - Health dept approval

### 8. Location/Local Images (Priority: MEDIUM for Local SEO)
- `los-angeles-service-area.jpg` - Map or LA skyline
- `downtown-la-cleaning.jpg` - Downtown LA specific
- `beverly-hills-cleaning.jpg` - Beverly Hills area
- `santa-monica-cleaning.jpg` - Santa Monica area

### 9. Blog Post Featured Images (Priority: LOW)
For each blog post, create a featured image:
- `blog/health-code-changes-2024.jpg`
- `blog/restaurant-cleaning-cost.jpg`
- `blog/cleaning-frequency-guide.jpg`
- `blog/nfpa-96-compliance.jpg`

## Image Optimization Guidelines

### File Sizes:
- Hero images: Max 200KB (use JPEG at 80-85% quality)
- Service images: Max 100KB each
- Logos: PNG format with transparency
- Gallery images: Max 150KB each

### SEO Best Practices:
1. **File Names**: Use descriptive names with keywords
   - Good: `restaurant-kitchen-cleaning-los-angeles.jpg`
   - Bad: `IMG_12345.jpg`

2. **Alt Text**: Already added in HTML, describes image content and includes keywords

3. **Compression Tools**:
   - Use TinyPNG.com for PNG files
   - Use JPEG-Optimizer.com for JPEG files
   - Or use local tools like ImageOptim

### How to Add Images:

1. **Create the images folder:**
```bash
mkdir "C:\Users\JacobShure\spruce website\images"
mkdir "C:\Users\JacobShure\spruce website\images\gallery"
mkdir "C:\Users\JacobShure\spruce website\images\blog"
```

2. **Download images from your Google Drive**

3. **Rename according to the list above**

4. **Optimize file sizes**

5. **Place in appropriate folders**

## CSS Already Prepared

The styles.css file already has styling for:
- Service card images
- Hero background
- Gallery grid
- Responsive image handling

## Where Images Will Appear:

### Homepage (index.html):
- Logo in header navigation
- Hero background image
- 6 service card images
- Before/after gallery section
- Trust badges near testimonials
- Footer logo

### Blog Posts:
- Featured image at top of each post
- Inline images for demonstrations
- Charts/infographics as needed

### Local Pages:
- Area-specific hero images
- Local landmark photos
- Service area maps

## Quick Implementation:

Once you've added the images to the folders, the website will automatically display them. The HTML references are already in place with proper alt text for SEO.

## Missing Images Fallback:

If any images are missing, the site will still function but with:
- Emoji icons as placeholders (currently active)
- Solid color backgrounds
- Text-based logo

## Priority Order for Adding Images:

1. **First Priority (Do Today):**
   - Logo files
   - Hero image
   - Main service images

2. **Second Priority (This Week):**
   - Before/after gallery
   - Trust badges
   - Team photos

3. **Third Priority (As Available):**
   - Blog featured images
   - Additional service images
   - Local area images

## Need Stock Photos?

If you need professional stock photos, consider:
- Unsplash.com (free)
- Pexels.com (free)
- Shutterstock (paid, but high quality)
- Getty Images (premium)

Search terms to use:
- "commercial kitchen cleaning"
- "restaurant kitchen professional"
- "industrial cleaning service"
- "Los Angeles restaurant"
- "clean commercial kitchen"

## Color Matching:

Your brand colors from original site:
- Primary Teal: #14b8a6
- Dark Teal: #0d9488
- Light Background: #f0fdfa
- Text Dark: #134e4a

Make sure any new images complement these colors.