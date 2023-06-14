import sqlite3

conn=sqlite3.connect('patient.db')

cur=conn.cursor()

cur.execute("CREATE TABLE PATIENTINFO(NAME VARCHAR(40),RESULT VARCHAR (20))")

cur.execute("INSERT INTO PATIENTINFO VALUES ('Ramu','Diabetics')")
cur.execute("INSERT INTO PATIENTINFO VALUES ('Raju','No diabetic')")
cur.execute("INSERT INTO PATIENTINFO VALUES ('sharan','Diabetic')")

conn.commit()
