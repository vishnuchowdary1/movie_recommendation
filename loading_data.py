import boto3
import json
import logging
from decimal import Decimal

dynamo_client = boto3.resource(
    "dynamodb", 
    region_name='us-east-2'
    )


def genre_upload(genre):
    genre_table = "genre"
    table = dynamo_client.Table(genre_table)

    try:
        # Read json file 
        with open("data/genre.json") as file:
            genre_data = json.load(file)

        genres = genre_data['genres']

        # iterate through data
        with table.batch_writer() as batch:
            for genre in genres:
                batch.put_item(Item=genre)

        print(f"Genre data upload to {table}")

    except Exception as e:
        print(f"An error occured {str(e)}")


# def movie_upload(movies):
movie_table = "movies"
table = dynamo_client.Table(movie_table)

# try:
# Read json file
with open("movies.json") as file:
    movie_data = json.load(file)

for page in movie_data: 
    with table.batch_writer() as batch:
        batch.put_item(Item=str(page))

    print(f"Movie data is uploaded to {table}")
    
# except Exception as e:
#     print(f"An error occured {str(e)}")
