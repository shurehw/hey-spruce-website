# GroundOps Developer Handoff Documentation

## Project Overview
Professional restaurant cleaning service website and portal system with integrated contract management and B2B operations.

**Live Site**: https://hey-spruce-website.vercel.app/
**Repository**: GitHub integration configured with auto-deployment

---

## Portal Architecture

### 🌟 Customer Portal (Public Website)
**Location**: `C:\Users\JacobShure\spruce website\`
**Purpose**: Public-facing website for GroundOps cleaning services
**Status**: ✅ **LIVE & DEPLOYED**

**Key Files**:
- `index.html` - Main landing page with SEO optimization
- `styles.css` - Main stylesheet (navy #5f6b9b branding)
- `blog.html`, `blog-post.html` - Content marketing pages
- `vercel.json` - Deployment configuration

**Features**:
- Professional navy blue branding (#5f6b9b)
- Mobile-responsive design (28px border radius)
- SEO optimized with structured data
- Vercel deployment with auto-deploy on git push
- Health inspection pass guarantee messaging

### 🏢 Internal SHW Portal (Supplier Management)
**Location**: `C:\Users\JacobShure\spruce website\supplier-portal.html`
**Purpose**: Internal contract management and client operations
**Status**: ✅ **BUILT & FUNCTIONAL**

**Key Files**:
- `supplier-portal.html` - Contract management interface (17.4KB)
- `portal-styles.css` - Portal-specific styling (6.9KB)  
- `portal-script.js` - Contract generation logic (18KB)

**Features**:
- 6 pre-built contract templates (Standard Restaurant, Quick Service, Bar & Nightclub, etc.)
- Dynamic form generation for client contracts
- PDF generation and email integration ready
- Contract tracking and management system
- Template-based workflow for different service types

---

## B2B Admin System
**Location**: `C:\Users\JacobShure\b2b-admin-portal\`
**Status**: ✅ **ACTIVE DEVELOPMENT**

### Components:
1. **Quote Builder** (`/quote-builder`) - Main quote generation system
2. **Art Proofs Functions** (`/art-proofs-functions`) - Firebase functions for art workflows
3. **Firebase Functions** (`/firebase-functions`) - Backend services and PDF generation

---

## Data & Integration Ecosystem
**Location**: `C:\Users\JacobShure\syncs-and-backups\`
**Status**: ✅ **OPERATIONAL** (150+ files)

### Key Systems:
- **Airtable Synchronization**: Client data management
- **Supabase Integration**: Database operations
- **QuickBooks Sync**: Financial data flow
- **Email Automation**: Client communication workflows
- **Data Export Tools**: Cross-platform data management

### Critical Files:
- `airtable_to_supabase.py` - Primary data sync (3.2KB)
- `email_automation.py` - Client communication (2.1KB)
- `quickbooks_integration.py` - Financial sync (1.8KB)

---

## EcoTrack Provider Export
**Location**: `C:\Users\JacobShure\ecotrack provider\`
**Status**: ✅ **COMPLETE**
**Purpose**: Export service providers from EcoTrack to local database

**Features**:
- SQLite/MySQL/PostgreSQL support
- Pagination handling
- JSON backup creation
- Comprehensive error logging

---

## Technical Specifications

### Deployment Stack:
- **Frontend**: Static HTML/CSS/JavaScript
- **Hosting**: Vercel with auto-deployment
- **Version Control**: GitHub integration
- **Database**: SQLite (local), Supabase (cloud)
- **Backend Services**: Firebase Functions

### Key Dependencies:
- Playwright for web scraping
- GitHub CLI for repository management
- Vercel CLI for deployment
- Firebase SDK for backend services

### Color Scheme & Branding:
```css
:root {
  --primary-color: #5f6b9b;    /* GroundOps Navy */
  --secondary-color: #667eea;   /* Accent Blue */
  --border-radius: 28px;        /* Modern rounded corners */
}
```

---

## Development Workflow

### Current Process:
1. Local development in `C:\Users\JacobShure\spruce website\`
2. Git commit with descriptive messages
3. `git push` triggers automatic Vercel deployment
4. Live site updates within seconds

### Repository Structure:
```
spruce-website/
├── index.html              # Main website
├── supplier-portal.html    # Internal contract portal
├── styles.css              # Main styling
├── portal-styles.css       # Portal styling
├── portal-script.js        # Portal functionality
├── vercel.json            # Deployment config
└── blog/                  # Content marketing
```

---

## Next Development Priorities

### Immediate Tasks:
1. **Portal Integration**: Connect supplier portal to main website navigation
2. **Database Connection**: Link contract system to Supabase backend
3. **Authentication**: Implement login system for supplier portal
4. **Email Integration**: Connect contract sending to email automation

### Future Enhancements:
1. **Contract Analytics**: Track contract performance and conversion
2. **Client Dashboard**: Customer-facing portal for service tracking
3. **Mobile App**: Native app for field technicians
4. **API Development**: RESTful API for third-party integrations

---

## Access & Credentials

### Required Access:
- GitHub repository permissions
- Vercel project access
- Firebase project permissions
- Supabase database access

### Environment Variables Needed:
```env
# EcoTrack (if applicable)
ECOTRACK_USERNAME=
ECOTRACK_PASSWORD=

# Database
SUPABASE_URL=
SUPABASE_ANON_KEY=

# Email
EMAIL_SERVICE_API_KEY=
```

---

## Support & Documentation

### Contact Information:
- **Project Owner**: Jacob Shure
- **Primary Codebase**: `C:\Users\JacobShure\spruce website\`
- **Development History**: Comprehensive work across multiple Claude Code sessions

### Key Documentation:
- `push-to-github.md` - Git setup and deployment guide
- `README.md` (in each project) - Specific setup instructions
- This document - Complete project overview

---

**Last Updated**: September 6, 2025
**Status**: Ready for developer onboarding and collaboration