import psycopg2
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        with psycopg2.connect(**config) as conn:   #** распаковывает словарb,передаеt data как именованные аргументы функции
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)
    conn = psycopg2.connect(**config)