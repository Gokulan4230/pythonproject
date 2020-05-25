import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', password='dreamrocks', database='bgv_simservice')
mycursor = con.cursor()
sql = mycursor.execute('insert into totalcaptchacount (id, status, files, totalcaptchacount, ref_id) values (%i, %s, %s, '
                 '%i, %i)')
val = (423, "Highway 21", ' ', 23, 34567899754)
mycursor.execute(sql, val)
con.commit()

print(mycursor.rowcount, "record inserted.")
