import pymysql
db=pymysql.connect('localhost','root','123456','python')
cur=db.cursor()

#---------------------------------------------------------

SqlSelect = 'select * from t1 ;'
cur.execute(SqlSelect)
data=cur.fetchall()

for i in data:
	print((i))

#---------------------------------------------------------
db.commit()
cur.close()
db.close()