""" 
hangman.py
Last updated on April 3, 2021
 """
import requests
import os
import time
import random
import copy
from dictionary import *
from UI import *
Da = open('dictionary.py', 'r')
read = Da.read()
Da.close()
print('Hi')
version = 0.2
named_tuple = time.localtime()  # get struct_time
time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
print('Time started: ' + time_string)
print('Welcome to the Hangman game by 56\n Game version: {}'.format(version))
database = ['dog', 'cat', 'egg', 'chicken', 'hen']


def menu():  # head to the selected menu function
    UI_menu_table()
    table = input('Decision:')
    if 'a' in table:
        print('welcome admin')
        admin()
    elif 'c' in table:
        print('welcome editor')
        # config()
    elif 'p' in table:
        print('welcome player')
        player()
    elif 'e' in table:
        UI_exit_button(True)
        print('Process ending')
        exit()
    else:
        print('INVALID value')


def admin():
    global database
    call = input('Call in database?:').lower()
    call_txt = call.find('y')
    if call_txt >= 0:
        print('calling database...')
        print(database)
    else:
        print('Failed to call database.')


def admin_database_editor():
    print('Mode selected: database editor.')
    print('This function is not available yet.' ' Waiting for major update.')

    #  with open("dictionary.py") as D:
    #   'D.seek(0)'
    #   'counting = 0'
    #   'newlast = 0'
    #   "for line in range(2):"
    # 'look = read.find("D_")'
    #   'last = read.find("]", newlast)'
    #    'newlast = copy.deepcopy(last)'
    #    'print("copy: ", newlast)'
    #     'print(last)'
    #    'print(D.readline(last))'

    # looking = True
    # while looking is True:
    #   locate = read.find('D_', 0)
    #    counting += 1


def player():
    print('Mode selected: player')
    index = int(input('index value:'))
    print(database[index])
    print(len(database[index]))
    UI_underline(len(database[index]))


while True:
    menu()
