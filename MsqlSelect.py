import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="restaurant"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT productname FROM items")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
