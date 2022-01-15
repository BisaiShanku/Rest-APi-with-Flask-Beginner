import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "create table users (id int,username text,password text)"

cursor.execute(create_table)

user = (1,"shanku","shanku")

insert_query = "insert into users values(?,?,?)"

cursor.execute(insert_query,user)

connection.commit()

value =cursor.execute("select * from users")

for i in value:
    print(i)

connection.close()

print(value)