import pygsheets
import config

# 打开文件 读取行数 读取最后一行内容 写入内容 获得对应格子的值 列出所有内容

class YouSheet():

    def __init__(self):
        print('YouSheet Message: start sheet')

    def append_list(self, value, row, ID):
        clinet = pygsheets.authorize()
        sh = clinet.open_by_key(ID)
        ws = sh.sheet1
        ws.insert_rows(row, values=value, inherit=True)

    def append_cell(self, value, row, col, ID):
        clinet = pygsheets.authorize()
        sh = clinet.open_by_key(ID)
        ws = sh.sheet1
        ws.update_cell((col, row), value)

    def get_value(self, key, ID, latest = True):
        clinet = pygsheets.authorize()
        sh = clinet.open_by_key(ID)
        ws = sh.sheet1
        row = ws.rows
        print('row is ' + str(row))
        if key == 'ID':
            return ws.get_value((3,row))

    def get_row(self, ID):
        clinet = pygsheets.authorize()
        sh = clinet.open_by_key(ID)
        ws = sh.sheet1
        row = ws.rows
        return row

if __name__ == '__main__':
    run = YouSheet()
    run.get('ID', '1qsJERn8bEXXmtjhY3hsCitTI_lEViVZgJLa6IesXA4E')



