@echo off
echo Activating virtual environment...
call venv\Scripts\activate.bat

echo.
echo Installing Django and dependencies...
python -m pip install -r requirements.txt

echo.
echo Creating database migrations...
python manage.py makemigrations

echo.
echo Applying migrations...
python manage.py migrate

echo.
echo Setup complete!
echo.
echo Next steps:
echo 1. Create a superuser: python manage.py createsuperuser
echo 2. Populate products (optional): python manage.py populate_products
echo 3. Run server: python manage.py runserver
echo.
pause

