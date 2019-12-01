### currency-converter

To run:

```
git clone https://github.com/deniskolosov/currency-converter.git
cd currency-converter
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
and go to 127.0.0.1/admin to set up the scheduler task.

#### Run tests:
```
./manage.py test
```
