import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='Zc.1319119251',
    charset='utf8',
    database='metadata'
)
cursor = conn.cursor()
cursor.execute('show tables')
results = cursor.fetchall()
print(results)
if ('test',) in results:
    print(True)
