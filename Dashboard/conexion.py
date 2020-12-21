import pymysql.cursors


def getConnection():
    connection = pymysql.connect(host='localhost',
                                 port=8889,
                                 user='root',
                                 password='root',
                                 db='Soccer',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    return connection.cursor(), connection
