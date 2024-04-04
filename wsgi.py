# -*- coding: utf-8 -*-
import os,sys

#путь к проекту
sys.path.append('/home/p/...../public_html')
#путь к фреймворку
sys.path.append('/home/p/....')
#путь к виртуальному окружению
sys.path.append('/home/p/..../.flaskvenv/lib/python3.8/site-packages/')
#исключить системную директорию
#sys.path.remove('/usr/lib/python3.8/site-packages')

from app import app
application = app
