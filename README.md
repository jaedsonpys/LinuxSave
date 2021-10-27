# LinuxSave - Backup automático

O LinuxSave é um programa onde você pode, de forma automática, realizar o backup de todos os seus
dados que forem selecionados.

### Conteúdos

* [Sobre](#Sobre)
    * [Como funciona](#Como-funciona)
* [Como usar](#Como-usar)
    * [Alterar pastas do backup](#Alterar-pastas-do-backup)
    * [Alterar local para o backup](#Alterar-local-para-o-backup)
    * [Mudando os horários](#Mudando-os-horários)
* [Tecnologias]()
* [Problemas]()
* [Licença]()

# Sobre

No código, é possível definir os horarios em que os backups serão realizados, podendo definir no minimo *um backup por hora*.

Você conseguirá definir quais diretórios vão fazer parte do backup e para onde eles vão, seja seu HDD externo ou um pendrive!

O objetivo desse projeto foi a solução para evitar a perda dos meus dados, já que meu HDD começou a apresentar problemas de leitura e corrompimento de dados, para isso, decidi criar um código que fizesse o backup dos meus dados.

## Como funciona

Ao definir os horários, que são colocados em uma lista, o código irá a cada um minuto, dentro de um loop *while*, **verificar se a hora atual** corresponde a algum horário definido pelo usuário. **Veja o exemplo**:

>     ...
>
>     horarios = [15, 18, 21]
>     hora_atual = datetime.now().hour
>
>     for h in horarios:
>         if h == hora_atual:
>             start_backup()

Assim, se a condição for verdadeira, o backup é iniciado.

### Pergunta

> Mas quando o loop voltar para o início, o backup não vai ser feito novamente? Entrando em um loop de backups?

### Resposta

Sim, para isso, usamos uma váriavel para armazenar a hora do último backup, para impedir esse loop. **Veja um exemplo** utilizando o mesmo pedaço de código, adicionando o que acabamos de falar:

>     ...
>
>     horarios = [15, 18, 21]
>     hora_atual = datetime.now().hour
>     ultimo_backup
>
>     for h in horarios:
>         if h == hora_atual and ultimo_backup != hora_atual:
>             start_backup()
>
>             # assim que o backup for finalizado, define
>             # a hora do ultimo backup:
>
>             utlimo_backup = hora_atual

Agora, o próximo backup só vai ocorrer quando a hora atual for diferente do horário em que
o último backup foi realizado.

*Este foi apenas um exemplo de como o código funciona

# Como usar

Aqui você aprenderá a configurar o LinuxSave.

## Alterar pastas do backup

Neste pedaço de código você pode escolher quais pastas vão fazer parte do backup. Lembre-se que, o caminho raíz é
**/home/usuario**, então se quiser fazer backup da pasta Documentos, basta fazer adicionar o nome dela na lista que está no final do arquivo **main.py**:

>       ...
>       folders = ['Documentos']
>       BackupData(hours_backup, folders, local_save_backup)

Se quiser fazer o backup de uma pasta que está dentro de Documentos, adicione o caminho:

>       folders = ['Documentos/FotosDaFamilia']

*Ainda não é possível fazer backup de arquivos, apenas pastas.

## Alterar local para o backup

Este é o local onde o backup vai ser salvo, ou seja, para onde os arquivos vão, pode ser seu HDD, pendrive, ou outra pasta no próprio computador:

>       ...
>       # Aqui, escolhemos uma pasta do próprio computador
>       # para salvar nossos backup:
>
>       local_save_backup = '/home/jaedsonpys/MeusBackups'
>
>       BackupData(hours_backup, folders, local_save_backup)

Caso queria salvar seu backup em uma mídia removível, veja onde sua mídia está montada e adicione o local a váriavel **local_save_backup**, o local pode ser parecido com isso:

>       ...
>       local_save_backup = '/media/<nome_da_usuario>/<nome_da_midia>'

## Mudando os horários

Para alterar os horários de backup, basta adicionar a hora na lista que está no final do código em **main.py**, veja um exemplo:

>       ...
>       # Aqui você define os horários, no minimo o intervalo é de uma hora.
>       hours_backup = [13, 14, 15, 23]
>
>       BackupData(hours_backup, folders, local_save_backup)

Quando o sistema encontrar algum desses horários, ele irá começar o backup automaticamente.