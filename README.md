# techmart 

# IM - Django setup

1. make virtual environment named env
2. turn on virtual environment
3. pip install -r requirements.txt
4. python manage.py migrate
5. python manage.py createsuperuser
6. python manage.py runserver

other prerequisites:
- run XAMPP and start APACHE and SQL
   - go to http://localhost/phpmyadmin/sql
- if updated models: 
    - python manage.py make migrations
    - python manage.py migrate
