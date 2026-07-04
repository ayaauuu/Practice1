from connect import connect, create_table

create_table()

while True:

    print("""
1 Search
2 Add/Update
3 Show page
4 Delete
5 Exit
""")

    choice = input()

    conn = connect()
    cur = conn.cursor()

    if choice=="1":

        word=input("Search: ")

        cur.execute(
            "SELECT * FROM search_contact(%s)",
            (word,)
        )

        print(cur.fetchall())

    elif choice=="2":

        name=input("Username: ")
        phone=input("Phone: ")

        cur.execute(
            "CALL add_contact(%s,%s)",
            (name,phone)
        )

        conn.commit()

    elif choice=="3":

        cur.execute(
            "SELECT * FROM get_contacts(10,0)"
        )

        print(cur.fetchall())

    elif choice=="4":

        value=input("Username or phone: ")

        cur.execute(
            "CALL delete_contact(%s)",
            (value,)
        )

        conn.commit()

    elif choice=="5":

        cur.close()
        conn.close()
        break

    cur.close()
    conn.close()
