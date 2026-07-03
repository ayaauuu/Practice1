from connect import conn, cursor

while True:

    print("1.Search")
    print("2.Add")
    print("3.Show")
    print("4.Delete")
    print("5.Exit")

    choice = input()

    if choice == "1":

        text = input("Search: ")

        cursor.execute(
            "SELECT * FROM search_contact(%s)",
            (text,)
        )

        print(cursor.fetchall())

    elif choice == "2":

        name = input("Name: ")
        phone = input("Phone: ")

        cursor.execute(
            "CALL add_contact(%s,%s)",
            (name, phone)
        )

        conn.commit()

    elif choice == "3":

        cursor.execute(
            "SELECT * FROM get_contacts(10,0)"
        )

        print(cursor.fetchall())

    elif choice == "4":

        value = input("Name or phone: ")

        cursor.execute(
            "CALL delete_contact(%s)",
            (value,)
        )

        conn.commit()

    elif choice == "5":
        break

cursor.close()
conn.close()
