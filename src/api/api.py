from fastapi import FastAPI, Cookie, Depends
from http import HTTPStatus
from kafka import errors

from src.api.models import MovieTimeStamp
from src.my_kafka.kafka_producer import kafka

 
app = FastAPI(docs_url='/docs')


@app.post("/send_stamp")
async def send_time_stamp(data:MovieTimeStamp):
    """отправляем в кафку инфу о прогрессе просмотра фильма юзером"""

    key = str(data.user_id).encode('utf-8') + '+'.encode('utf-8') + \
            str(data.movie_id).encode('utf-8') 
    value = str(data.timestamp).encode('utf-8')

    kafka.send(key=key, value=value)

    return HTTPStatus.OK
    