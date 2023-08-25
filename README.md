# Проект "Укради контент друга"

этот скрипт даст вам чюжой контент конечно я не одобряю все это, но жизнь заставляет))

## Наглядный пример

![Описание изображения](https://github.com/oldman-sa/grabChannel/blob/main/example.png)

## Установка

1. Обновление всего:
  
```
apt uptade && apt upgrade
```
2. Клонируйте репозиторий:

```
git clone https://github.com/oldman-sa/grabChannel.git
```
3. Откройте папку со скриптом:

```
cd timeName
```
4. Устанавливаем важные библиотеки:

```
sudo apt install python@3.11
python3 -m pip install -r requirements.txt
```
## Запуск скрипта

```
python3 grab.py
```
## Получения api_id и api_hash

перейдите на сайт https://my.telegram.org авторизируйтесь на свой номер и перейдите в раздел ```API development tools``` получив свои данные ```api_id``` и ```api_hash```
и введи свой ```api_id``` и ```api_hash``` после введи юзер канала у которого хотите забрать контент, а после юзер своего канала и ждите
каждый пост будет обрабатываться до ```7 секунд```

