# 🔐 Environment Variables Explained

## What are Environment Variables?

Environment variables are **secret configuration values** that your app needs to run, but you don't want to hardcode in your files (for security reasons).

Think of them as **settings that change between development and production**.

## Why Do You Need Them?

### 1. **Security** 🔒

- **SECRET_KEY**: Django's encryption key (like a master password)
- **Database passwords**: You don't want these in your code
- **API keys**: Third-party service credentials

### 2. **Different Environments** 🌍

- **Development** (your computer): `DEBUG=True`, SQLite database
- **Production** (Vercel): `DEBUG=False`, PostgreSQL database

### 3. **Flexibility** 🔄

- Change settings without modifying code
- Same code works in different environments

## Required Environment Variables for Your App

### 1. **SECRET_KEY** (Required)

**What it is:** Django's secret key for encryption
**Why needed:** Used for:

- Session security
- Password hashing
- CSRF protection
- Signing cookies

**How to generate:**

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

**Example:**

```
SECRET_KEY=django-insecure-abc123xyz789... (long random string)
```

### 2. **DEBUG** (Required)

**What it is:** Shows/hides error pages
**Why needed:**

- `True` in development (shows detailed errors)
- `False` in production (hides errors from users)

**Value:**

```
DEBUG=False
```

### 3. **ALLOWED_HOSTS** (Required)

**What it is:** List of domains your app can run on
**Why needed:** Security - prevents others from using your app

**Value:**

```
ALLOWED_HOSTS=your-app.vercel.app,*.vercel.app
```

(Replace `your-app` with your actual Vercel app name)

### 4. **POSTGRES_URL** (Required)

**What it is:** Database connection string
**Why needed:** Vercel doesn't support SQLite, needs PostgreSQL

**Format:**

```
POSTGRES_URL=postgresql://username:password@host:port/database
```

**Where to get:**

- Vercel Postgres (in Vercel dashboard)
- Railway, Supabase, Neon (free options)

## What Does "Pull Environment Variables" Mean?

When Vercel CLI asks: **"Would you like to pull environment variables now?"**

It means: **Download the environment variables from Vercel to your local `.env.local` file**

### Why Pull Them?

1. **Run migrations locally** - Connect to production database
2. **Create superuser** - Add admin user to production
3. **Test locally** - Use production settings
4. **Sync settings** - Keep local and production in sync

### What Happens When You Pull?

Vercel creates a `.env.local` file in your project with:

```
SECRET_KEY=your-secret-key
DEBUG=False
ALLOWED_HOSTS=your-app.vercel.app
POSTGRES_URL=postgresql://...
```

Then you can use these locally:

```bash
# Run migrations on production database
python manage.py migrate

# Create superuser on production database
python manage.py createsuperuser
```

## Should You Pull Now?

### ✅ **YES, Pull if:**

- You want to run migrations on production database
- You want to create a superuser
- You want to test with production settings
- You've already set environment variables in Vercel

### ❌ **NO, Don't Pull if:**

- You haven't set environment variables in Vercel yet
- You just want to deploy (not manage database)
- You're only testing locally

## Step-by-Step: Setting Environment Variables

### Method 1: Via Vercel Dashboard (Easiest)

1. Go to https://vercel.com/dashboard
2. Select your project
3. Go to **Settings** → **Environment Variables**
4. Click **Add New**
5. Add each variable:
   - Name: `SECRET_KEY`
   - Value: (paste your generated key)
   - Environment: Production, Preview, Development (select all)
   - Click **Save**
6. Repeat for: `DEBUG`, `ALLOWED_HOSTS`, `POSTGRES_URL`

### Method 2: Via Vercel CLI

```bash
# Add each variable
vercel env add SECRET_KEY
# Paste value when prompted

vercel env add DEBUG
# Type: False

vercel env add ALLOWED_HOSTS
# Type: your-app.vercel.app,*.vercel.app

vercel env add POSTGRES_URL
# Paste your database connection string
```

### Method 3: Pull After Setting in Dashboard

```bash
# After setting in dashboard, pull to local file
vercel env pull .env.local
```

## Example: Complete Setup

```bash
# 1. Generate secret key
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
# Copy the output

# 2. Set in Vercel (via dashboard or CLI)
# SECRET_KEY = (paste generated key)
# DEBUG = False
# ALLOWED_HOSTS = your-app.vercel.app,*.vercel.app
# POSTGRES_URL = (your database URL)

# 3. Pull to local (optional)
vercel env pull .env.local

# 4. Use locally
python manage.py migrate
python manage.py createsuperuser
```

## Security Notes ⚠️

1. **Never commit `.env.local`** - It's in `.gitignore` for a reason
2. **Never share your SECRET_KEY** - Keep it secret
3. **Rotate keys regularly** - Change SECRET_KEY periodically
4. **Use different keys** - Dev and production should have different keys

## Troubleshooting

### Issue: "Environment variable not found"

**Solution:** Make sure you set it in Vercel dashboard first

### Issue: "Can't connect to database"

**Solution:** Check POSTGRES_URL format and database credentials

### Issue: ".env.local not working"

**Solution:** Make sure file is in project root, restart terminal

## Summary

- **Environment variables** = Secret settings for your app
- **Pull** = Download from Vercel to your computer
- **Set first** = Add variables in Vercel before pulling
- **Use locally** = Run migrations, create users, etc.

Need help? Check `VERCEL_DEPLOY.md` for full deployment guide!


