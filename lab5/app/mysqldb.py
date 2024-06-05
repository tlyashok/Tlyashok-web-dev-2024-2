import mysql.connector
from flask import g

DEBUG = True


class DBConnector:
    def __init__(self, app) -> None:
        self.app = app
        self.db_config = {
            'user': app.config['MYSQL_USER'],
            'password': app.config['MYSQL_PASSWORD'],
            'host': app.config['MYSQL_HOST'],
            'database': app.config['MYSQL_DATABASE'],
        }

        if DEBUG:
            self.drop_tables()
            self.create_tables()
            self.insert_test_data()
        else:
            self.create_tables()

        self.app.teardown_appcontext(self.close)

    def connect(self):
        if 'db' not in g or g.db.is_closed():
            g.db = mysql.connector.connect(**self.db_config)
        return g.db

    def close(self, e=None):
        db = g.pop('db', None)
        if db is not None:
            db.close()

    def drop_tables(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute('DROP TABLE IF EXISTS Users;')
            cursor.execute('DROP TABLE IF EXISTS Roles;')
            connection.commit()

    def insert_test_data(self):
        with self.connect() as connection:
            cursor = connection.cursor()
            cursor.execute("""
                INSERT INTO Roles (name, description)
                VALUES ('Администратор', ''), ('Пользователь', '')
            """)
            role_id = 1
            cursor.execute("""
                INSERT INTO Users (login, password, last_name, first_name,
                                middle_name, role_id)
                VALUES (%s, SHA2(%s, 256), %s, %s, %s, %s)
            """, ('user', 'user', 'Doe', 'John', 'Michael', role_id))
            connection.commit()

    def create_tables(self):
        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Roles (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    description TEXT
                )  ENGINE=INNODB;
            """)
            connection.commit()

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    login VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(256) NOT NULL,
                    last_name VARCHAR(50) NOT NULL,
                    first_name VARCHAR(50) NOT NULL,
                    middle_name VARCHAR(50),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    role_id INT,
                    FOREIGN KEY (role_id) REFERENCES Roles(id)
                ) ENGINE=INNODB;
            """)
            connection.commit()
