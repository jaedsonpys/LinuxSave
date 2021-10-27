# LinuxSave - Backup automático

O LinuxSave é um programa onde você pode, de forma automática, realizar o backup de todos os seus
dados que forem selecionados.

### Conteúdos

* [Sobre](#Sobre)
    * [Como funciona](#Como-funciona)
* [Como usar](#Como-usar)
    * [Definindo a inicialização automática](#Definindo-a-inicialização-automática)
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

## Como usar

Aqui você aprenderá a configurar o LinuxSave.

## Definindo a inicialização automática

Essas instruções foram testadas apenas no **Ubuntu 20.4** utilizando a interface gráfica
Gnome, para outras distribuições, pesquise sobre como definir **aplicativos de inicialização**

Veja como fazer isso no Ubuntu:

1. Procure pelo programa ***Aplicativos iniciais de sessão*** e abra-o;
2. Clique no botão ***Adicionar***;
3. Preencha algumas informações, o nome pode ser LinuxSave e uma descrição opcional, como