import config
import requests
import os
import subprocess


def get_access_token_yun():
    payloads_renew = {'grant_type': 'refresh_token'}
    payloads_renew['client_id'] = config.CLIENT_ID_YUN
    payloads_renew['refresh_token'] = config.REFRESH_TOKEN_YUN
    # print(payloads_renew)
    json_renew = requests.post(url=config.URL_RENEW_ACCESS_YUN, data=payloads_renew).json()
    # print(json_renew)
    return json_renew['access_token']

def delete_youku_video(id):
    print("YouCoreMessage: delete video for id:" + id)

def download_youtube(title,url_video):
    print("YouCoreMessage: download video " + title + " now")
    dowload_path = os.getcwd() + r'/resource/videos'
    # cmd = 'proxychains you-get --itag=137 -o ' + dowload_path + ' \'' + url_video + '\''
    cmd = 'proxychains you-get --itag=137 -o ' + dowload_path + ' \'' + url_video + '\''
    print(cmd)
    cmd_re = subprocess.call(cmd, shell=True)
    if (cmd_re == 0):
        return True
    else:
        print("YouCoreMessage: download failed. Please make sure your internet connected and check the url again")


def upload_youku(title):
    print("YouCoreMessage: upload video " + title + " to youku now")