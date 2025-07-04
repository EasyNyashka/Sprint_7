# Sprint_7
## Тестировать API учебного сервиса Яндекс Самокат.
Необходимо:
1. Создание курьера, проверь, что:
- курьера можно создать;
- нельзя создать двух одинаковых курьеров;
- чтобы создать курьера, нужно передать в ручку все обязательные поля;
- запрос возвращает правильный код ответа;
- успешный запрос возвращает {"ok":true};
- если одного из полей нет, запрос возвращает ошибку;
- если создать пользователя с логином, который уже есть, возвращается ошибка.
2. Логин курьера, проверить, что:
- курьер может авторизоваться;
- для авторизации нужно передать все обязательные поля;
- система вернёт ошибку, если неправильно указать логин или пароль;
- если какого-то поля нет, запрос возвращает ошибку;
- если авторизоваться под несуществующим пользователем, запрос возвращает ошибку;
- успешный запрос возвращает id.
3. Создание заказа, проверить, что, когда создаёшь заказ:
- можно указать один из цветов — BLACK или GREY;
- можно указать оба цвета;
- можно совсем не указывать цвет;
- тело ответа содержит track.
4. Список заказов, проверить, что:
- в тело ответа возвращается список заказов.

#### Перед работой установлены зависимости: `pip3 install -r requirements.txt`
#### После выполнения работы запустить все тесты из директории tests можно: `pytest tests --alluredir=allure_results`
#### Отчет посмотреть: `allure serve allure_results`