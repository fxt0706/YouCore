import requests
import config

class YouTo():

    def __init__(self):
        print("YouTo Meassage: start YouTube Catcher")

    def get_duration(self, video_id):
        url = 'https://www.googleapis.com/youtube/v3/videos?id=' + video_id + '&key=' + config.GO_API + '&part=contentDetails'
        r = requests.get(url).json()
        duration = r['items'][0]['contentDetails']['duration']
        duration = '' + duration[2:]
        duration = duration.replace('M', 'min ')
        duration = duration.replace('S', 'second')
        duration = duration.replace('H', 'hour ')
        return duration

if __name__ == '__main__':
    run = YouTo()
    run.get_duration('ZhnsEyal-ok')