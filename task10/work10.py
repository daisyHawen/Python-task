#coding:utf-8
__author__ = 'Administrator'

#域名服务，该服务器负责维护一个由主机名和端口号组成的数据库。
# 提供域名注册服务，域名查询服务。数据库采用mysql。
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost","root","123456","test" )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
def create(cursor):
# 如果数据表已经存在使用 execute() 方法删除表。
     cursor.execute("DROP TABLE IF EXISTS DOMAIN")
# 创建数据表SQL语句
     sql = """CREATE TABLE DOMAIN (
         HOSTNAME  CHAR(20) NOT NULL,
         HOSTPORT  CHAR(20) )"""
     cursor.execute(sql)
def insert(cursor):
    # SQL 插入语句
    sql1 = """INSERT INTO DOMAIN(HOSTNAME,HOSTPORT)
         VALUES ('www.uestc.edu.cn', '222.192.186.50')"""
    sql2 = """INSERT INTO DOMAIN(HOSTNAME,HOSTPORT)
         VALUES ('www.baidu.com', '180.149.155.40')"""
    # sql = """INSERT INTO DOMAIN(HOSTNAME,HOSTPORT)
    #      VALUES ('www.qq.com', '58.205.220.36')"""
    try:
   # 执行sql语句
        cursor.execute(sql1)
        cursor.execute(sql2)
   # 提交到数据库执行
        db.commit()
    except:
          # Rollback in case there is any error
        db.rollback()
def select(cursor,hostname):
    sql = "SELECT * FROM DOMAIN \
       WHERE HOSTNAME > '%d'" % (1000)
    try:
   # 执行SQL语句
       cursor.execute(sql)
   # 获取所有记录列表
       results = cursor.fetchall()
       for row in results:
          if row[0]==hostname:
             port = row[1]
             print "name=%s,port=%s" % (hostname,port)
    except:
       print "Error: unable to fecth data"

def test(cursor):
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print "Database version : %s " % data
#create(cursor)
#insert(cursor)
select(cursor,"www.baidu.com")

# 关闭数据库连接
db.close()