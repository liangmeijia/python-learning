import pymysql
'''
利用 Python 连接 MySQL 数据库的方式：
1.mysql-connector-python
是官方推荐的 MySQL 连接器，支持更多高级功能
2.pymysql
是一个轻量级的第三方库，更加灵活，但某些功能可能需要手动实现
'''



def connect_to_mysql():
    try:
        # 建立连接
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            database='sql_tutorial'

        )
        print("成功连接到数据库")
        cursor = connection.cursor()
        # 执行查询
        cursor.execute("SELECT * FROM `student`;")
        records = cursor.fetchall()
        for row in records:
            print(row)
        # cursor.execute("INSERT INTO `student` (`name`,`major`,`score`) VALUES ('小哈哈', '化学',80);")
        # connection.commit()
        # print('插入数据成功')
    except pymysql.MySQLError as e:
        print("数据库连接失败:", e)
    finally:
        # 关闭连接
        if 'connection' in locals() and connection.open:
            cursor.close()
            connection.close()
            print("数据库连接已关闭")

# 调用函数
connect_to_mysql()
