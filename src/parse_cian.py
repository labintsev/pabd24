"""  https://github.com/lenarsaitov/cianparser
"""
import datetime

import cianparser
import pandas as pd
from dotenv import dotenv_values
import boto3

config = dotenv_values(".env")
client = boto3.client(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=config['KEY'],
    aws_secret_access_key=config['SECRET']
)

moscow_parser = cianparser.CianParser(location="Москва")


def main():
    """Function docstring"""
    t = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    n_rooms = 1
    CSV_PATH = f'data/raw/{n_rooms}_{t}.csv'
    data = moscow_parser.get_flats(
        deal_type="sale",
        rooms=(n_rooms,),
        with_saving_csv=True,
        additional_settings={
            "start_page": 1,
            "end_page": 2,
            "object_type": "secondary"
        })
    df = pd.DataFrame(data)

    df.to_csv(CSV_PATH,
              encoding='utf-8',
              index=False)
    bucket_name = 'pabd24'
    object_name = '1/' + CSV_PATH
    client.upload_file(CSV_PATH, bucket_name, object_name)


if __name__ == '__main__':
    main()
