import shelve


class Recoder:

    def __init__(self):
        print("Recoder Message: Recoder start")
        # file = shelve.open("./record/list.db", protocol=2, flag='c')
        # file['num'] = 0;
        # file['dict'] = {0:['title'], 1:['id'], 2:['date'],3:['subtitle_en'], 4:['subtitle_cn'], 5:['download_video'], 6:['compos_en'], 7:['upload_en'], 8:['compos_cn'], 9:['upload_cn']}
        # file.sync()
        # file.close()

    def latest(self):
        file = shelve.open("./record/list.db", protocol=2, flag='c')
        num = file['num']
        out_dict = {}
        for i in range(0,7):
            out_dict[i] = file['dict'][i][num]
        file.close()
        return out_dict

    def add_new_video(self, title, id, date,):
        file = shelve.open("./record/list.db", writeback=True)
        num = file['num'] + 1

        file['dict'][0].append(title)
        file['dict'][1].append(id)
        file['dict'][2].append(date)

        for i in range(3,10):
            temp = file['dict'][i]
            temp.append('null')
            file['dict'][i] = temp
        file['num'] = num

        file.sync()
        print('Recoder Message: the dict is : \n')
        print(file['dict'])

        file.close()
        print("Recoder Message: add new video: " + title)


    def check_id(self, id):
        file = shelve.open("./record/list.db", protocol=2, flag='c')
        id_latest = file['dict'][1][file['num']]
        print("Recoder Message: latest id is " + id_latest)
        file.close()
        if id_latest == id:
            return True
        else:
            return False

    def check_sub(self, lang):
        if lang == 'en':
            file = shelve.open("./record/list.db", protocol=2, flag='c')
            num = file['num']
            sub_latest = file['dict'][3][num]
            file.close()
            return sub_latest
        elif lang == 'cn':
            file = shelve.open("./record/list.db", protocol=2, flag='c')
            num = file['num']
            sub_latest = file['dict'][4][num]
            file.close()
            return sub_latest

    def check_download(self):
        file = shelve.open("./record/list.db", protocol=2, flag='c')
        num = file['num']
        download_latest = file['dict'][5][num]
        file.close()
        return download_latest

    def check_compos(self):
        file = shelve.open("./record/list.db", protocol=2, flag='c')
        num = file['num']
        compos_latest = file['dict'][6][num]
        file.close()
        return compos_latest

    def check_upload(self):
        file = shelve.open("./record/list.db", protocol=2, flag='c')
        num = file['num']
        upload_latest = file['dict'][7][num]
        file.close()
        return upload_latest

    def add_content(self, item, content):
        file = shelve.open("./record/list.db", writeback=True)
        num = file['num']
        file['dict'][item][num] = content
        file.sync()
        file.close()

    def simple_judge(self):
        file = shelve.open("./record/list.db", writeback=True)
        num = file['num']
        sub_latest = file['dict'][3][num]
        download_latest = file['dict'][5][num]
        compos_latest = file['dict'][6][num]
        upload_latest = file['dict'][7][num]

        for each in sub_latest,download_latest,compos_latest,upload_latest:
            if each == 'null':     # if not finished, do schedule again
                return False
            elif each == 'running':
                return False

        return True



if __name__ == '__main__':
    recoder = Recoder()

