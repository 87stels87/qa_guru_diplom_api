# Пример проекта автотестов для сайта  [https://reqres.in/]([https://okko.tv/](https://reqres.in/))

![main page screenshot](images/screen/reqres.png)
![main page screenshot](images/screen/swagger.png)


###  Используемые технологии
<p align="center">
  <code><img src="images/logo/python-original.svg" width="40" height="40" title="Python"></code>
  <code><img src="images/logo/pytest-original.svg" width="40" height="40" title="PyTest"></code>
  <code><img src="images/logo/selene.png" width="40" height="40" title="Selene"></code>
  <code><img src="images/logo/pycharm.png" width="40" height="40"vtitle="PyCharm"></code>
  <code><img src="images/logo/jenkins-original.svg" width="40" height="40" title="Jenkins"></code>
  <code><img src="images/logo/selenoid.png" width="40" height="40" title="Selenoid"></code>
  <code><img src="images/logo/Allure_Report.png" width="40" height="40" title="Allure Report"></code>
  <code><img src="images/logo/AllureTestOps.png" width="40" height="40" title="Allure TestOps"></code>
  <code><img src="images/logo/tg.png" width="40" height="40" title="Telegram Bot"></code>
  <code><img src="images/logo/docker.png" width="40" height="40" title="Docker"></code>
</p>

## Покрываемый функционал
✅ Главная страница:
- [x] Наличие секции по вводу промокода;
- [x] Проверка наименования почты в разделе акций;
- [x] Наличие секции "Новые фильмы" в разделе "Магазин";
- [x] Проверка урла после редиректа по кнопке "Подписка";
  
✅ Карточка фильма:
- [x] Наличие кнопки "Купить";
- [x] Отображение плеера при просмотре трейлера;
- [x] Оценка фильма незарегистрированным пользователем;
  
✅ Поиск фильмов:
- [x] Отображение на странице поиска секции "Часто ищут";
- [x] Поиск фильма по наименованию;
- [x] Поиск фильма по фамилии и имени режиссера;

## Запуск тестов
#### Тесты запускаются в Jenkins (инфраструктура qa-guru). Selenoid развернут в докер-контейнере. Докер поднят на вирутальной машине сервиса https://cloud.ru/

### Локально
Перед запуском нужно создать файл .env и указать там login, password и url для selenoid 


Для запуска тестов локально, нужно выполнить следующие шаги
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в териминале следующие команды
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
context=web pytest -m web  
```

### С помощью [Jenkins](https://jenkins.autotests.cloud/job/C19-AndreyOok-diplom-ui/)
#### Для запуска автотестов необходимо:
 - Открыть [джобу](https://jenkins.autotests.cloud/job/C19-AndreyOok-diplom-ui/) в jenkins
 - Нажать на кнопку Build with Parameters
 - Выбрать версию хрома
 - Выбрать окружение, где будут исполняться тесты
 - Нажать на Build

<img src="images/screen/jenkins_parametrs.png">

## Отчет о прохождении тестов (Allure)
### Локально
Для получения отчета нужно ввести команду 
```
allure serve tests/allure-results
``` 
Ниже представлен пример allure отчета 
<img src="images/screen/report_1.png">

Подробные инструкции по работе с allure можно найти по [ссылке](https://allurereport.org/docs/)..
### Если тесты запускались в Jenkins

Для получения отчета нужно нажать на иконку allure report'a в строке билда  
У него будет точно такой же формат, как и при получении локально
<img src="images/screen/report_1.png">

### В проекте реализована интеграция с Allure TestsOps. Проект в TestOps можно найти по [ссылке](https://allure.autotests.cloud/project/4791/dashboards).
<img src="images/screen/testops1.png">
<img src="images/screen/testops2.png">
<img src="images/screen/testops3.png">

### В проекте настроена отправка краткого отчета в Telegram
<img src="images/screen/tg.png">

#### Нагрузка виртуальной машины (vCPU=2, RAM=4) во время прогона тест-кейсов:
<img src="images/screen/proc1.png">
<img src="images/screen/package.png">
