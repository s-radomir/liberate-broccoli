import pandas as pd
import numpy as np



def make_latex_table_with_borders(data):
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data.axes[1])
    stroka = 'c'.join(['|' for k in range(leng+1)])
    table.append('\\begin{tabular}{'.replace('//', '\\')+stroka+'}')
    table.append('\hline')
    for j in range(len(data.axes[0])):
        for i in range(len(data.axes[1])):
            table.append(str(data.iat[j, i]))
            if i != len(data.axes[1])-1:
                table.append('&')
        table.append(' \\\\')
        table.append('\hline')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

def make_latex_table_without_borders(data):
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data.axes[1])
    stroka = 'c'.join(['' for k in range(leng+1)])
    table.append('\\begin{tabular}{'.replace('//', '\\')+stroka+'}')
    for j in range(len(data.axes[0])):
        for i in range(len(data.axes[1])):
            table.append(str(data.iat[j, i]))
            if i != len(data.axes[1])-1:
                table.append('&')
        table.append(' \\\\')
        table.append('\hline')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

def make_latex_table_with_separator_between_columns(data):
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data.axes[1])
    stroka = 'c'.join(['|' for k in range(leng+1)])
    table.append('\\begin{tabular}{'.replace('//', '\\')+stroka+'}')
    table.append('\hline')
    for j in range(len(data.axes[0])):
        for i in range(len(data.axes[1])):
            table.append(str(data.iat[j, i]))
            if i != len(data.axes[1]) - 1:
                table.append('&')
    table.append('\hline')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

def make_latex_table_with_length_columns(data, len_array):
    '''
    :param data:
    :param len_array: ширина столбца в сантиметрах
    :return:
    '''
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data.axes[1])
    stroka = ''
    for k in len_array:
        stroka += ('m{' + str(k) + 'cm}|' )
    table.append('\\begin{tabular}{'.replace('//', '\\')+'|' + stroka+'}')
    table.append('\hline')
    for j in range(len(data.axes[0])):
        for i in range(len(data.axes[1])):
            table.append(str(data.iat[j, i]))
            if i != len(data.axes[1]) - 1:
                table.append('&')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

len_array = [2, 3, 4]
Q = pd.read_excel(r'C:\Users\user\liberate-broccoli\proj\l.xlsx')
for i in make_latex_table_with_borders(Q):
    print(i)