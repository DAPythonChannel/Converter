<h1 align="center"># Converter </h1>
<h1 align="center">Language:RU </h1>
<h2>Вид программы:</h2>
<div align="center">
<image style="margin-left: auto; margin-right: auto; width: 50%;" src="Resources/form.png" alt="View software in MacOS">
<image style="margin-left: auto; margin-right: auto; width: 50%;" src="Resources/form_windows.png" alt="View software in Windows">
</div>
<h2>Описание ПО:</h2>
<p>Программное обеспечение предназначено для конвертации файлов pdf в файлы tiff. ПО выполняет обход (рекрусивный или простой) по указанной папке и делает поиск всех pdf файлов, выводит все файлы списком. По завершению поиска выполняет конвертацию и открывает путь к файлу.
</p>

<h2>Выбор технологий:</h2>
<p>Python3, pillow, pdf2image, PyQt6, tqdm, colorama, Qt Designer, poppler, pip, conda.</p>

<h2>Установка и запуск:</h2>
<p>Устанавливаем 
<a href="https://www.python.org/downloads/release/python-3913/">Python 3.9</a> c официального сайта.</p> 

<p>Устанавливаем нужные библиотеки следующей командой:</p>
<p><code>pip install -r req.txt или pip3.9 install -r req.txt</code></p>
<p>Windows:<p>
<p><code>conda install -c conda-forge poppler</code></p>
<p>или используйте архив Library с указанием пути к нему.</p>

<p>MacOS:</p>
<p><code>brew install poppler</code></p>

<p>Запускаем ПО:</p>
<p><code>python Run.py или python3.9 Run.py</code></p>

<p>Дополнительное описание ПО:</p>
<p><ul>
<li>Один файл pdf = один файл tiff.</li>
<li>Файл при конвертации сжимается.</li>
<li>Максимальное число страниц при конвертации не должно достигать 100 страниц.</li>
<li>Ограничитель по странице отсутствует.</li>
<li>Файл tiff будет больше чем исходный файл, это нормально.</li>
</ul>
</p>

<h2>Проблемы требующие решения:</h2>
<ul>
<li>Разные способы установки библиотек, требуется оптимизация скриптами.</li></ul>