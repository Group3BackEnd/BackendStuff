
import MySQLdb
def connection():
	conn = MySQLdb.connect(host="localhost",
				user="root",
				passwd="*******",
				db="wordlocation")
	c = conn.cursor()
	return c,conn

