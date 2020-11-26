from peewee import Model, DatabaseProxy, CharField, DateTimeField
from playhouse.db_url import connect

database_proxy = DatabaseProxy()


class BaseModel(Model):
    class Meta:
        database = database_proxy


class Forecast(BaseModel):
    weather_type = CharField()
    temperature = CharField()
    date = DateTimeField(unique=True)


def init(url: str):
    database = connect(url)
    database_proxy.initialize(database)
    database_proxy.create_tables([Forecast])
