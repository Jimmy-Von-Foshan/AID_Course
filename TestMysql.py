from ClassForMysql import MysqlPython

#update
name = input("Input the name of the student: ")
score= int(input ("Input the score of the student: "))
sql= "update t1 set score ='%s' where name = '%s'"\
	%(score,name)

sqlH = MysqlPython("localhost",3306,"python",\
	 "root",'123456')

sqlH.execute(sql)
