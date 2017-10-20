import requests
import YouCore
import xlwt
import config

file_times = open("./resource/youku_video_times.txt","wb")
file_video = open("./resource/youku_video_list.txt","wb")
xls_data = xlwt.Workbook()
xls_table=xls_data.add_sheet('videos',cell_overwrite_ok=True)
xls_line = 1

# youku yun developer

class YouList():

    def __init__(self):
        print('YouList Message: Start output')

        self.init_xls()

        url = config.URL_LIST_YUN

        # replace your private parameter below(client_id / access_token / video_page)
        payloads = {'client_id':config.CLIENT_ID_YUN,'access_token':YouCore.get_access_token_yun(),'count':50,'page':1}
        video_page = 2

        # get the JSON data and set to list
        video_list = []
        self.trans_json(video_page,video_list,url,payloads)

        # analyze the video times and output to .txt
        video_set = set(video_list)
        for item in video_set:
            if(video_list.count(item) > 1):
                # print(" %s : %d \n" % (item, video_list.count(item)))
                words = "%s : %d \n" % (item, video_list.count(item))
                file_times.write(words.encode('utf-8'))

        # get the final list of video(without the number of occurrences) and list
        video_list_final = sorted(video_set,key = video_list.index)
        # print(video_list_final)
        for item in video_list_final:
            words = item + "\n"
            file_video.write(words.encode('utf-8'))

        # close the file
        file_times.close()
        file_video.close()
        xls_data.save("./resource/youku_video_data.xls")
        print("Get the video list succeed! \nCheck the two txt files for details")


    def export_video_list(self,video_list,youku_text,num):
        #this function list the video to video_list and export details to .xls
        for i in range(num):
            video_list.append(youku_text['videos'][i]['title'])
            global xls_line
            xls_table.write(xls_line, 0, youku_text['videos'][i]['id'])
            xls_table.write(xls_line, 1, youku_text['videos'][i]['title'])
            xls_table.write(xls_line, 2, youku_text['videos'][i]['view_count'])
            xls_table.write(xls_line, 3, youku_text['videos'][i]['link'])
            xls_table.write(xls_line, 4, youku_text['videos'][i]['published'])
            xls_line += 1


    def trans_json(self,video_page,video_list,url,payloads):
        #this fuction get the all json files and deal with the data
        for i in range(1,video_page+1):
            youku_json_get = requests.get(url, params=payloads).json()
            video_num = len(youku_json_get['videos']) - 1
            self.export_video_list(video_list, youku_json_get, video_num)
            payloads['page'] = i+1
            # time.sleep(0.9)



    def init_xls(self):
        xls_table.write(0,0,"id")
        xls_table.write(0,1,"title")
        xls_table.write(0,2,"view_count")
        xls_table.write(0,3,"link")
        xls_table.write(0,4,'published')



