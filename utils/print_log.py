# Um print personalizado acompanhado de uma
# mensagem.
#
# MIT License
# Copyright (c) 2021 Jaedson Francisco da Silva 
# 
# @autor: Jaedson Silva
# @github: github.com/jaedsonpys 
# 

from datetime import datetime

def print_log(message: str, type_message: str):
    current_hour = datetime.utcnow()

    if type_message == 'sucess':
        print(f'[\033[32msucess\033[m][{current_hour}] {message}')
    elif type_message == 'loading':
        print(f'[\033[34mloading\033[m][{current_hour}] {message}')
    elif type_message == 'error':
        print(f'[\033[31merror\033[m][{current_hour}] {message}')
    else:
        print(f'[{type_message}] {message}')