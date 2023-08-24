
### Description

**get_the_comp_conf** - Скрипт предназначен для сбора информации с удаленных хостов загруженных из файлов .csv. Скрипт может дополнятся, в зависимости от спекта необходимой информации для сбора.
Скрипт основан на библиотеке python - 'fabric3'
Весь конфиг расположен в файле fabfile.py.

### Installation
```
curl -sSL https://install.python-poetry.org | python3 -  (Для выполнения команды прописать настройки прокси, путем редактирования .bashrc)
sudo yum install git
git clone https://github.com/minoko86/get_the_comp_conf.git
cd get_the_comp_conf
make install
make build
make package-install
убрать настройки прокси
```

### Customization
```
0. Откройте на редактирование fabfile.py
1. Если не используете экспорт пароля из .env закомментируйте строку #9, раскомментируйте строку #10 и введите пароль в ''.
2. В строке #21 измените окончание файла 'kamges.csv' на Ваш.
3. Измените название функции в строке #51 на Ваши.
4. Замените csv-файлы проекта на Ваши.
```

### HELP
```
Для просмотра списка доступных команд используйте - 'fab --list'
```

### Use
```
Перейти в директорию где расположены файлы fabfile.py и .csv
Запустить скрипт командами указаными в HELP, добавляя перед командой 'fab'. 
Например:
"fab diskspace_kamges"
"fab diskspace_kamges > 1.txt" - записывает вывод команды в файл 1.txt находящейся в текущей директории.
```

### Examples
Вывод команды 'fab -list'

[![asciicast](https://asciinema.org/a/p0iHcPxwWEniEqBIHqWSMwsVC.svg)](https://asciinema.org/a/p0iHcPxwWEniEqBIHqWSMwsVC)