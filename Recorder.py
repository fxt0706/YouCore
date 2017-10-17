import shelve


class Recoder:

    def __init__(self):
        print("Recoder Message: Recoder start")
        # file = shelve.open("./record/list.db", protocol=2, flag='c')
        # file['num'] = 0;
        # file['dict'] = {0:['title'], 1:['id'], 2:['date'],3:['subtitle'], 4:['translate'], 5:['compos'], 6:['upload']}
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

    def add_new_video(self, title, id, date, subtitle, translate, compos, upload):
        print("Recoder Message: add new video: " + title)

    def check_id(self, id):
        file = shelve.open("./record/list.db", protocol=2, flag='c')
        id_latest = file['dict'][1][file['num']]
        if id_latest == id:
            return True
        else:
            return False




if __name__ == '__main__':
    recoder = Recoder()


