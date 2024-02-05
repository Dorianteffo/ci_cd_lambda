import logging 
import requests
import boto3
import os 
import datetime
import json

logging.basicConfig(level=logging.INFO, 
                              format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)


def extract_api_data(url : str, headers : dict)->dict: 
    try : 
        response = requests.get(url, headers=headers)
        if response.status_code == 200 : 
            data = json.loads(response.text)['results']
            logger.info('API data extracted')
            return data 
    except Exception as e : 
        logger.error('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        logger.error(f'Error while extracting data from the api: {e}')




def upload_to_s3(bucket_name : str, key : str, data : dict) : 
    data_string = json.dumps(data, indent=2, default=str)


    # Upload JSON String to an S3 Object
    s3 = boto3.client('s3')

    s3.put_object(
        Bucket=bucket_name, 
        Key=key,
        Body=data_string
    )



def lambda_handler(event, context): 
    authorization = os.environ.get('Authorization')
    
    url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"
    headers = {
        "accept": "application/json",
        "Authorization": authorization
    }

    today_date = datetime.date.today().strftime("%Y-%m-%d")

    bucket_name = "movie-api-data-daily"
    key = f"api_data/{today_date}/movies.json"

    data = extract_api_data(url, headers)

    upload_to_s3(bucket_name, key, data)





