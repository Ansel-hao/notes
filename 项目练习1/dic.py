import re
import pymysql
db = pymysql.connect(host='localhost',port=3386,user='root',password='zjh666666',database='xml',charset='utf8')
cur = db.cursor()
sql = 'insert into zd(work,mens) values (%s,%s);'
with open('dict.txt','r+') as f:
    while True:
        s = f.readline()
        if s == "":
            break
        l = re.findall(r'(\w+)\s+(.*)',s)[0]
        try:
            cur.execute(sql,l)
            db.commit()
        except Exception:
            db.rollback()

cur.close()
db.close()