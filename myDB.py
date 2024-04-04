import psycopg2
import sys


class db_conn():

   def db_connected(self):
      connected = psycopg2.connect(user="prokat54rf",
                                   # пароль, который указали при установке PostgreSQL
                                   password="QNPJw1i75zSE&u5A",
                                   host="pg3.sweb.ru",
                                   port="5432")
      return connected

