import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

MYSQL_USER = 'std_2585_lab4'
MYSQL_DATABASE = 'std_2585_lab4'
MYSQL_PASSWORD = '12345678'
MYSQL_HOST = 'std-mysql.ist.mospolytech.ru'
