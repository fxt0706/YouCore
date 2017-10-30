import subprocess
import os

class ComposVideo:

    def __init__(self):
        print("YouTools Message: Composite video start")

    def compos(self, title):
        print('ComposVideo Message: start compos video ' + title)
        path = os.getcwd() + '/resource/videos'
        cmd = r'cd ' + path
        cmd_re = subprocess.call(cmd, shell=True)
        if cmd_re == 0:
            cmd = r'cd ' + path +' && mkvmerge -o \'' + title + '.en.mkv\' \'' + title + '.mp4\' \'' + title + '.en.srt\''
            print(cmd)
            cmd_re = subprocess.call(cmd, shell=True)   # strart compositon

            result = os.path.isfile(path + '/' + title +'.en.mkv')
            if result == True:
                print('ComposVideo Message: video composition succeed: ' + title)
                return True
            elif result == False:
                print('ComposVideo Message: something error during the video composition')
                return False
        elif cmd_re == 1:
            return False
            print('ComposVideo Message: cd command wrong.')

if __name__ == '__main__':
    video = ComposVideo()
    video.compos(r'The Developer Show (TL;DR 085)')