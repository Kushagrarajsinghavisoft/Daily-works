import mysql.connector

dataBase= mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root"
)

cursorObject=dataBase.cursor()

cursorObject.execute("CREATE DATABASE students_data")

