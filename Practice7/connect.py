import psycopg2
import config


def connect():
    return psycopg2.connect(
        host=config.host,
        database=config.database,
        user=config.user,
        password=config.password,
        port=config.port
    )


def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS phonebook(
        id SERIAL PRIMARY KEY,
        username VARCHAR(50),
        phone VARCHAR(20)
    );
    """)

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    create_table()
    print("Table created successfully!")
