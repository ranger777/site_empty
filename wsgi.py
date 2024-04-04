# -*- coding: utf-8 -*-
import os,sys

#путь к проекту
sys.path.append('/home/p/prokat54rf/public_html')
#путь к фреймворку
sys.path.append('/home/p/prokat54rf')
#путь к виртуальному окружению
sys.path.append('/home/p/prokat54rf/.flaskvenv/lib/python3.8/site-packages/')
#исключить системную директорию
#sys.path.remove('/usr/lib/python3.8/site-packages')

from app import app
application = app