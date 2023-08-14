from pywebio import input
from pywebio.output import *
from pywebio import start_server

from read_HPLC_ import read, HPLC, find_character, read_web
#from std_last import main as std
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 部署后端，解决闪退报错的问题
import matplotlib
matplotlib.use('Agg')

def set(f, file_name_li, 
        name_li, 
        RT_time,
        channel, 
        Threshold=0.1):
    data = pd.DataFrame()
    for name in name_li:
        file_content = []
        value_li = []
        for i in file_name_li:
            if name in i and '.txt' in i:
                file_content.append(f[file_name_li.index(i)])
        for i in file_content:
            hplc = read_web(i)
            pda = HPLC(hplc)
            df = pda.peak(channel)
            # tag = i.replace('.txt', '')
            try:
                value = find_character(df, RT_time, Threshold) # 时间为样品峰的时间
            except:
                value = None
            value_li.append(value)
        try:
            data[name] = value_li
        except:
            data_row = data.shape[0]
            add_num = data_row - len(value_li)
            value_li = value_li + [None for i in range(add_num)]
            data[name] = value_li
    return data
    
def sample_cluster1(f):
    file_name_li = []
    for file_dict in f:
        file_name = file_dict['filename']
        file_name_li.append(file_name)
    return file_name_li
def sample_cluster2(file_name_li):
    name_li = []
    for i in file_name_li:
        if i[0:2] not in name_li:
            name_li.append(i[0:2])
    return name_li



def train():
    ff = input.input_group('HPLC info', [
        input.file_upload('Upload a HPLC file or files (text file transfered from .lcd)', multiple=True, name='f'),
        input.file_upload('Please upload the RT time and compound csv file', name='RT_time'),
        input.input('What is your standard of grouping? (eg. files constituted by "aa1.txt, aa2.txt, aa3.txt, bb1.txt, bb2.txt" should be printed as "aa bb", just use blank space " " to split aa and bb)', name='name_li'),
        input.input('RT threshold(OPTINAL, default=0.1 min)', name='Threshold'),
        input.select('PDA_Channel: ', [1, 2, 3], name='detect')])
    RT_li = list(read_web(ff['RT_time']).values())[0]
    file_name_li = sample_cluster1(ff['f'])
    name_li = ff['name_li'].split(' ')
    if name_li == None:
        name_li = sample_cluster2(file_name_li)
    for RT_C in RT_li:
        if RT_C != '':
            RT_C_li = RT_C.split(',')
            RT_time = RT_C_li[0]
            C = RT_C_li[1]
            #try:
            data = set(ff['f'], file_name_li=file_name_li, RT_time=float(RT_time), name_li=name_li, Threshold=float(ff['Threshold']), channel=ff['detect'])    
            fig = plt.figure(dpi=200)
            sns.barplot(data)
            plt.xticks(rotation=90, fontsize=6)
            plt.savefig('test.png')
            img = open('test.png', 'rb').read() 
            put_text(C) 
            put_image(img, width='1400px')
            table_list = [data.columns]+[data.loc[i] for i in range(data.shape[0])]
            put_table(table_list)
            put_text('\n\n', '--'*50)
            # except:
            #     put_text('No result')
            
            
    
if __name__ == '__main__': 
    start_server(train, port=1314)