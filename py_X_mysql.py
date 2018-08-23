import pymysql

#Connect to mysql
db=pymysql.connect("localhost","root","123456")

#Create cursor object
cur=db.cursor()

#Create database
cur.execute('create database if not exists python;')

#Create tables
cur.execute('use python;')
cur.execute('create table if not exists t1 (\
			id int primary key,\
			name varchar(20),\
			score tinyint unsigned);')

#Insert recoreds into t1
cur.execute('insert into t1 values\
			(1,"Tom",88),\
			(2,"Jerry",100),\
			(3,"Jacky",80),\
			(4,"Luke",60),\
			(5,"Ken",99)')

#Commit
db.commit()
#Disconnect
cur.close()
db.close()
