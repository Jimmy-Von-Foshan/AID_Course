from pymysql import *

class MysqlPython:
	def __init__(self,host,port,db,user,passwd):
		self.host =host
		self.port =port
		self.db=db
		self.user=user 
		self.passwd=passwd

	def open(self):
		self.con = connect(host=self.host,port=self.port,db=self.db,\
			user=self.user, passwd=self.passwd)
		self.cursor=self.con.cursor()

	def close(self):
		self.cursor.close()
		self.con.close()

	def execute(self,sql):
		self.open()
		self.cursor.execute(sql)
		self.con.commit()
		self.close()

	def all(self,sql):
		try:
			self.open()
			self.cursor.execute(sql)
			data=self.cursor.fetchall()
			self.close()

			return data
		except Exception as e:
			print(e)