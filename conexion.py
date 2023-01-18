# Login  verificacion de datos
# @autor: Magno Efren
# Youtube: https://www.youtube.com/c/MagnoEfren

import mysql.connector


class Registro_datos():

    def __init__(self):
        self.conexion = mysql.connector.connect(host='192.168.1.8',
                                                user='luis',
                                                password='luis1717',
                                                database='colegio',
                                                port=3306)

    def busca_users(self, users):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuario WHERE nombre_user = {}".format(users)
        print(sql)
        cur.execute(sql)
        usersx = cur.fetchall()
        cur.close()
        return usersx

    def busca_password(self, password):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuario WHERE pass_user = {}".format(password)  #
        print(sql)
        cur.execute(sql)
        passwordx = cur.fetchall()
        cur.close()
        return passwordx
