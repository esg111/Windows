import tkinter
from datetime import datetime


class WriteFile:
    def __init__(self):
        self.name = ['날짜', '시간', '기록자',
                     '위치', '개수', '씨앗 이름',
                     '습도', '조도', '온도', '장비 결함 여부',
                     '나무', '꽃', '과일',
                     '최소 높이', '최대 높이', '평균 높이',
                     '메모']

    def writeFile(self, var_list):
        file = open('test.txt', 'a+')
        file.write(str(datetime.today()) + '\n')
        for idx, i in enumerate(var_list):
            if idx == 16:
                file.write(self.name[idx] + ": " + str(i.get('1.0', tkinter.END)) + '\n')
            else:
                file.write(self.name[idx] + ": " + str(i.get()) + '\n')
        file.close()
