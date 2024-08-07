
'''Импорт Qt libs для формирования GUI и обработчиков событий'''
from PyQt6 import QtWidgets
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import threading

import sys, os
'''Импорт основного контроллера и UI'''
import UI
from Controller import Controller
'''Пути к ресурсам'''
ICON = os.path.join(os.path.dirname(__file__), "Resources","icon.png")
ABOUT = os.path.join(os.path.dirname(__file__),"Resources","about.txt")
PATH_FILE_OUT = os.path.join(os.path.dirname(__file__),"out")

class App(QtWidgets.QMainWindow, UI.Ui_MainWindow, Controller):
    list_path=[]
    def __init__(self) ->None:
        super().__init__()    
        self.setWindowIcon(QIcon(ICON)) 
        self.setupUi(self)   
        '''Обработчики кнопок'''      
        self.pButtonPath.clicked.connect(self.browse_folder)
        self.pButtonStart.clicked.connect(self.thread_converting_files)    
        
        '''Обработчики меню'''
        self.menu_action_path.triggered.connect(self.browse_folder)    
        self.menu_action_start.triggered.connect(self.thread_converting_files)
        self.menu_action_pdf.triggered.connect(self.open_folder_pdf)    
        self.menu_action_tiff.triggered.connect(self.open_folder_tiff)
        self.menu_about.triggered.connect(self.about_show)    
        self.menu_version.triggered.connect(self.version_show)
        
    def browse_folder(self) ->None:
        '''Просмотр выбранной папки'''
        self.labelPath.clear()
        self.labelFound.clear()
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")
        if directory: 
            print("---------------------------Конвертер ООО 'Башнефть-Добыча'----------------------------") 
            self.list_path= self.get_path_to_pdf_files(directory, self.checkBoxRec.isChecked())
            text = f"Найдено: {len(self.list_path)} pdf-файлов"
            self.labelPath.setText(directory)
            self.labelFound.setText(text) 

    def thread_converting_files(self):
        th = threading.Thread(target=self.converting_files)
        th.start()
        th.join()
      
    def converting_files(self):
        '''Запускает конвертацию блокируя основной поток с учетом всех необходимых проверок
        Основной поток не нужен, т.к. в процессе работы к нему обращатся не будут'''
        path = self.labelPath.text()   
        if path:
            if os.path.exists(path):
                if self.list_path:
                    self.converting_fl(self.list_path)
                else: self.message_show(title="Ошибки в конвертации.",text="В папке pdf-файлы не найдены!")
            else: self.message_show(title="Ошибки в конвертации.",text="Папка не существует!")
        else: self.message_show(title="Ошибки в конвертации.",text="Не выбран путь к pdf-файлам!")
    
    def message_show(self, text: str, title: str, icon: str="Warning") ->None:
        '''Формирование сообщений пользователю'''
        msg = QMessageBox(self)         
        msg.setWindowTitle(title)
        msg.setText(text)
        if icon=="Warning":
            msg.setIcon(QMessageBox.Icon.Warning)
        elif icon=="Information":
            msg.setIcon(QMessageBox.Icon.Information)
        elif icon=="Question":
            msg.setIcon(QMessageBox.Icon.Question)
        elif icon=="Critical":
            msg.setIcon(QMessageBox.Icon.Critical)
        return msg.exec()
    
    def open_folder_pdf(self) -> None:
        '''Открывает папку где хранятся входные файлы программы (pdf)'''
        if self.labelPath.text():
            os.startfile(self.labelPath.text()) # Открывает папку где хранятся pdf
        else: self.message_show(title="Ошибка при открытии папки",text="Папка не существует!")

    def open_folder_tiff(self) ->None:
        '''Открывает папку где хранятся выходные файлы программы (tiff)'''
        if os.path.exists(PATH_FILE_OUT):
            os.startfile(PATH_FILE_OUT) # Открывает папку где хранятся tiff
        else: self.message_show(title="Ошибка при открытии папки",text="Папка не существует!")

    def version_show(self) ->None:
        '''Показывает версию через MessageBox'''
        self.message_show(title="Версия ПО 'Проект Конвертор'",text="Версия: beta 1.2",icon="Information")

    def about_show(self) ->None:
        '''Показывает информацию о программе через MessageBox'''
        os.startfile(ABOUT)
    
    def startfine(self) -> None:
        '''Открывает папку'''
        if os.name == "nt":
            os.startfile(PATH_FILE_OUT)
        else:
            os.system(f'open {r"./out"}')
def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = App()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    sys.exit(app.exec())  # и запускаем приложение

if __name__ == '__main__':  
    main()  