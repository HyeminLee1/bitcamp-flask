import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())

class PopStructure():

    data: [] = list()
    home: [] = list()

    def read_data(self):
        df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands=',', index_col=0)
        df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_without_comma.csv', 'rt', encoding='UTF-8'))
        # next(data)
        # print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) ->[] :
        # [주의] csv reader 는 1회 이상 사용하면 GC(가비지컬렉터)가 제거한다.
        arr = []
        [arr.append(int(i)) for j in self.data if dong in j[0] for i in j[3:]]
        print(arr)
        return arr

    def show_flot(self, arr: []):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

    def find_similar_dong(self):
        data = self.data
        name = input('인구 구조가 알고 은싶 지역의 이름(읍면동 단위)을 입력해주세요 : ')
        # home = (np.array(i[3:], dtype=int) for i in data if name in i[0])
        # home: np.array([])
        for i in data:
            if name in i[1]:
                self.home = np.array(i[3:], dtype=int)
        return self.home

        # plt.rc('font', family='C:/Windows/Fonts/H2GTRE.ttf')
        # plt.title(name + '지역의 인구구조')
        # plt.plot(home)
        # plt.show()


    def array_to_list(self, arr: object) -> []:
        return arr.to_list()

    def list_to_arrary(self, ls: []) -> object:
        return np.array(ls)

    def show_plot_home(self, arr: object):
        plt.title(f'{self.home} 지역의 인구 구조')
        plt.plot(arr)
        plt.show()


if __name__ == '__main__':
    pop = PopStructure()
    pop.read_data()
    # pop.show_flot(pop.pop_per_dong('역삼2동'))
    print(pop.find_similar_dong())