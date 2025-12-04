# 🔧 Troubleshooting Vercel Deployment Issues

If you're still getting errors after adding environment variables and redeploying, follow these steps:

## Step 1: Check What Error You're Seeing

### Common Errors:

1. **500 Internal Server Error** - Usually means:

   - Database connection failed
   - Missing environment variables
   - Code error

2. **Database Connection Error** - Means:

   - POSTGRES_URL is wrong
   - Database not accessible
   - Wrong credentials

3. **Static Files Not Loading** - Means:
   - Static files not collected
   - STATIC_URL misconfigured

## Step 2: Check Vercel Logs

**This is the most important step!**

1. Go to **Vercel Dashboard** → Your Project
2. Click on **Deployments** tab
3. Click on the latest deployment
4. Click **View Function Logs** or **View Build Logs**
5. Look for error messages (usually in red)

**What to look for:**

- Database connection errors
- Missing environment variables
- Import errors
- Django errors

## Step 3: Verify Environment Variables

Make sure they're set correctly:

1. **Vercel Dashboard** → Your Project → **Settings** → **Environment Variables**
2. Verify these exist:

   - ✅ `SECRET_KEY` (long random string)
   - ✅ `DEBUG` = `False` (not `true` or `True`, must be exactly `False`)
   - ✅ `ALLOWED_HOSTS` = `e-shopping-diisqbs9v-asim-khans-projects-a9a2e6c6.vercel.app,*.vercel.app`
   - ✅ `POSTGRES_URL` = `postgresql://...` (full connection string)

3. **Important:** Make sure they're set for **Production** environment (or all environments)

## Step 4: Test Database Connection

The POSTGRES_URL might be wrong. Let's verify:

### Check Connection String Format:

It should look like:

```
postgresql://username:password@host:port/database?sslmode=require
```

**Common issues:**

- Missing `postgresql://` at the start
- Wrong password (with special characters that need encoding)
- Missing `?sslmode=require` at the end
- Wrong host/port

### Test Connection Locally:

```bash
# Pull environment variables
vercel env pull .env.local

# Test database connection
python manage.py dbshell
```

If this fails, your POSTGRES_URL is wrong.

## Step 5: Check Neon Database Status

1. Go to **Neon Dashboard**: https://console.neon.tech
2. Check if database is **Active**
3. Verify you can see the connection string
4. Make sure database is not paused (Neon pauses inactive databases)

## Step 6: Common Fixes

### Fix 1: Re-add Environment Variables

Sometimes Vercel doesn't pick them up. Try:

1. **Delete** all environment variables
2. **Add them again** one by one
3. **Redeploy**:
   ```bash
   vercel --prod
   ```

### Fix 2: Check DEBUG Setting

Make sure `DEBUG` is exactly `False` (capital F, lowercase rest):

- ✅ Correct: `False`
- ❌ Wrong: `false`, `FALSE`, `True`, `true`

### Fix 3: Verify ALLOWED_HOSTS

Make sure it includes your exact domain:

```
e-shopping-diisqbs9v-asim-khans-projects-a9a2e6c6.vercel.app,*.vercel.app
```

### Fix 4: Check POSTGRES_URL Format

If your password has special characters, they need to be URL-encoded:

- `@` becomes `%40`
- `#` becomes `%23`
- `$` becomes `%24`
- etc.

Or regenerate password in Neon with only alphanumeric characters.

### Fix 5: Force Redeploy

Sometimes a simple redeploy doesn't work:

```bash
# Remove deployment
vercel remove

# Deploy fresh
vercel --prod
```

## Step 7: Check Django Settings

Make sure your `settings.py` is reading environment variables correctly.

The code should be:

```python
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-key')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*').split(',')
```

## Step 8: Test Locally with Production Settings

```bash
# Pull environment variables
vercel env pull .env.local

# Test locally
python manage.py check --deploy
python manage.py migrate
python manage.py runserver
```

If it works locally, the issue is with Vercel deployment.

## Step 9: Check Vercel Function Logs

1. **Vercel Dashboard** → Your Project
2. **Functions** tab (or **Logs** tab)
3. Look for recent errors
4. Check for:
   - Import errors
   - Database connection errors
   - Missing modules

## Step 10: Verify Requirements.txt

Make sure all dependencies are listed:

```txt
Django==5.0.1
boto3==1.34.34
Pillow==10.2.0
dj-database-url==2.1.0
psycopg2-binary==2.9.9
whitenoise==6.6.0
```

## Quick Diagnostic Commands

Run these to check:

```bash
# Check if environment variables are set
vercel env ls

# Pull and check locally
vercel env pull .env.local
cat .env.local

# Test database connection
python manage.py dbshell
```

## Still Not Working?

1. **Share the error message** from Vercel logs
2. **Check if database is accessible** from Neon dashboard
3. **Try creating a new Neon database** and use that connection string
4. **Check Vercel function timeout** (Django can be slow on first request)

## Alternative: Use Railway or Render

If Vercel continues to have issues, consider:

- **Railway**: https://railway.app (easier Django deployment)
- **Render**: https://render.com (free tier, simpler setup)

These platforms are more Django-friendly than Vercel.

## Need More Help?

Share:

1. The exact error message from Vercel logs
2. Screenshot of your environment variables (hide sensitive parts)
3. What happens when you visit your app URL

This will help diagnose the specific issue!


