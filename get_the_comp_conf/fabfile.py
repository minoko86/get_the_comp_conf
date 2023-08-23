import os 
import csv
from fabric.api import run, env, hosts, sudo
from fabric.api import *
from dotenv import load_dotenv, find_dotenv


load_dotenv()
env.password = os.getenv('password') # Закомментировать строку и использовать строку ниже, вставив актуальный пароль от УЗ
# env.password = 'пароль'
env.port = 22 
env.skip_bad_hosts = True

# Открытие CSV  и нормализация записи hosts
path = os.getcwd()
spisok_kamges = []
spisok_GRVKK = []
spisok_RGITS = []

for filename in os.listdir(path):
    if filename.endswith('kamges.csv'): #Окончание файла выгружаемого с Foreman, необходимо заменить на свое
        with open(filename, newline='', encoding='utf-8') as File:  
            reader = csv.reader(File)
            for row in reader:
                new_text = 'user@' + row[0]
                spisok_kamges.append(new_text)
                result_kamges = spisok_kamges[1:]
        KAMGES = result_kamges
        # print(result)
    if filename.endswith('GRVKK.csv'):
        with open(filename, newline='', encoding='utf-8') as File_GRVKK:  
            reader_GRVKK = csv.reader(File_GRVKK)
            for row in reader_GRVKK:
                new_text = 'user@' + row[0]
                spisok_GRVKK.append(new_text)
                result_GRVKK = spisok_GRVKK[1:]
        GRVKK = result_GRVKK
        # print(result)
    if filename.endswith('RGITS.csv'):
        with open(filename, newline='', encoding='utf-8') as File:  
            reader = csv.reader(File)
            for row in reader:
                pos = row[0]
                new_text = 'user@' + row[0]
                spisok_RGITS.append(new_text)
                result_RGITS = spisok_RGITS[1:]
        # print(result)
        RGITS = result_RGITS


# Функции просмотра свободного места
@hosts(KAMGES)
def diskspace_kamges(): #Можно поменять названия функции, например: diskspace_kvvges
    # run("df -h")
    run("df -h | awk ' /100%/{print $0}'")
    # sudo('du -h -c -d1 /tmp')
    sudo("du -h -c -d1 /tmp | awk '/[1-9][1-9]G\s/ {print $0}'")
    # sudo('du -h -c -d1 /tmp | tee /tmp/1.txt')
    # get('/tmp/1.txt')


@hosts(GRVKK)
def diskspace_gvvk():
    # run("df -h")
    run("df -h | awk ' /100%/{print $0}'")
    # sudo('du -h -c -d1 /tmp')
    sudo("du -h -c -d1 /tmp | awk '/[1-9][1-9]G\s/ {print $0}'")
    # sudo('du -h -c -d1 /tmp | tee /tmp/1.txt')
    # get('/tmp/1.txt')


@hosts(RGITS)
def diskspace_rgits():
    # run("df -h")
    run("df -h | awk ' /100%/{print $0}'")
    # sudo('du -h -c -d1 /tmp')
    sudo("du -h -c -d1 /tmp | awk '/[1-9][1-9]G\s/ {print $0}'")
    # sudo('du -h -c -d1 /tmp | tee /tmp/1.txt')
    # get('/tmp/1.txt')
