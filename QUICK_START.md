# Quick Start Guide - Windows

## The Problem

The commands are slow or not working because Django isn't installed yet.

## Solution: Install Django First

### Step 1: Open PowerShell or Command Prompt in this folder

### Step 2: Install Django (Choose ONE method)

**Method A: Using system Python (if venv has issues)**

```cmd
python -m pip install Django==5.0.1
```

**Method B: Recreate virtual environment (Recommended)**

```cmd
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: After Django is installed, run these commands:

```cmd
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_products
python manage.py runserver
```

## Troubleshooting

**If "python" command not found:**

- Try `py` instead of `python`
- Or `python3` instead of `python`

**If virtual environment has path issues:**

- Delete the `venv` folder
- Run: `python -m venv venv`
- Then activate it and install packages

**If pip is slow:**

- Use: `pip install --upgrade pip` first
- Then: `pip install Django==5.0.1`

## After Installation

Once Django is installed, all the `manage.py` commands will work instantly!
