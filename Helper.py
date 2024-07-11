#Windows command exec: 
#req.txt
'''
pdf2image==1.16.2
pillow==9.0.1
PyQt6==6.2.3
PyQt6-Qt6==6.2.3
PyQt6-sip==13.2.1
tqdm==4.49.0
colorama==0.4.4
'''

#Удаление библиотек из pip
'''
@echo on
python -m pip uninstall -y -r req.txt
pause
'''

#Скачивание библиотек с репозитория для использования в офлайн режиме
'''
@echo on
py -m pip download -r req.txt --only-binary :all: -d ./
'''

#Офлайн распоковка библиотек
'''
@echo on
py -m pip install --no-index --find-links="%~dp0\" -r req.txt
pause
'''