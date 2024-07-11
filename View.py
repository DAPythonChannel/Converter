
'''Импорт Qt libs для формирования GUI и обработчиков событий'''
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMessageBox

import sys, os
'''Импорт основного контроллера и UI'''
import Controller, UI

class App(QtWidgets.QMainWindow, UI.Ui_MainWindow, Controller.Controller):
    
    def __init__(self) ->None:
        pass

    def browse_folder(self) ->None:
        '''Просмотр выбранной папки'''
        pass        

    def convert_start(self) ->None:
        '''Запускает конвертацию блокируя основной поток с учетом всех необходимых проверок
        Основной поток не нужен, т.к. в процессе работы к нему обращатся не будут'''
        pass
    
    def message_show(self, text: str, title: str, icon: str="Warning") ->None:
        '''Формирование сообщений пользователю'''
        pass
    
    def open_folder_pdf(self) -> None:
        '''Открывает папку где хранятся входные файлы программы (pdf)'''
        pass

    def open_folder_tiff(self) ->None:
        '''Открывает папку где хранятся выходные файлы программы (tiff)'''
        pass

    def version_show(self) ->None:
        '''Показывает версию через MessageBox'''
        pass

    def about_show(self) ->None:
        '''Показывает информацию о программе через MessageBox'''
        pass

def main():
    pass

if __name__ == '__main__':  
    main()  