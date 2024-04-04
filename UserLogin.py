import psycopg2
import sys
from myDB import db_conn #мой класс для коннекта к БД

#класс для управления пользователями
class UserLogin():

   def getUser(self, user_id):
      try:
         query_str = (f'SELECT * FROM users WHERE id = {user_id} LIMIT 1')
         connected = db_conn().db_connected()
         cursor = connected.cursor()
         cursor.execute(query_str)
         res = cursor.fetchone()
         cursor.close()
         connected.close()
         if not res:
            print("Пользователь не найден")
            return False
         return res
      except psycopg2.Error as e:
         print("Ошибка получения данных из БД " + str(e))
      return False


   def fromDB(self, user_id):
      self.__user = self.getUser(user_id)
      return self


   def create(self, user):
      self.__user = user
      return self


   def is_authenticated(self):
      return True


   def is_active(self):
      return True


   def is_anonymous(self):
      return False


   def get_id(self):
      return str(self.__user[0])