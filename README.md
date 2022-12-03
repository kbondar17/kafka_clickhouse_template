1. docker-compose up -d

2. создать окружение
 
3. запустить апи для отправки timestamps

```uvicorn src.api.api:app```

4. начать принимать сообщения из кафки и загружать в кликхаус

```python3 -m src.kafka_to_house_etl```

5. отправить тестовые данные 

```python3 -m src.api.fake_views```


