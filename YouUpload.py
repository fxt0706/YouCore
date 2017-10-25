import os
import sys
import subprocess
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests

import config
import YouCore
from youku_official import YoukuUpload

class YouUpload():

    def __init__(self, video_name):

        path = os.getcwd() + '/resource/videos'
        # change video_name to your onine title of YouTube video

        # replace client_id and refresh_token with your parameter
        client_id = config.CLIENT_ID_YUN
        refresh_token = config.REFRESH_TOKEN_YUN
        upload_path = '\'' + path + '/' + video_name + '.en.mkv' + '\''

        # input the info of video
        self.video_info = {
            'title' : video_name,
            'tags' : '',
            'description' : '',
            'category' : ''
        }

        access_token = YouCore.get_access_token_yun()

        youku_obj = YoukuUpload(client_id, access_token, upload_path)
        youku_obj.upload(self.video_info)
        youku_obj.check()
        result = youku_obj.commit()

        if youku_obj.finished == True:
            return result
        elif youku_obj.finished == False:
            return False


if __name__ == '__main__':
    YouUpload('The Developer Show (TL;DR 085)')