import mysql.connector
import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'TM@chine123',
    'host': 'localhost',
    'database': 'people_mockdata',
}


def connectDB():
    try:
        cnx = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DV_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

    return cnx
