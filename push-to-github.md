# Push GroundOps Website to GitHub

## Step 1: Authenticate with GitHub

Run this command and follow the prompts:
```bash
gh auth login
```

Choose:
- GitHub.com
- HTTPS
- Login with web browser (or paste authentication token)

## Step 2: Create Repository and Push

After authentication, run these commands:

```bash
# Navigate to your project
cd "C:\Users\JacobShure\groundops website"

# Create a new repository on GitHub
gh repo create groundops-website --public --source=. --remote=origin --push

# If the above doesn't work, try manual steps:
# 1. Create repo first
gh repo create groundops-website --public

# 2. Add remote
git remote add origin https://github.com/YOUR_USERNAME/groundops-website.git

# 3. Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Connect Vercel to GitHub (Optional but Recommended)

1. Go to your [Vercel Dashboard](https://vercel.com/jacob-shures-projects/groundops-website)
2. Go to Settings → Git
3. Connect to your GitHub repository
4. Now Vercel will auto-deploy on every push!

## Alternative: Manual GitHub Creation

If you prefer using the GitHub website:

1. Go to [github.com/new](https://github.com/new)
2. Name: `hey-spruce-website`
3. Description: "Professional restaurant cleaning services website for GroundOps"
4. Make it Public
5. Don't initialize with README (we already have files)
6. Create repository

Then run:
```bash
cd "C:\Users\JacobShure\spruce website"
git remote add origin https://github.com/YOUR_USERNAME/hey-spruce-website.git
git branch -M main
git push -u origin main
```

## Your Repository Will Include:

- ✅ Complete website (HTML, CSS, JS)
- ✅ All blog pages
- ✅ SEO optimizations
- ✅ Vercel configuration
- ✅ Deployment documentation
- ✅ .gitignore configured

## Benefits of GitHub + Vercel:

- 🔄 Auto-deploy on every push
- 📝 Version control history
- 🌍 Backup of your code
- 👥 Easy collaboration
- 🔍 Code search and management

---

After pushing to GitHub, your workflow will be:
1. Make changes locally
2. `git add .`
3. `git commit -m "Your message"`
4. `git push`
5. Vercel auto-deploys in seconds!