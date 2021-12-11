# Django app for storing receipts from purchases

## Install
- If you downloaded sources: `pip install .`
- Or directly `pip install git+https://github.com/Guilouf/django-receipt.git`

## Plug in an existing project
- Put `'receipt'` and `'django_filters'` in your `INSTALLED_APPS`
- `python manage.py makemigrations receipt` and `python manage.py migrate receipt`

## Run in standalone
- Download sources and `pip install -r requirements.txt`
- `python manage.py makemigrations receipt` and `python manage.py migrate receipt`
- `python manage.py runseruver` in `project_receipt`
