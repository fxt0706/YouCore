import shelve


class Recoder:

    def __init__(self):
        print("Recoder Message: Recoder start")
        # file = shelve.open("./record/list.db", protocol=2, flag='c')
        # file['num'] = 0;
        # file['dict'] = {0:['title'], 1:['id'], 2:['data'],3:['subtitle'], 4:['translate'], 5:['compos'], 6:['upload']}
        # file.sync()
        # file.close()

    def latest(self,):
        file = shelve.open("./record/list.db", protocol=2, flag='c')




if __name__ == '__main__':
    recoder = Recoder()
    recoder.latest()
