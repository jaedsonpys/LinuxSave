import os
import shutil
from datetime import datetime
from time import sleep
from utils.print_log import print_log

#
# Leia o README para entender algumas partes do código.
#
# MIT License
# Copyright (c) 2021 Jaedson Francisco da Silva 
# 
# @autor: Jaedson Silva
# @github: github.com/jaedsonpys 
# 


class BackupData:
    def __init__(self, schedule_backup: list, folders_to_backup: list, local_save_backup: str) -> None:
        '''
        Inicia o backup no horario definido.
        
        schedule_backup: Uma lista com os horarios definidos
        para realizar o backup.
        
        folders_to_backup: Lista de pastas que serão copiadas
        na hora do backup.
        
        local_save_backup: O local para onde todos os arquivos
        que foram copiados vão.
        '''

        self.schedule_backup = schedule_backup
        self.folders_to_backup = folders_to_backup
        self.local_save_backup = local_save_backup

        self.__last_backup = None
        self.__verify_schedule()
    
    def __verify_schedule(self) -> None:
        '''Faz verificações a cada 10 (dez) segundos
        para verificar se está na hora de realizar o backup.'''

        while True:
            print_log('Verificando horário...', 'loading')
            current_time = datetime.now().hour

            # Se a hora atual for igual a hora definida para backup e
            # o ultimo backup não for igual a hora atual, inicie. #
            if self.__last_backup != current_time:
                for hour in self.schedule_backup:
                    if hour == current_time:
                        self.__start_backup()
                        self.__last_backup = hour
            
            sleep(120)
            

    def __start_backup(self) -> bool:
        print_log('Preparando para fazer backup...', 'loading')

        # deletando os diretórios dentro de LinuxSave
        self.__delete_directories()

        for folder in self.folders_to_backup:
            # se a pasta padrão onde os subdiretorios são salvos
            # não existir, crie-o
            if os.path.isdir(f'{self.local_save_backup}/LinuxSave') is False:
                os.mkdir(f'{self.local_save_backup}/LinuxSave')
                print_log(f'Pasta "LinuxSave" criada com sucesso', 'sucess')
                
            # copiando diretorio para LinuxSave
            self.__copy_directory(folder)

        print_log('Backup finalizado', 'sucess')
        return True


    def __copy_directory(self, folder: str) -> None:
        root_directory = os.getenv('HOME')

        # copiando o diretorio
        print_log(f'Copiando pasta "{folder}"...', 'loading')

        directory_source = f'{root_directory}/{folder}'
        destination_directory = f'{self.local_save_backup}/LinuxSave/{folder}'

        try:
            shutil.copytree(directory_source, destination_directory)
        except shutil.Error as err:
            print_log(f'Ocorreu um erro ao copiar o diretório "{folder}": {err}', 'error')
            return
        else:
            print_log(f'Pasta "{folder}" copiada com sucesso', 'sucess')
    

    def __delete_directories(self) -> None:
        '''Deleta todos os diretórios salvos em LinuxSave para
        fazer a cópia dos novos diretórios.'''

        print_log('Deletando diretórios antigos...', 'loading')

        for f in self.folders_to_backup:
            directory = f'{self.local_save_backup}/LinuxSave/{f}'

            # se o diretório existir, delete-o
            if os.path.isdir(directory):
                shutil.rmtree(directory)


folders = ['Documentos', 'Downloads', 'Imagens', 'RepoOverKernel', 'smmc', 'OverNucle']
local_save_backup = '/media/jaedsonpys/Jaedson'
hours_backup = [13, 18, 22, 5]

BackupData(hours_backup, folders, local_save_backup)