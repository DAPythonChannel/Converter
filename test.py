from Controller import Controller as ct

path = "D:\\софт\\Data\\ruRU\\Documentation"

list_path = ct.get_path_to_pdf_files(ct,path,False)
print(list_path)
ct.start(ct,list_path)