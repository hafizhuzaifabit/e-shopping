# 🔍 How to Find Your Neon Database Connection String

You've set up Neon database - great! Here's where to find the connection string.

## Method 1: From Vercel Dashboard (Easiest)

If you created Neon through Vercel:

1. **Go to Vercel Dashboard**

   - Visit: https://vercel.com/dashboard
   - Select your project: **e-shopping**

2. **Go to Storage Tab**

   - Click on **Storage** in the left sidebar
   - Or go to: Your Project → **Storage**

3. **Find Your Neon Database**

   - You should see your Neon database listed
   - Click on it

4. **Get Connection String**

   - Look for **"Connection String"** or **"Connection URL"**
   - It might be under **"Settings"** or **"Connection"** tab
   - Copy the entire string (it looks like: `postgresql://user:password@host/database`)

5. **Add to Environment Variables**
   - Go to **Settings** → **Environment Variables**
   - Add new variable:
     - **Name:** `POSTGRES_URL`
     - **Value:** (paste the connection string)
     - **Environment:** Select all (Production, Preview, Development)
     - Click **Save**

## Method 2: From Neon Dashboard (Direct)

If you created Neon separately:

1. **Go to Neon Dashboard**

   - Visit: https://console.neon.tech
   - Login with your account

2. **Select Your Project**

   - Click on your project name

3. **Go to Connection Details**

   - Look for **"Connection String"** or **"Connection Details"**
   - It's usually on the main dashboard or under **"Settings"**

4. **Copy Connection String**

   - You'll see something like:
     ```
     postgresql://username:password@ep-xxx-xxx.region.aws.neon.tech/neondb?sslmode=require
     ```
   - Click **"Copy"** button next to it

5. **Add to Vercel**
   - Go back to Vercel Dashboard
   - Your Project → **Settings** → **Environment Variables**
   - Add `POSTGRES_URL` with the copied string

## Method 3: Build Connection String Manually

If you can't find the full string, you can build it from parts:

1. **In Neon Dashboard**, find:

   - **Host:** (e.g., `ep-xxx-xxx.region.aws.neon.tech`)
   - **Database:** (usually `neondb` or your database name)
   - **User:** (your username)
   - **Password:** (your password)

2. **Build the string:**

   ```
   postgresql://USERNAME:PASSWORD@HOST/DATABASE?sslmode=require
   ```

   Example:

   ```
   postgresql://myuser:mypassword@ep-cool-123.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```

## What the Connection String Looks Like

A Neon connection string typically looks like:

```
postgresql://username:password@ep-xxxxx-xxxxx.region.aws.neon.tech/neondb?sslmode=require
```

Or with a specific database name:

```
postgresql://username:password@ep-xxxxx-xxxxx.region.aws.neon.tech/mydatabase?sslmode=require
```

## Quick Steps Summary

1. ✅ Vercel Dashboard → Your Project
2. ✅ Click **Storage** (or find Neon database)
3. ✅ Click on your Neon database
4. ✅ Find **Connection String** or **Connection URL**
5. ✅ Copy it
6. ✅ Go to **Settings** → **Environment Variables**
7. ✅ Add `POSTGRES_URL` = (paste connection string)
8. ✅ Save and redeploy

## After Adding Connection String

1. **Redeploy your app:**

   ```bash
   vercel --prod
   ```

2. **Pull environment variables locally:**

   ```bash
   vercel env pull .env.local
   ```

3. **Run migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Create superuser:**

   ```bash
   python manage.py createsuperuser
   ```

5. **Populate products:**
   ```bash
   python manage.py populate_products
   ```

## Troubleshooting

### Can't find connection string in Vercel?

- Try Method 2 (Neon Dashboard directly)
- Check if database is properly linked to Vercel project

### Connection string format wrong?

- Make sure it starts with `postgresql://`
- Include `?sslmode=require` at the end
- No spaces in the string

### Still having issues?

- Check Neon documentation: https://neon.tech/docs
- Verify database is active in Neon dashboard
- Make sure you're copying the entire string

## Need Help?

If you still can't find it:

1. Take a screenshot of your Neon dashboard
2. Check Vercel Storage section
3. Look for any "Connection" or "Settings" tabs

The connection string is usually prominently displayed - it's the main thing you need to connect to the database!


