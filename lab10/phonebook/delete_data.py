import psycopg2

def delete_by_phone_number(phone_number):
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()
    
    cur.execute(
        "DELETE FROM PhoneBook WHERE phone_number = %s",
        (phone_number,)
    )
    
    conn.commit()
    conn.close()
