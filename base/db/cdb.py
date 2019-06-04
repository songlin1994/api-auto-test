import pymysql

# 创建连接
conn = pymysql.connect(host='192.168.1.137', port=3306, user='root', passwd='root', db='mall')

# 创建游标
cursor = conn.cursor()

cursor.execute("select id,order_sn,create_time from oms_order")
row_1 = cursor.fetchone()
print(row_1)

row_3 = cursor.fetchmany(3)
print(row_3)
