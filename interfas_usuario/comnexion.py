import pickle
import mysql.connector

variable2 = pickle.load(open("variabledatos.dat", "rb"))


class DataBase:
    def __init__(self):
        self.miconexion = mysql.connector.connect(host=variable2, user="luis", passwd="luis1717", database="colegio",port = 3306)

        self.cursor = self.miconexion.cursor()
