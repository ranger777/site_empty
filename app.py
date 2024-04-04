from flask import Flask, render_template, url_for, request, redirect, flash, session
import psycopg2
from  werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from UserLogin import UserLogin #наш класс для упаравления пользователями
import sys
from myDB import db_conn #наш класс для подключения к БД

#sys.stderr.write(f'vivod v load_user peredali = {user_id}\n') #для вывода в еррол-лог

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hgszxkjylydmdsfjxzxcbvdfzhbnxdmgfdsjx'#ключ для шифрования

login_manager = LoginManager(app)
login_manager.login_view = '/вход'#перенаправляет на страницу логин если не авторизованный пользователь попапл на закрытую страницу
login_manager.login_message = "Для просмотра данной страницы необходимо авторизоваться"# сообщение для неавторизованного пользователя
login_manager.login_message_category = "error" #категория сообщения выше

@login_manager.user_loader
def load_user(user_id):
   return UserLogin().fromDB(user_id)


@app.route("/")
def index():
   url_for_adm = url_for('index')
   return render_template("index1.html", url_for_adm=url_for_adm[9:])


@app.route("/админка")
@login_required #декоратор для закрытия страницы от неавторизованных пользователей
def adminka():
   query_str = (f'SELECT * FROM users')
   connected = db_conn().db_connected()
   cursor = connected.cursor()
   try:
      cursor.execute(query_str)
      users = cursor.fetchall()
   except:
      users = ()
   cursor.close()
   connected.close()
   return render_template("adminka.html", users=users, hash=hash)


@app.route("/админка/акции")
@login_required
def promotion():
   return "<h1>Акции, скидки, промоушен</h1>"


@app.route("/админка/оборудование")
@login_required
def tools():
   return "<h1>Все оборудование, добавление и редактирование</h1>"


@app.route("/вход", methods=['POST', 'GET'])
def login():
   if current_user.is_authenticated:# если пользователь уже авторизован, то
      return redirect(url_for('adminka')[9:])# отправим его на админку
   if request.method == "POST":
      name = request.form['name']
      query_str = (f'SELECT * FROM users WHERE name = \'{name}\'')
      connected = db_conn().db_connected()
      cursor = connected.cursor()
      cursor.execute(query_str)
      user = cursor.fetchone()
      cursor.close()
      connected.close()
      if user and check_password_hash(user[3], request.form['psw']):#если логин совпадает с бд и хеш паролей совпадают, то
         userlogin = UserLogin().create(user)#запишем пользователя в сессию
         rm = True if request.form.get("remainme") else False#если галочка "запомнить меня" включена, то поднимем флаг неразлогиниваться
         login_user(userlogin, remember=rm)#и запишем все в сессию
         if request.args.get("next"):#если в ссылке, откуда попали на логин, есть адрес, то
            return redirect(request.args.get("next")[9:])#вернемся на этот адрес
         else:
            return redirect(url_for('adminka')[9:])# если адреса нет, то переходим в админку

      flash("Неверный логин или пароль", "error")
   return render_template("login.html")


@app.route("/выход")
@login_required
def logout():
   logout_user()#передаем пустые данные в сессию, ткм самым заменяем все данные на "пусто"
   flash("Вы разлогинились", "success")
   return redirect(url_for('login')[9:])


@app.errorhandler(404)#декоратор обрабатывает случай если попадем на несуцествующую страницу
def pageNotFount(error):
   return render_template('page404.html')



if __name__ == "__main__":
   app.run(host='0.0.0.0')
