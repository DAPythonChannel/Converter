from pdf2image import convert_from_path
from tqdm import tqdm
import os

PATH_TO_LIB=os.path.dirname(__file__)+r"\Library"

class Controller():

    def __init__(self):
        pass

    def start(self, list_path: list, path_file_out: str) ->None: 
        '''Запуск процесса конвертирования и вывод на экран вспомогательных сообщений.
        По завершению открывает папку с файлами.
        '''         
        print(f"Всего pdf-файлов: {len(list_path)}")     
        print("Логирование конвертации:\n")
        for i, path in enumerate(list_path,1):
            print(f"№{i} Конвертируется файл: {path}")
            self.converting(self,i, path, path_file_out) # запуск функции конвертация
            print(f'Конвертация файла завершена, создан следующий файл: out{i}.tiff')
            print("--------------------------------------------------------------------------------------")
        print("\nКонвертация завершена, после закрытия логирование будет удалено.") 
        os.startfile(path_file_out)
    
    def converting(self, index: int, path: str, path_file_out: str) -> None:        
        '''Запуск процесса ковертирования, на входе идентификатор списка и его путь,
        после превращает pdf в массив картинок, складывает все картинки в необходимый
        формат tiff, на выходе показывает прогресс бар и конвертированный файл.
        '''
        images = convert_from_path(path, fmt='jpeg', poppler_path=PATH_TO_LIB) 
        progress_bar = tqdm(images,desc="Прогресс конвертации:",total=len(images))
        for i in range(len(images)):
            images[0].save(f'{path_file_out}\out{index}.tiff',save_all=True,append_images=images[1:],compression='tiff_lzw') 
            progress_bar.update() 
        progress_bar.close()

    def get_path_to_pdf_files(self, path_in: str, is_recursive: bool) -> list:
        '''Получаем список всех pdf файлов по указанному пути: 
        1. Если рекурсия False -> исключаем все вложенные деректории и соответственной файлы
        2. Если рекурсия True  -> просматриваем все файлы и папки
        '''
        list = []
        print("Выбраны следующие файлы:")        
        for root, dirs, files in os.walk(path_in):
            if not is_recursive:
                while len(dirs) > 0:  
                    dirs.pop() 
            for file in files:
                if file.endswith('.PDF') or file.endswith('.pdf'):            
                    list.append(os.path.join(root,file))
                    print(os.path.join(root,file))
        if len(list) == 0: print("В папке отсутствуют файлы pdf.") 
        return list

    