from pdf2image import convert_from_path
from tqdm import tqdm
import os

'''Путь к папкам: результат и библиотека'''
PATH_TO_LIB=os.path.dirname(__file__)+r"\Library"
PATH_FILE_OUT = os.path.dirname(__file__)+r"\Out"

class Controller():

    def __init__(self):
        pass

    def start(self, list_path: list) ->None: 
        '''Запуск процесса конвертирования и вывод на экран вспомогательных сообщений.
        По завершению открывает папку с файлами.
        '''         
        pass
        

    def get_PATH_FILE_OUT(self):
        return PATH_FILE_OUT
    
    def converting(self, index: int, path: str) -> None:        
        '''Запуск процесса ковертирования, на входе идентификатор списка и его путь,
        после превращает pdf в массив картинок, складывает все картинки в необходимый
        формат tiff, на выходе показывает прогресс бар и конвертированный файл.
        '''
        pass

    def get_path_to_pdf_files(self, path_in: str, is_recursive: bool) -> list:
        '''Получаем список всех pdf файлов по указанному пути: 
        1. Если рекурсия False -> исключаем все вложенные деректории и соответственной файлы
        2. Если рекурсия True  -> просматриваем все файлы и папки
        '''
        pass

    