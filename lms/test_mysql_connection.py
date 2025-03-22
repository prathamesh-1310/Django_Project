import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="12345",
        db="library_db"
    )
    print("Connected to MySQL successfully!")
    db.close()
except Exception as e:
    print("Error connecting to MySQL:", e)
