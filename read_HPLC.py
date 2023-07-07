import matplotlib.pyplot as plt
import pandas as pd
import os
import scipy.stats as st
def read(file_name):
    content = []
    content_dict = {}
    with open(file_name, 'r') as f:
        while [''] != content:
            line = f.readline()
            content.append(line.replace('\n', ''))
            if line == '\n':
                if content != ['']:
                    content_dict[content[0]] = content[1:-1]
                content = []
    f.close()
    return content_dict

class HPLC:
    def __init__(self, hplc_dict):
        self.date = hplc_dict['[Header]'][3].split('\t')[1]
        self.dict = hplc_dict
    def PDA(self, num=1):
        hplc = self.dict
        x = []
        y = []
        for i in hplc[f'[PDA Multi Chromatogram(Ch{num})]']:
            x.append(i.split('\t')[0])
            y.append(i.split('\t')[1])
        x = [float(i) for i in x[y.index('Intensity')+1:]]
        y = [float(i)+10000*(num-1) for i in y[y.index('Intensity')+1:]]
        plt.plot(x, y, label=f'PDA{num}')
    def peak(self, num=1):
        hplc = self.dict
        x = []
        y = []
        for i in hplc[f'[Peak Table(PDA-Ch{num})]']:
            content = i.split('\t')
            if content[0] != '# of Peaks':
                x.append(content[1])
                y.append(content[4])
        start = x.index('R.Time')+1
        x = [float(i) for i in x[start:]]
        y = [float(i) for i in y[start:]]
        df = pd.DataFrame()
        df['RT.time'] = x
        df['Area'] = y
        return df

def find_character(df, time=23.021):
    time_df = df
    char = time_df[abs(time_df['RT.time']-time)<0.3]['Area'].values
    if len(char) > 1:
        char = max(char)
    else:
        char = char[0]
    return char

def calculate_std(file_li, time, y=[0.006, 0.03, 0.06]):
    file_li_new = []
    value_li = []
    for i in file_li:
        if 'HB' in i:
            file_li_new.append(i)
    for i in file_li_new:
        hplc = read(i)
        pda = HPLC(hplc)
        # pda.PDA(1)
        # plt.show()
        df = pda.peak(1)
        value = find_character(df, time)
        value_li.append(value)
    y = y # 因变量为第 2 列数据
    x = value_li # 自变量为第 3 列数据
    # 线性拟合，可以返回斜率，截距，r 值，p 值，标准误差
    slope, intercept, r_value, p_value, std_err = st.linregress(x, y)
    return slope, intercept, r_value**2 # 输出斜率 输出截距 输出 r^2


if __name__ == '__main__':
    file_li = os.listdir()
    file_li_new = []
    value_li = []
    for i in file_li:
        if 'S' in i:
            file_li_new.append(i)
    for i in file_li_new:
        hplc = read(i)
        pda = HPLC(hplc)
        df = pda.peak(1)
        weight_df = pd.read_csv('weight', delimiter='\t')
        tag = i.replace('.txt', '')
        value = find_character(df, 24.369)/weight_df[tag].values[0]
        value_li.append(value)
    data = pd.DataFrame()
    data['x'] = [i.replace('.txt', '') for i in file_li_new]
    data['y'] = value_li
    data['hue'] = [i.split('-')[0] for i in file_li_new]
    import seaborn as sns
    sns.barplot(data=data, x=data['hue'], y=data['y'])
    # plt.legend()
    plt.show()
    
#  "LCA": 23.021, 'gcg': 6.336, 'gcs': 12.289, 'ggcd': 24.369