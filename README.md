# AERO-test
Test

# Тестовое задание Aero DE

Привет 👩🏼‍💻 

В рамках работы помимо размышлений о красивой и функциональной архитектуре аналитической платформы, часто нужно писать коннекторы, которые будут наполнять эту самую платформу жизнью и смыслом. Некоторые из них полностью или частично уже отработаны в рамках нашей кодовой базы, но мы постоянно пополняем её потому что никогда не знаешь какие источники понадобятся тому или иному клиенту. 

В тестовом задании как раз нужно будет написать один не сложный коннектор. 

Мы используем ЯП Python и SQL для общения с базой.
В чем суть: у нас есть открытое api (мне нравится вот это `https://random-data-api.com/api/cannabis/random_cannabis?size=10`, но если ты хочешь поработать с другим я не против) из которого нужно каждые 12 часов забирать данные и складывать к нам в хранилище. Коннектор должен будет реализовать простую логику ELT процесса, когда мы забираем данные и кладем без изменений к себе для дальнейшей обработки. Оркестрацию можно сделать на кроне или написать коннектор под Airflow.

Базу выбирай на свое усмотрение, но будет круто, если это будет Postgres, Clickhouse или Greenplum.

Для проверки код готового коннектора нужно выложить себе в гитхаб, а ссылку прислать нам 🙂

p.s. если api для тебя слишком простой используй информацию отсюда для записи в базу `https://statsapi.web.nhl.com/api/v1/teams/21/stats` — моя любимая команда 🏒

p.p.s схема данных во втором апи на усмотрение: ожидаются массивы и их можно или распарсить или попробовать уложить как есть

