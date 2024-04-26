import psycopg2

def query_by_name(first_name):
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()
    
    cur.execute(
        "SELECT * FROM PhoneBook WHERE first_name = %s",
        (first_name,)
    )
    
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    conn.close()
