# Happy Mobile Coding Setup - spruce website

This repo is configured for seamless coding between VS Code (desktop) and Happy app (mobile).

## 🌿 Branch Strategy

- **`master`** - Production branch (auto-deploys to Vercel) ⚠️
- **`dev`** - Mobile coding branch (does NOT deploy) ✅

**Important:** Code on your phone using the `dev` branch. When ready to deploy, merge `dev` → `master`.

## 🚀 Quick Start

### On Your Phone (Happy App)

1. **Clone the repo** in Happy app
2. **Switch to dev branch**: `git checkout dev`
3. **Always work on dev branch in Happy!**

### Auto-Sync

Run auto-sync on your PC:

```bash
cd "c:\Users\JacobShure\spruce website"
node auto-sync.js
```

This will:
- Auto-pull changes from GitHub every 5 minutes
- Auto-commit and push your changes on the `dev` branch
- **Won't trigger Vercel deployments** (dev branch doesn't deploy!)

**To deploy to production:**
```bash
git checkout master
git merge dev
git push
# This triggers Vercel deployment
```

---

Happy coding on the go! 🎉
