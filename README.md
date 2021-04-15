# Church members management

Simple app to track church members


### Dependencies

- Python 3.9


### Virtual environment

Create virtualenv:

```
python3.9 -m venv venv
```

Activate virtualenv:
```
source venv/bin/activate
```


### Installing app dependencies

```
pip install -r requirements.txt
```


### Run an interactive shell

```
python manage.py shell_plus
```


### Database migrations

Generate migrations when the Models are changed:
```
python manage.py makemigrations
```

Apply database migrations:
```
python manage.py migrate
```


### Import church members from CSV

Run the following command to import:

```
python manage.py import_members path/to/csv/file
```

The CSV needs to have the following columns:

```
id, name, phone, mobile_phone, address, baptize_date, birth_date, note
```


### Create user to access admin panel

```
python manage.py createsuperuser
```


### Start development server

```
python manage.py runserver
```


### Running the app

1. Create virtual environment
2. Apply migrations
3. Import church members from CSV (*optional*)
4. Create superuser
5. Access admin panel - http://localhost:8000/admin


### Print the birthdays of all Church members

1. Open the interactive shell

    ```
    python manage.py shell_plus
    ```

2. Call the following function:

    ```
    from church_list.members.actions import print_birthdays
    print_birthdays()
    print_birthdays(2020)
    ```
