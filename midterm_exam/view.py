import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import Spinbox
from datetime import datetime


class View:
    def __init__(self):
        self.loc = None
        self.curRad = None

        # 초기 윈도우 설정
        self.win = tk.Tk()
        self.win.title("Python GUI Midterm Project")
        self.win.geometry('600x720')
        self.win.resizable(True, True)

        # 데이터가 담길 변수목록
        self.date_var = tk.StringVar()
        self.time_var = tk.StringVar()
        self.recorder_var = tk.StringVar()
        self.location_var = tk.StringVar()
        self.seedsCount_var = tk.StringVar()
        self.seedName_var = tk.StringVar()
        self.humidity_var = tk.StringVar()
        self.illuminance_var = tk.StringVar()
        self.temperature_var = tk.StringVar()
        self.treeCount_var = tk.StringVar()
        self.flowerCount_var = tk.StringVar()
        self.fruitCount_var = tk.StringVar()
        self.minHeight_var = tk.StringVar()
        self.maxHeight_var = tk.StringVar()
        self.avgHeight_var = tk.StringVar()
        self.defect_var = tk.IntVar()

        # 위젯 생성
        self.create_widgets()
        self.setup_layout()
        self.reset()

    # 초기화
    def reset(self):
        self.date_var.set('')
        self.time_var.set('')
        self.recorder_var.set('')
        self.location_var.set(3)
        self.seedsCount_var.set('')
        self.seedName_var.set('')
        self.humidity_var.set('')
        self.illuminance_var.set('')
        self.temperature_var.set('')
        self.treeCount_var.set('')
        self.flowerCount_var.set('')
        self.fruitCount_var.set('')
        self.minHeight_var.set('')
        self.maxHeight_var.set('')
        self.avgHeight_var.set('')
        self.memo_textfield.delete('1.0', tk.END)
        self.defect_var.set(0)

    # 저장 (공백이거나 숫자가 아닐 경우 데이터 저장 실패 메시지 출력)
    def save(self):
        intVar_list = [self.humidity_var, self.illuminance_var, self.temperature_var,
                       self.treeCount_var, self.flowerCount_var, self.fruitCount_var,
                       self.minHeight_var, self.maxHeight_var, self.avgHeight_var]
        var_list = [self.date_var, self.time_var, self.recorder_var,
                    self.location_var, self.seedsCount_var, self.seedName_var,
                    self.humidity_var, self.illuminance_var, self.temperature_var, self.defect_var,
                    self.treeCount_var, self.flowerCount_var, self.fruitCount_var,
                    self.minHeight_var, self.maxHeight_var, self.avgHeight_var,
                    self.memo_textfield]
        error_name = ['습도', '조도', '온도',
                      '나무', '꽃', '과일',
                      '최소 높이', '최대 높이', ' 평균 높이']
        write = WriteFile()
        error_point = []
        error = 0
        for idx, i in enumerate(intVar_list):
            if not (i.get().isdigit() | (i.get() == '')):
                error += 1
                error_point.append(error_name[idx])

        if error > 0:
            self.result_label.config(text='{}에서 에러 발생 : Plot. 데이터 저장 실패!'.format(error_point))
        else:
            self.result_label.config(text='일지가 저장되었습니다.')
            write.writeFile(var_list)
            self.reset()

    # 위젯 생성
    def create_widgets(self):
        self.title = tk.Label(self.win, text="식물 일지 프로그램", anchor='center', font=('Arial', 20))

        ###############################################################################################
        # Record info: 라벨 프레임
        self.recordInfo = tk.LabelFrame(self.win, text='Record Information')

        # Record info: 내부를 vertical 방향으로 3칸 나눔, 정렬을 위한 라벨 생성
        self.record_boundary1 = tk.Label(self.recordInfo)
        self.record_boundary2 = tk.Label(self.recordInfo)
        self.record_boundary3 = tk.Label(self.recordInfo)

        # Record info: subtitle1
        self.title_date = tk.Label(self.record_boundary1)
        self.subTitle_date = tk.Label(self.title_date, text='날짜')
        self.title_time = tk.Label(self.record_boundary2)
        self.subTitle_time = tk.Label(self.title_time, text='시간')
        self.title_recorder = tk.Label(self.record_boundary3)
        self.subTitle_recorder = tk.Label(self.title_recorder, text='기록자')

        # 날짜 입력 엔트리
        self.date_label = tk.Label(self.record_boundary1)
        self.date_entered = tk.Entry(self.date_label, textvariable=self.date_var)

        # 시간 콤보 박스
        self.time_label = tk.Label(self.record_boundary2)
        self.time_chosen = ttk.Combobox(self.time_label, width=12, textvariable=self.time_var, state='readonly')
        self.time_chosen['values'] = ('00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00',
                                      '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00',
                                      '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00',
                                      '21:00', '22:00', '23:00',)

        # 기록자 성명 엔트리
        self.recorder_label = tk.Label(self.record_boundary3)
        self.recoder_entered = tk.Entry(self.recorder_label, textvariable=self.recorder_var)

        # Record info: subtitle2
        self.title_location = tk.Label(self.record_boundary1)
        self.subTitle_location = tk.Label(self.title_location, text='위치')
        self.title_seed_count = tk.Label(self.record_boundary2)
        self.subTitle_seedcount = tk.Label(self.title_seed_count, text='개수')
        self.title_seed_name = tk.Label(self.record_boundary3)
        self.subTitle_seedname = tk.Label(self.title_seed_name, text='씨앗 이름')

        # 위치 라디오 버튼
        self.location_label = tk.Label(self.record_boundary1)

        # 씨앗 개수 콤보 박스
        self.seed_count_label = tk.Label(self.record_boundary2)
        self.seeds_chosen = ttk.Combobox(self.seed_count_label, width=12,
                                         textvariable=self.seedsCount_var,
                                         state='readonly')
        self.seeds_chosen['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

        # 씨앗 이름 엔트리
        self.seed_name_label = tk.Label(self.record_boundary3)
        self.seed_name_entered = tk.Entry(self.seed_name_label, textvariable=self.seedName_var)

        ###############################################################################################
        # Environment data: 라벨 프레임
        self.environmentData = tk.LabelFrame(self.win, text='Environment Data')

        # Environment data: 내부를 vertical 방향으로 3칸 나눔, 정렬을 위한 라벨 생성
        self.env_boundary_1 = tk.Label(self.environmentData)
        self.env_boundary_2 = tk.Label(self.environmentData)
        self.env_boundary_3 = tk.Label(self.environmentData)

        # Environment data: subtitle
        self.title_humidity = tk.Label(self.env_boundary_1)  # 습도
        self.subTitle_humidity = tk.Label(self.title_humidity, text='습도 (g/m³)')
        self.title_illuminance = tk.Label(self.env_boundary_2)  # 조도
        self.subTitle_illuminance = tk.Label(self.title_illuminance, text='조도 (klx)')
        self.title_temperature = tk.Label(self.env_boundary_3)  # 온도
        self.subTitle_temperature = tk.Label(self.title_temperature, text='온도 (℃)')

        # 습도 데이터 스핀 박스
        self.humidity_data_label = tk.Label(self.env_boundary_1)
        self.humidity_data_spin = Spinbox(self.humidity_data_label, from_=0, to=100, textvariable=self.humidity_var)

        # 조도 데이터 스핀 박스
        self.illuminance_data_label = tk.Label(self.env_boundary_2)
        self.illuminance_data_spin = Spinbox(self.illuminance_data_label, from_=0, to=700, increment=50,
                                             textvariable=self.illuminance_var)

        # 온도 데이터 스핀 박스
        self.temperature_data_label = tk.Label(self.env_boundary_3)
        self.temperature_data_spin = Spinbox(self.temperature_data_label, from_=-30, to=50,
                                             textvariable=self.temperature_var)

        # 장비 결함 여부 체크 버튼
        self.defect_data_label = tk.Label(self.env_boundary_1)
        self.defect_checkBtn = tk.Checkbutton(self.defect_data_label, text='장비 결함 여부', variable=self.defect_var,
                                              anchor='w')
        ###############################################################################################
        # Plant data: 라벨 프레임
        self.plantData = tk.LabelFrame(self.win, text='Environment Data')

        # Plant data: 내부를 vertical 방향으로 3칸 나눔, 정렬을 위한 라벨 생성
        self.plant_boundary_1 = tk.Label(self.plantData)
        self.plant_boundary_2 = tk.Label(self.plantData)
        self.plant_boundary_3 = tk.Label(self.plantData)

        # Plant data: subtitle1
        self.title_treeCount = tk.Label(self.plant_boundary_1)  # 습도
        self.subTitle_tree = tk.Label(self.title_treeCount, text='나무')
        self.title_flowerCount = tk.Label(self.plant_boundary_2)  # 조도
        self.subTitle_flower = tk.Label(self.title_flowerCount, text='꽃')
        self.title_fruitCount = tk.Label(self.plant_boundary_3)  # 온도
        self.subTitle_fruit = tk.Label(self.title_fruitCount, text='과일')

        # 나무 데이터 스핀 박스
        self.tree_data_label = tk.Label(self.plant_boundary_1)
        self.tree_data_spin = Spinbox(self.tree_data_label, from_=0, to=20,
                                      textvariable=self.treeCount_var)

        # 꽃 데이터 스핀 박스
        self.flower_data_label = tk.Label(self.plant_boundary_2)
        self.flower_data_spin = Spinbox(self.flower_data_label, from_=0, to=20,
                                        textvariable=self.flowerCount_var)

        # 과일 데이터 스핀 박스
        self.fruit_data_label = tk.Label(self.plant_boundary_3)
        self.fruit_data_spin = Spinbox(self.fruit_data_label, from_=0, to=20,
                                       textvariable=self.fruitCount_var)

        # Plant data: subtitle2
        self.title_minHeight = tk.Label(self.plant_boundary_1)
        self.subTitle_minH = tk.Label(self.title_minHeight, text='최소 높이(cm)')
        self.title_maxHeight = tk.Label(self.plant_boundary_2)
        self.subTitle_maxH = tk.Label(self.title_maxHeight, text='최대 높이(cm)')
        self.title_avgHeight = tk.Label(self.plant_boundary_3)
        self.subTitle_avgH = tk.Label(self.title_avgHeight, text='평균 높이(cm)')

        # 최소 높이 데이터 스핀 박스
        self.minHeight_data_label = tk.Label(self.plant_boundary_1)
        self.minHeight_data_spin = Spinbox(self.minHeight_data_label, from_=0, to=500,
                                           textvariable=self.minHeight_var)
        # 최대 높이 데이터 스핀 박스
        self.maxHeight_data_label = tk.Label(self.plant_boundary_2)
        self.maxHeight_data_spin = Spinbox(self.maxHeight_data_label, from_=0, to=500,
                                           textvariable=self.maxHeight_var)
        # 평균 높이 데이터 스핀 박스
        self.avgHeight_data_label = tk.Label(self.plant_boundary_3)
        self.avgHeight_data_spin = Spinbox(self.avgHeight_data_label, from_=0, to=500,
                                           textvariable=self.avgHeight_var)
        ###############################################################################################
        # 메모
        self.title_memo = tk.Label(self.win)
        self.subTitle_memo = tk.Label(self.title_memo, text='메모')
        self.memo_frame = tk.Label(self.win)
        self.memo_textfield = scrolledtext.ScrolledText(self.memo_frame, wrap=tk.WORD, height=15)
        ###############################################################################################
        # 초기화 저장 버튼
        self.button_frame = tk.Label(self.win)
        self.save_btn = tk.Button(self.button_frame, text="저장", command=self.save)
        self.reset_btn = tk.Button(self.button_frame, text="초기화", command=self.reset)
        ###############################################################################################
        self.result_frame = tk.Label(self.win)
        self.result_label = tk.Label(self.result_frame, text='')

    # 위젯 배치
    def setup_layout(self):

        self.title.pack()
        self.recordInfo.pack(fill='x')
        self.record_boundary1.pack(fill='both', side='left', expand=True)
        self.record_boundary2.pack(fill='both', side='left', expand=True)
        self.record_boundary3.pack(fill='both', side='left', expand=True)
        self.title_date.pack(fill='x')
        self.subTitle_date.pack(side='left')
        self.title_time.pack(fill='x')
        self.subTitle_time.pack(side='left')
        self.title_recorder.pack(fill='x')
        self.subTitle_recorder.pack(side='left')
        self.date_label.pack(fill='x')
        self.date_entered.pack(side='bottom', fill='x', expand=True)
        self.time_label.pack(fill='x')
        self.time_chosen.pack(side='left', fill='x', expand=True)
        self.recorder_label.pack(fill='x')
        self.recoder_entered.pack(side='left', fill='x', expand=True)
        self.title_location.pack(fill='x')
        self.subTitle_location.pack(side='left')
        self.title_seed_count.pack(fill='x')
        self.subTitle_seedcount.pack(side='left')
        self.subTitle_seedname.pack(side='left')
        self.title_seed_name.pack(fill='x')
        self.subTitle_seedname.pack(side='left')
        self.location_label.pack(fill='x')
        self.loc = ['A동', 'B동', 'C동']
        for col in range(3):
            self.curRad = tk.Radiobutton(self.location_label, text=self.loc[col], variable=self.location_var,
                                         value=col)
            self.curRad.pack(side='left', fill='x', expand=True)
        self.seed_count_label.pack(fill='x')
        self.seeds_chosen.pack(side='left', fill='x', expand=True)
        self.seed_name_label.pack(fill='x')
        self.seed_name_entered.pack(side='left', fill='x', expand=True)
        self.environmentData.pack(fill='x')
        self.env_boundary_1.pack(fill='both', side='left', expand=True)
        self.env_boundary_2.pack(fill='both', side='left', expand=True)
        self.env_boundary_3.pack(fill='both', side='left', expand=True)
        self.title_humidity.pack(fill='x')
        self.title_illuminance.pack(fill='x')
        self.title_temperature.pack(fill='x')
        self.subTitle_humidity.pack(side='left')
        self.subTitle_illuminance.pack(side='left')
        self.subTitle_temperature.pack(side='left')
        self.humidity_data_label.pack(fill='x')
        self.humidity_data_spin.pack(side='left', fill='x', expand=True)
        self.illuminance_data_label.pack(fill='x')
        self.illuminance_data_spin.pack(side='left', fill='x', expand=True)
        self.temperature_data_label.pack(fill='x')
        self.temperature_data_spin.pack(side='left', fill='x', expand=True)
        self.defect_data_label.pack(fill='x')
        self.defect_checkBtn.pack(side='left', fill='x', expand=True)
        self.plantData.pack(fill='x')
        self.plant_boundary_1.pack(fill='both', side='left', expand=True)
        self.plant_boundary_2.pack(fill='both', side='left', expand=True)
        self.plant_boundary_3.pack(fill='both', side='left', expand=True)
        self.title_treeCount.pack(fill='x')
        self.title_flowerCount.pack(fill='x')
        self.title_fruitCount.pack(fill='x')
        self.subTitle_tree.pack(side='left')
        self.subTitle_flower.pack(side='left')
        self.subTitle_fruit.pack(side='left')
        self.tree_data_label.pack(fill='x')
        self.tree_data_spin.pack(side='left', fill='x', expand=True)
        self.flower_data_label.pack(fill='x')
        self.flower_data_spin.pack(side='left', fill='x', expand=True)
        self.fruit_data_label.pack(fill='x')
        self.fruit_data_spin.pack(side='left', fill='x', expand=True)
        self.title_minHeight.pack(fill='x')
        self.subTitle_minH.pack(side='left')
        self.title_maxHeight.pack(fill='x')
        self.subTitle_maxH.pack(side='left')
        self.title_avgHeight.pack(fill='x')
        self.subTitle_avgH.pack(side='left')
        self.minHeight_data_label.pack(fill='x')
        self.minHeight_data_spin.pack(side='left', fill='x', expand=True)
        self.maxHeight_data_label.pack(fill='x')
        self.maxHeight_data_spin.pack(side='left', fill='x', expand=True)
        self.avgHeight_data_label.pack(fill='x')
        self.avgHeight_data_spin.pack(side='left', fill='x', expand=True)
        self.title_memo.pack(fill='x')
        self.subTitle_memo.pack(side='left')
        self.memo_frame.pack(fill='x')
        self.memo_textfield.pack(side='left', fill='x', expand=True)
        self.button_frame.pack(fill='x')
        self.save_btn.pack(side='right')
        self.reset_btn.pack(side='right')
        self.result_frame.pack(fill='x')
        self.result_label.pack(side='left')


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
                file.write(self.name[idx] + ": " + str(i.get('1.0', tk.END)) + '\n')
            else:
                file.write(self.name[idx] + ": " + str(i.get()) + '\n')
        file.close()


view = View()
view.win.mainloop()
