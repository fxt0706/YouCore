import config
import requests


def get_access_token_yun():
    payloads_renew = {'grant_type': 'refresh_token'}
    payloads_renew['client_id'] = config.CLIENT_ID_YUN
    payloads_renew['refresh_token'] = config.REFRESH_TOKEN_YUN
    print(payloads_renew)
    json_renew = requests.post(url=config.URL_RENEW_ACCESS_YUN, data=payloads_renew).json()
    print(json_renew)
    return json_renew['access_token']

def delete_youku_video(id):
    print("YouCoreMessage: delete video for id:" + id)

def download_youtube(url,title):
    print("YouCoreMessage: download video " + title + " now")

def upload_youku(title):
    print("YouCoreMessage: upload video " + title + " to youku now")