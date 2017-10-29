import feedparser
import requests
import time
import schedule
import YouCore

from Recorder import Recoder
from ComposVideo import ComposVideo
from YouUpload import YouUpload

class YoutubeListener:

    def __init__(self):
        print("YoutubeListener Message: listener start")
        self.check_update()
        schedule.every(60).minutes.do(self.check_task)
        while True:
            schedule.run_pending()

    def check_task(self):
        self.check_update(0)
        self.check_update(1)
        self.check_update(2)

    def check_update(self, num):
        id = ['UC_x5XG1OV2P6uZZ5FSM9Ttw','UCnUYZLuoy1rq1aVMwx4aTzw','UCVHFbqXqoYvEWM1Ddxl0QDg'] #GD CD AD
        feeds = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=' + id[num])

        self.video_id = feeds.entries[0]['id'].split(':', 2)[2]


        if Recoder.check_id(self, self.video_id):
            print('YoutubeListener Message: already latest video: ' + self.video_title)
            self.download_subtitle(self.video_id, self.video_title, 'en')
            self.download_video(self.video_title, self.video_url)
            self.compos_video(self.video_title)
            self.upload_video(self.video_title)
        else:
            if Recoder.simple_judge(self) == True:
                self.video_title = feeds.entries[0]['title']
                self.video_publish_date = feeds.entries[0]['published']
                self.video_update_date = feeds.entries[0]['updated']
                self.video_url = 'https://www.youtube.com/watch?v=' + self.video_id
                Recoder.add_new_video(self, self.video_title, self.video_id, self.video_update_date)
                print('YoutubeListener Message: new video record: ' + self.video_title)
            else:
                self.video_id = Recoder.latest()[1]
            self.download_subtitle(self.video_id, self.video_title, 'en')
            self.download_video(self.video_title, self.video_url)
            self.compos_video(self.video_title)
            self.upload_video(self.video_title)

    def download_subtitle(self, id, title, lang):
        if Recoder.check_sub(self, lang) == 'null':
            print("YoutubeListener Message: download subtitle now")
            Recoder.add_content(self, 3, 'downloading')
            sub_url = 'https://www.youtube.com/api/timedtext?lang=en&fmt=vtt&v=' + id + '&name=CC+%28English%29'
            sub = requests.get(sub_url)
            sub_file = open("./resource/subtitles/" + title +".srt", "wb")
            sub_file.write(sub.content)
            sub_file.close()
            print('YoutubeListener Message: download subtitles ' + title + " successd!")
            Recoder.add_content(self,3,'true')
        elif Recoder.check_sub(self) == 'downloading':
            print("YoutubeListener Message: still downloading subtitle")
        elif Recoder.check_sub(self) == 'true':
            print('YoutubeListener Message: ' + title + ' subtitle exist')

    def download_video(self, title, url):
        check = Recoder.check_download(self)
        if check == 'null':
            print('YoutubeListener Message: download ' + title + ' now')
            Recoder.add_content(self, 5, 'downloading')
            result = YouCore.download_youtube(title, url)
            if result == True:
                print('YoutubeListener Message: download succeess: ' + title)
                Recoder.add_content(self, 5, 'true')
            elif result == False:
                print('YoutubeListener Message: download ' + title +' failed')
                Recoder.add_content(self, 5, 'null')
        elif check == 'downloading':
            print('YoutubeListener Message: downloading now: ' + title)
        elif check == 'true':
            print('YoutubeListener Message: ' + title + ' already downloaded')

    def compos_video(self, title):
        check = Recoder.check_compos(self)
        if check == 'null':
            Recoder.add_content(self, 6, 'composing')
            result = ComposVideo.compos(self, title)
            if result == True:
                Recoder.add_content(self, 6, 'true')
            elif result == False:
                Recoder.add_content(self, 6, 'null')
        elif check == 'composing':
            print('YoutubeListener Message: compositing now: ' + title)
        elif check == 'true':
            print('YoutubeListener Message: ' + title + ' already composited')

    def upload_video(self, title):
        check = Recoder.check_upload()
        if check == 'null':
            print('YoutubeListener Message: upload ' + title + ' now')
            Recoder.add_content(self, 7, 'uploading')
            result = YouUpload()
            if result != False:
                print('YoutubeListener Message: upload ' + title + ' succeed')
                Recoder.add_content(self, 7, 'true')
            else:
                print('YoutubeListener Message: upload ' + title + ' failed')
                Recoder.add_content(self, 7, 'null')
        elif check == 'uploading':
            print('YoutubeListener Message: uploading now: ' + title)
        elif check == 'true':
            print('YoutubeListener Message: ' + title + ' already uploaded')


if __name__ == '__main__':
    lisnter = YoutubeListener()