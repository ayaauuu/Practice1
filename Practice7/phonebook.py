import csv
from connect import connect, create_table

create_table()


def insert_csv():
    conn = connect()
    cur = conn.cursor()

    with open("contacts.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            cur.execute(
                "INSERT INTO phonebook(username, phone) VALUES(%s,%s)",
                (row["username"], row["phone"])
            )

    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported!")


def insert_console():
    conn = connect()
    cur = conn.cursor()

    username = input("Name: ")
    phone = input("Phone: ")

    cur.execute(
        "INSERT INTO phonebook(username, phone) VALUES(%s,%s)",
        (username, phone)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added!")


def show_all():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook")

    rows = cur.fetchall()

    print("\nCONTACTS\n")

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_name():
    conn = connect()
    cur = conn.cursor()

    name = input("Enter name: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE username=%s",
        (name,)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_prefix():
    conn = connect()
    cur = conn.cursor()

    prefix = input("Phone prefix: ")

    cur.execute(
        "SELECT * FROM phonebook WHERE phone LIKE %s",
        (prefix + "%",)
    )

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def update_name():
    conn = connect()
    cur = conn.cursor()

    old = input("Old name: ")
    new = input("New name: ")

    cur.execute(
        "UPDATE phonebook SET username=%s WHERE username=%s",
        (new, old)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Updated!")


def update_phone():
    conn = connect()
    cur = conn.cursor()

    name = input("Username: ")
    phone = input("New phone: ")

    cur.execute(
        "UPDATE phonebook SET phone=%s WHERE username=%s",
        (phone, name)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Updated!")


def delete_name():
    conn = connect()
    cur = conn.cursor()

    name = input("Delete username: ")

    cur.execute(
        "DELETE FROM phonebook WHERE username=%s",
        (name,)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")


def delete_phone():
    conn = connect()
    cur = conn.cursor()

    phone = input("Delete phone: ")

    cur.execute(
        "DELETE FROM phonebook WHERE phone=%s",
        (phone,)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Deleted!")


while True:

    print("\n========== PHONEBOOK ==========")
    print("1 - Import contacts from CSV")
    print("2 - Add contact")
    print("3 - Show all contacts")
    print("4 - Search by name")
    print("5 - Search by phone prefix")
    print("6 - Update name")
    print("7 - Update phone")
    print("8 - Delete by name")
    print("9 - Delete by phone")
    print("0 - Exit")

    choice = input("Choose: ")

    if choice == "1":
        insert_csv()

    elif choice == "2":
        insert_console()

    elif choice == "3":
        show_all()

    elif choice == "4":
        search_name()

    elif choice == "5":
        search_prefix()

    elif choice == "6":
        update_name()

    elif choice == "7":
        update_phone()

    elif choice == "8":
        delete_name()

    elif choice == "9":
        delete_phone()

    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Wrong choice!")
