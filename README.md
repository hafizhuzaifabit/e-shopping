# ShopSmart - E-commerce Dashboard

A dynamic e-commerce dashboard built with Django featuring product management, shopping cart, user profiles, and more.

## Features

✅ **Base Template & Includes**

- Reusable `base.html` template with header and footer includes
- Header with site name "ShopSmart" and navigation links
- Footer with dynamic year and total product count using custom template tag

✅ **Home Page**

- Welcome message with authentication check
- Conditional display based on user authentication status

✅ **Products Page**

- Grid layout displaying all products
- Product details: Name, Price, Stock Status
- Stock status indicators (In Stock, Low Stock, Out of Stock)
- Search functionality
- Pagination (9 products per page)

✅ **Cart Page**

- Display cart items
- Dynamic total price calculation
- Add/Remove items functionality

✅ **Profile Page**

- User details display
- Template inheritance from base.html

✅ **Additional Features**

- Custom price formatting filter (e.g., 1,200.00)
- Custom template tag for total product count
- Reusable product card template using {% include %}
- Django pagination
- Search bar in header for filtering products

## Setup Instructions

### ⚡ Quick Setup (Windows - Easiest Method)

**Just double-click `setup.bat`** - It will automatically:

- Activate the virtual environment
- Install Django and all dependencies
- Create database migrations
- Set up the database

Then run the server by double-clicking `run_server.bat`

### 📝 Manual Setup (Step by Step)

**IMPORTANT: You must activate the virtual environment first!**

1. **Activate Virtual Environment (Windows PowerShell)**

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   Or if that doesn't work, use Command Prompt:

   ```cmd
   venv\Scripts\activate.bat
   ```

   You should see `(venv)` in your prompt when activated.

2. **Install Dependencies**

   ```cmd
   pip install -r requirements.txt
   ```

   This installs Django and boto3.

3. **Run Migrations**

   ```cmd
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create Superuser (for admin access)**

   ```cmd
   python manage.py createsuperuser
   ```

   Follow the prompts to create your admin account.

5. **Populate Sample Products (Optional)**

   ```cmd
   python manage.py populate_products
   ```

6. **Run Development Server**

   ```cmd
   python manage.py runserver
   ```

7. **Access the Application**
   - Main site: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## Project Structure

```
E-comerce/
├── ecommerce/          # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── shop/               # Main app
│   ├── models.py      # Product and CartItem models
│   ├── views.py       # All views (home, products, cart, profile)
│   ├── urls.py        # URL routing
│   ├── admin.py       # Admin configuration
│   ├── templatetags/  # Custom template tags and filters
│   └── templates/     # HTML templates
│       └── shop/
│           ├── base.html
│           ├── home.html
│           ├── products.html
│           ├── cart.html
│           ├── profile.html
│           └── includes/
│               ├── header.html
│               ├── footer.html
│               └── product_card.html
├── static/            # Static files
│   └── css/
│       └── style.css
└── manage.py
```

## Usage

1. **View Products**: Navigate to `/products/` to see all available products
2. **Search**: Use the search bar in the header to filter products
3. **Add to Cart**: Click "Add to Cart" on any product (requires login)
4. **View Cart**: Navigate to `/cart/` to see your cart items and total
5. **Profile**: View your profile at `/profile/` (requires login)

## Custom Template Tags & Filters

- `{% total_products %}`: Returns the total number of products
- `{{ price|format_price }}`: Formats price with thousand separators (e.g., 1,200.00)

## Admin Panel

Access the admin panel to:

- Add/Edit/Delete products
- View cart items
- Manage users

Login at: http://127.0.0.1:8000/admin/
