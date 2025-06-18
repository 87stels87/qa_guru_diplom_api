# Пример проекта автотестов для сайта  [reqres.in]((https://reqres.in/))

![main page screenshot](images/screen/reqres.png)
![main page screenshot](images/screen/swagger.png)


###  Используемые технологии
<p align="center">
  <code><img src="images/logo/python.svg" width="40" height="40" title="Python"></code>
  <code><img src="images/logo/pytest.svg" width="40" height="40" title="PyTest"></code>
  <code><img src="images/logo/selene.png" width="40" height="40" title="Selene"></code>
  <code><img src="images/logo/pycharm.png" width="40" height="40"vtitle="PyCharm"></code>
  <code><img src="images/logo/Jenkins.svg" width="40" height="40" title="Jenkins"></code>
  <code><img src="images/logo/allure_testops.png" width="40" height="40" title="Allure TestOps"></code>
  <code><img src="images/logo/Telegram.svg" width="40" height="40" title="Telegram Bot"></code>
  <code><img src="images/logo/Allure_new.png" width="40" height="40" title="Docker"></code>
   <code><img src="images/logo/requests.png" width="40" height="40" title="Docker"></code>
</p>

## Покрываемый функционал

- [x] Отображение списка пользователей;
- [x] Отображение данных у пользователя;
- [x] Отображение почты пользователя;
- [x] Регистрация нового пользователя;
- [x] Редактирование поля job у пользователя;
- [x] Удаление заданного пользователя; 
  
## Запуск тестов
Процесс автоматизации тестирования организован с использованием Jenkins, размещённого в докер-контейнере. Контейнеризация Jenkins выполняется посредством Docker. Сам контейнер с Jenkins запущен на виртуальной машине (VM), предоставленной сервисом облачных вычислений Cloud.ru.



Для запуска тестов локально, нужно выполнить следующие шаги
1. Склонировать репозиторий
2. Открыть проект в PyCharm
3. Ввести в териминале следующие команды
``` 
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

### С помощью Jenkins
#### Для запуска автотестов необходимо:
 - Открыть джобу в jenkins
 - Нажать на кнопку Build with Parameters
 - Выбрать окружение, где будут исполняться тесты (заглушка)
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
