import mysql.connector


class DataBase:
    def __init__(self):
        self.miconexion = mysql.connector.connect(host="192.168.1.8", user="luis", passwd="luis1717", database="colegio",port = 3306)

        self.cursor = self.miconexion.cursor()
