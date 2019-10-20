import psycopg2

con = psycopg2.connect(
    database = "test",
    user = "test",
    password = "test",
    host = "127.0.0.1",
    port = "5432"
)

print("Success")

cur = con.cursor()

# cur.execute('''CREATE TABLE STUDENT
#     (ADMISSION INT PRIMARY KEY NOT NULL,
#     NAME TEXT NOT NULL,
#     AGE INT NOT NULL,
#     COURSE CHAR(50),
#     DEPARTMENT CHAR(50));''')

# cur.execute(
#     "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420,'John','18','Computer science','ICT')"
# )
# cur.execute(
#   "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')"
# )
# cur.execute(
#   "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')"
# )
# cur.execute(
#   "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')"
# )

# print('Table create successfully')

# con.commit()
# print('Recorded successfully')


cur.execute("DELETE from STUDENT where ADMISSION=3420;")
con.commit()
print("Total deleted rows:", cur.rowcount)

cur.execute("SELECT ADMISSION, NAME, AGE, COURSE, DEPARTMENT from STUDENT")

rows = cur.fetchall()
for row in rows:
    print("ADMISSION=", row[0])
    print("NAME=", row[1])
    print("AGE", row[2])
    print("COURSE=", row[3])
    print("DEPARTMENT=", row[4],"\n")

print("Operation successfully")
con.close()
