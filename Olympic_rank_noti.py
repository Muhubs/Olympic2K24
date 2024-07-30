from airflow.models import DAG
from airflow.decorators import dag, task
from airflow.utils.dates import days_ago
import pandas as pd
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

default_args = {
    'owner': 'Olympic_2K24',
}


@task()
def ranking():
    session = HTMLSession()
    url = 'https://olympics.com/en/paris-2024/medals?utm_campaign=dp_google'
    r = session.get(url)
    soup = BeautifulSoup(r.content, 'lxml')

    #extract country
    spans = soup.find_all('span', class_='elhe7kv5 emotion-srm-uu3d5n')
    data = [span.get_text(strip=True) for span in spans]
    df = pd.DataFrame(data, columns=['Country'])

    # extract total_metal
    total_matal = soup.find_all('span', class_='e1oix8v91 emotion-srm-5nhv3o')
    data_total = [span.get_text(strip=True) for span in total_matal]
    df2 = pd.DataFrame(data_total, columns=['Total_matal'])
    df2["Total_matal"] = pd.to_numeric(df2["Total_matal"])
    return df , df2

@task ## mapping data
def combined_ranking(df,df2):
    df_combined = pd.concat([df, df2], axis=1)
    return df_combined

@task ## Send notification
def line_noti(df_combined):
    url = 'https://notify-api.line.me/api/notify'
    token = 'hi9Y226luEYnNNogmmjI3GS2dA5vU8tTykZz5Djh2A7'
    headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
    msg = df_combined.to_string()  # แปลง DataFrame เป็นข้อความ
    r = requests.post(url, headers=headers, data={'message': msg})


@dag(default_args=default_args, start_date=days_ago(1), tags=['Olympic2024xx'])
def olym_pipeline():
    t1 = ranking()
    t2 = combined_ranking()
    t3 = line_noti()
    t1 >> t2 >> t3
olym_pipeline()
