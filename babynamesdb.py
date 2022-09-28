__author__ = "Seth Labadie"

# Import statements
import sqlite3

# Global variables
db_name = "baby_names.db"


def connect_to_db():
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor()
    print("Connected to DB.")
    return db_conn, db_cursor


def create_table(db_cursor):
    sql = "create table names (name text, gender text, modern integer, cuteness integer, family_connection text, teasability integer)"
    db_cursor.execute(sql)
    print("Created table.")


def drop_table(db_cursor):
    sql = "drop table if exists names"
    db_cursor.execute(sql)
    print("Dropped table.")


def insert_row(db_cursor):
    sql = "insert into names values (?, ?, ?, ?, ?, ?)"
    # name text, gender text, modern integer, cuteness integer, family_connection text, teasability integer
    # Ask the user for each value
    name = input("Enter the name (str): ")
    gender = input("Enter the gender (str): ")
    modern = int(input("Enter the modernity score, 1-10 (int): "))
    cuteness = int(input("Enter the cuteness score, 1-10 (int): "))
    family_connection = input(" Enter if there is a family connection for the name, Y/N (str): ")
    teasability = int(input("Enter the teasability score 1-10 (int): "))
    tuple_of_values = (name, gender, modern, cuteness, family_connection, teasability)
    db_cursor.execute(sql, tuple_of_values)
    print("Inserted row into table.")


def select_all(db_cursor): # select without WHERE clause
    sql = "select * from names"
    result_set = db_cursor.execute(sql)
    print("\nTable now has the following rows: ")
    for row in result_set:
        print(row)
    print()


def select_row(db_cursor): # select with WHERE clause
    sql = "select * from names where name = ?"
    name = input("Please enter the name (str) you want to search for: ")
    tuple_of_value = (name, )
    result_set = db_cursor.execute(sql, tuple_of_value)
    print("\nHere is the row you have selected: ")
    for row in result_set:
        print(row)


def update_row(db_cursor):
    sql = "update names set cuteness = ?, teasability = ? where name = ?"
    name = input("Enter the name (str) for the name you would like to update: ")
    cuteness = int(input("Enter the new cuteness (int) score: "))
    teasability = int(input("Enter the new teasability (int) score: "))
    tuple_of_values = (cuteness, teasability, name)
    db_cursor.execute(sql, tuple_of_values) # binding
    print("Row updated.")


def delete_row(db_cursor):
    sql = "delete names where name = ?"
    name = input("Enter the name (str) you want to delete: ")
    tuple_of_value = (name, )
    db_cursor.execute(sql, tuple_of_value)
    print("Row deleted.")


def display_menu(db_conn, db_cursor):
    while True:
        print("Menu:")
        print("Enter S to get started and create a new database")
        print("Enter C to create a new row")
        print("Enter R to retrieve data")
        print("Enter U to update a row")
        print("Enter D to delete a row")
        print("Enter Q to quit the program")
        choice = input("Enter your choice: ").upper()
        if choice == "S":
            drop_table(db_cursor)
            create_table(db_cursor)
        elif choice == "C":
            insert_row(db_cursor)
        elif choice == "R":
            select_row(db_cursor)
        elif choice == "U":
            update_row(db_cursor)
        elif choice == "D":
            delete_row(db_cursor)
        elif choice == "Q":
            print("Goodbye")
            break
        else:
            print("Invalid choice of", choice)
        # (after each menu action) - db commit
        db_conn.commit()
        # (after each menu action) - select_all - see what data is in the db
        select_all(db_cursor)


def main():
    db_conn, db_cursor = connect_to_db()
    display_menu(db_conn, db_cursor)
    db_conn.close()


main()

