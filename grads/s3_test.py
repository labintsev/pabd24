import pandas as pd
from dotenv import dotenv_values
import boto3

BUCKET_NAME = 'pabd24'

config = dotenv_values(".env")

df = pd.read_csv('../docs/results.csv')

s3_resource = boto3.resource(
    's3',
    endpoint_url='https://storage.yandexcloud.net',
    aws_access_key_id=config['KEY'],
    aws_secret_access_key=config['SECRET']
)

bucket = s3_resource.Bucket(BUCKET_NAME)


def graduate(user_id: int) -> int:
    score = 0

    for obj in bucket.objects.filter(Prefix=f'{user_id}/data/raw'):
        print(obj.key)
        if obj.key.endswith('.csv'):
            score = 4

    return score


df['2'] = df['ID'].map(graduate)
df.to_csv('tmp.csv')
