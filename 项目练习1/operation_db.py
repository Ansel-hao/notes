"""
dict项目用于处理数据
"""
import pymysql
import hashlib
import time

# 编写功能类 提供给服务端使用
class Database:
    def __init__(self, host='localhost',
                 port=3386,
                 user='root',
                 passwd='zjh666666',
                 database='xml',
                 charset='utf8'):
        self.host = host
        self.port = port
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
        self.connect_db()  # 连接数据库

    def connect_db(self):
        self.db = pymysql.connect(host=self.host,
                                  port=self.port,
                                  user=self.user,
                                  password=self.passwd,
                                  database=self.database,
                                  charset=self.charset)
    def create_cursor(self):
        self.cur = self.db.cursor()

    # 关闭数据库
    def close(self):
        self.cur.close()
        self.db.close()

    # 处理注册
    def register(self,name,passwd):
        sql = "select * from user where name='%s'"%name
        self.cur.execute(sql)
        r = self.cur.fetchone() # 如果查询到结果
        if r:
            return False
        hash = hashlib.md5((name+"haha").encode())
        hash.update(passwd.encode())
        sql = "insert into user (name,password) values (%s,%s);"


        try:
            self.cur.execute(sql,[name,hash.hexdigest()])
            self.db.commit()
        except Exception:
            self.db.rollback()
            return False
        return True

    # 处理登录
    def db_login_reg(self,name,passwd):
        sql = "select * from user where name='%s'" % name
        self.cur.execute(sql)
        r = self.cur.fetchone()  # 如果查询到结果
        if r:
            hash = hashlib.md5((name + "haha").encode())
            hash.update(passwd.encode())
            if r[2] == hash.hexdigest():
                return True
        else:
            return False

    # 插入历史记录
    def insert_history(self,name,word):
        tm = time.ctime()
        sql = "insert into hist (name,work,time) values (%s,%s,%s);"
        try:
            self.cur.execute(sql,[name,word,tm])
            self.db.commit()
        except Exception:
            self.db.rollback()

    # 查单词
    def query(self,word):
        sql = "select mens from zd where work = '%s'"%word
        self.cur.execute(sql)
        self.db.commit()
        r = self.cur.fetchone()
        if r:
            return r[0]

    # 历史记录
    def history(self,name):
        sql = "select name,work,time from hist where name='%s' order by id desc limit 10"%name
        self.cur.execute(sql)
        self.db.commit()
        return self.cur.fetchall()