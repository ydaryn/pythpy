import psycopg2

def update_phone_number(user_id, new_phone_number):
    conn = psycopg2.connect(
        dbname="your_database_name",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cur = conn.cursor()
    
    cur.execute(
        "UPDATE PhoneBook SET phone_number = %s WHERE id = %s",
        (new_phone_number, user_id)
    )
    
    conn.commit()
    conn.close()

