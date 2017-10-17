import feedparser
import requests
import time
import schedule

class YoutubeListener:

    def __init__(self):
        print("YoutubeListener Message: Listener start")
        self.check_update()

    def check_update(self):
        feeds = feedparser.parse('https://www.youtube.com/feeds/videos.xml?channel_id=UC_x5XG1OV2P6uZZ5FSM9Ttw')
        video_title = feeds.entries[0]['title']
        print(feeds.entries[0]['updated'])
        print(feeds.entries[0]['published'])
        # print(feeds.entries[0]['id'])
        video_id = feeds.entries[0]['id'].split(':',2)[2]
        self.download_subtitles(video_id, video_title)

    def download_subtitles(self, id, title):
        print("YoutubeListener Message: download subtitles")
        sub_url = 'https://www.youtube.com/api/timedtext?lang=en&fmt=vtt&v=' + id + '&name=CC+%28English%29'
        sub = requests.get(sub_url)
        sub_file = open("./resource/subtitles/" + title +".srt", "wb")
        sub_file.write(sub.content)
        sub_file.close()

    def read_record(self):
        print()



if __name__ == '__main__':
    lisnter = YoutubeListener()