import psycopg2
import sys


class db_conn():

   def db_connected(self):
      connected = psycopg2.connect(user="....",
                                   # пароль, который указали при установке PostgreSQL
                                   password="Q....",
                                   host="....",
                                   port="....")
      return connected

