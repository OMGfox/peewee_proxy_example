from datetime import datetime
from pprint import pprint
from db_utils.init import init, Forecast


class DatabaseUpdater:
    def __init__(self, url):
        init(url)
        self.database = Forecast()

    def get_forecast(self, date_from: datetime = None, date_to: datetime = None):
        result = self.database.select()
        for data in result:
            print(data.weather_type)

    def save_forecast(self, weather_data):
        for data in weather_data:
            self.database.get_or_create(**data)


if __name__ == '__main__':
    url = "sqlite:///forecast.db"
    database_updater = DatabaseUpdater(url)
    weather_data = [{"weather_type": "Дождь",
                     "temperature": "+20",
                     "date": datetime(year=2020, month=11, day=25)},
                    {"weather_type": "Солнечно",
                     "temperature": "+25",
                     "date": datetime(year=2020, month=11, day=26)}
                    ]
    database_updater.save_forecast(weather_data)
    database_updater.get_forecast()
