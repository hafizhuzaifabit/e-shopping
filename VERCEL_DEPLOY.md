# 🚀 Deploying ShopSmart to Vercel

Complete guide to deploy your Django e-commerce application on Vercel.

## ⚠️ Important Note

**Vercel is primarily designed for serverless functions and static sites.** While Django can work on Vercel, it has limitations:

- No persistent file storage (use S3/Cloudinary for media)
- Cold starts can be slow
- Database must be external (PostgreSQL recommended)

**Alternative platforms** that work better with Django:

- **Railway** (https://railway.app) - Excellent Django support
- **Render** (https://render.com) - Free tier, easy setup
- **Fly.io** (https://fly.io) - Great for Django apps

## 📋 Prerequisites

1. ✅ GitHub account
2. ✅ Vercel account (sign up at https://vercel.com)
3. ✅ PostgreSQL database (Vercel Postgres, Railway, Supabase, or Neon)

## 🔧 Step 1: Prepare Your Code

### Why GitHub? (Optional but Recommended)

**You DON'T need GitHub!** Vercel supports multiple deployment methods:

1. **GitHub/GitLab/Bitbucket** (Recommended) - Automatic deployments, easy updates
2. **Vercel CLI** - Deploy directly from your computer
3. **Drag & Drop** - Upload files directly (limited features)

### Option A: Deploy via Vercel CLI (No GitHub Needed!)

This is the easiest way if you don't want to use GitHub:

```bash
# Install Vercel CLI
npm install -g vercel

# Login to Vercel
vercel login

# Deploy from your current directory
vercel

# Follow the prompts:
# - Set up and deploy? Yes
# - Which scope? (select your account)
# - Link to existing project? No
# - Project name? (your-app-name)
# - Directory? ./
# - Override settings? No

# Your app will be deployed!
```

**That's it!** No GitHub needed. Your code is deployed directly from your computer.

### Option B: Push to GitHub (For Automatic Deployments)

If you want automatic deployments when you push code:

```bash
git init
git add .
git commit -m "Ready for Vercel deployment"
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```

**Benefits of GitHub:**

- Automatic deployments on every push
- Easy rollbacks
- Team collaboration
- Version history

### Option C: Drag & Drop (Limited)

1. Go to Vercel Dashboard
2. Click "Add New Project"
3. Select "Deploy" tab
4. Drag your project folder
5. Deploy (limited to static sites, not ideal for Django)

### 1.2 Generate Secret Key

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Save this key - you'll need it for environment variables.

## 🗄️ Step 2: Set Up Database

Vercel doesn't support SQLite. You need PostgreSQL:

### Option A: Vercel Postgres (Easiest)

1. Go to Vercel Dashboard → Your Project → Storage
2. Click "Create Database" → Select "Postgres"
3. Copy the connection string

### Option B: External Services (Recommended)

- **Railway**: https://railway.app (Free tier)
- **Supabase**: https://supabase.com (Free tier)
- **Neon**: https://neon.tech (Free tier)

## 🚀 Step 3: Deploy to Vercel

### Method 1: Vercel CLI (Easiest - No GitHub Needed!) ⭐

**This is the simplest way - deploy directly from your computer:**

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy from your project directory
cd C:\Users\Huzaifa\Desktop\E-comerce
vercel

# Follow prompts, then set environment variables:
vercel env add SECRET_KEY
vercel env add DEBUG
vercel env add ALLOWED_HOSTS
vercel env add POSTGRES_URL

# Deploy to production
vercel --prod
```

**See `DEPLOY_WITHOUT_GITHUB.md` for detailed CLI instructions.**

### Method 2: Vercel Dashboard (Requires GitHub)

1. **Go to Vercel Dashboard**

   - Visit https://vercel.com/dashboard
   - Click "Add New Project"

2. **Import Repository**

   - Select your GitHub repository
   - Vercel will auto-detect settings

3. **Configure Project Settings**

   - **Framework Preset**: Other
   - **Root Directory**: `./` (leave as is)
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)
   - **Install Command**: `pip install -r requirements.txt`

4. **Add Environment Variables**
   Click "Environment Variables" and add:

   ```
   SECRET_KEY=your-generated-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=your-app.vercel.app,*.vercel.app
   POSTGRES_URL=postgresql://user:password@host:port/dbname
   ```

   **Important**: Replace `your-app.vercel.app` with your actual Vercel domain.

5. **Deploy**
   - Click "Deploy"
   - Wait 2-5 minutes for deployment

### Method 2: Vercel CLI

```bash
# Install Vercel CLI
npm install -g vercel

# Login
vercel login

# Deploy
vercel

# Set environment variables
vercel env add SECRET_KEY
vercel env add DEBUG
vercel env add ALLOWED_HOSTS
vercel env add POSTGRES_URL

# Deploy to production
vercel --prod
```

## 🗃️ Step 4: Run Migrations

After deployment, run migrations:

### Option A: Via Vercel CLI

```bash
# Pull environment variables
vercel env pull .env.local

# Run migrations locally (connects to production DB)
python manage.py migrate
```

### Option B: Via Django Admin

1. Access your admin panel: `https://your-app.vercel.app/admin/`
2. Create a superuser first (see Step 5)
3. Migrations may run automatically on first access

### Option C: Create Migration Function

Create a Vercel function to run migrations (advanced)

## 👤 Step 5: Create Superuser

```bash
# Set environment variables locally
export POSTGRES_URL="your-postgres-connection-string"
export SECRET_KEY="your-secret-key"

# Create superuser
python manage.py createsuperuser
```

## 📦 Step 6: Populate Products

```bash
# With environment variables set
python manage.py populate_products
```

## 📁 Step 7: Handle Static Files

Static files should be automatically served. If not:

1. **Collect static files locally:**

   ```bash
   python manage.py collectstatic --noinput
   ```

2. **Commit and push:**
   ```bash
   git add staticfiles/
   git commit -m "Add static files"
   git push
   ```

## 🖼️ Step 8: Media Files (Important!)

Vercel is serverless - uploaded files won't persist. Use external storage:

### Option A: AWS S3 (Recommended)

1. Create S3 bucket
2. Install boto3 (already in requirements.txt)
3. Configure Django to use S3 for media files
4. Update settings.py with S3 credentials

### Option B: Cloudinary

1. Sign up at https://cloudinary.com
2. Install django-cloudinary-storage
3. Configure in settings.py

### Option C: Vercel Blob Storage

1. Use Vercel's new Blob Storage feature
2. Configure in vercel.json

## ✅ Verification Checklist

- [ ] Code pushed to GitHub
- [ ] PostgreSQL database created
- [ ] Environment variables set in Vercel
- [ ] Deployment successful
- [ ] Migrations run
- [ ] Superuser created
- [ ] Products populated
- [ ] Static files loading
- [ ] Media files configured (S3/Cloudinary)

## 🔍 Troubleshooting

### Issue: 500 Internal Server Error

**Solution:**

- Check Vercel function logs
- Verify environment variables
- Check database connection

### Issue: Static files not loading

**Solution:**

- Run `collectstatic` locally
- Push staticfiles/ directory
- Check STATIC_URL in settings

### Issue: Database connection failed

**Solution:**

- Verify POSTGRES_URL format
- Check database credentials
- Ensure database allows connections from Vercel IPs

### Issue: Media uploads not working

**Solution:**

- Configure S3 or Cloudinary
- Update MEDIA_ROOT and MEDIA_URL
- Test file uploads

### Issue: Slow cold starts

**Solution:**

- This is normal for serverless
- Consider using Railway or Render for better performance

## 🎯 Production Checklist

Before going live:

- [ ] Set `DEBUG=False` in environment variables
- [ ] Generate strong `SECRET_KEY`
- [ ] Set proper `ALLOWED_HOSTS`
- [ ] Configure HTTPS (automatic on Vercel)
- [ ] Set up error monitoring (Sentry)
- [ ] Configure media file storage (S3/Cloudinary)
- [ ] Set up database backups
- [ ] Test all functionality
- [ ] Set up custom domain (optional)

## 📚 Additional Resources

- [Vercel Python Documentation](https://vercel.com/docs/concepts/functions/serverless-functions/runtimes/python)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/)
- [Railway Django Guide](https://docs.railway.app/guides/django)
- [Render Django Guide](https://render.com/docs/deploy-django)

## 🆘 Need Help?

If you encounter issues:

1. Check Vercel function logs
2. Review Django error logs
3. Verify all environment variables
4. Test database connection
5. Consider using Railway or Render for easier Django deployment

## 🎉 Success!

Once deployed, your app will be available at:
`https://your-app.vercel.app`

Good luck! 🚀
