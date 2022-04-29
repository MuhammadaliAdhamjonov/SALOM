import sqlite3

connect = sqlite3.connect("Mydatas.db")
cursor = connect.cursor()
cursor2 = connect.cursor()
cursor3 = connect.cursor()
cursor4 = connect.cursor()

quest = input("Nima haqida ma`lumot olmoqchimisiz").lower()

cursor.execute("""
CREATE TABLE IF NOT EXISTS shopping(
    name TEXT,
    last_name TEXT,
    old INTAGER
    
    
)
    
""")
cursor.execute("""
    INSERT INTO shoping VALUES
    ("Muhammadali", "Adhamjonov", 16),
    ("Azimjon", "Azimov", 16),
    ("Asadbek", "Abdumalikov", 16)

""")
cursor.execute("SELECT * FROM shopping")
result = cursor.fetchall()


