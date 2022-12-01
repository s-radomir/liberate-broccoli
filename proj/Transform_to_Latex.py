import pandas as pd
import numpy as np
import csv

def read_csv(file_name):
    with open(file_name) as file:
        reader = list(csv.reader(file, delimiter=',',
                      quotechar=',', quoting=csv.QUOTE_MINIMAL))
    return reader

def make_latex_table_with_borders(data):
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data[0])
    stroka = 'c'.join(['|' for k in range(leng+1)])
    table.append('\\begin{tabular}{'.replace('//', '\\')+stroka+'}')
    table.append('\hline')
    for i in range(len(data)):
        table.append(' & '.join(data[i]) + ' \\\\')
        table.append('\hline')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

def make_latex_table_without_borders(data):
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data[0])
    stroka = 'c'.join(['' for k in range(leng+1)])
    table.append('\\begin{tabular}{'.replace('//', '\\')+stroka+'}')
    for i in range(len(data)):
        table.append(' & '.join(data[i]) + ' \\\\')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

def make_latex_table_with_separator_between_columns(data):
    table = []
    table.append("\\begin{table}".replace('//', '\\'))
    table.append("\label{}".replace('/', '\\'))
    table.append('\caption{}'.replace('/', '\\'))
    leng = len(data[0])
    stroka = 'c'.join(['|' for k in range(leng+1)])
    table.append('\\begin{tabular}{'.replace('//', '\\')+stroka+'}')
    table.append('\hline')
    for i in range(len(data)):
        table.append(' & '.join(data[i]) + ' \\\\')
        if i == 0:
            table.append('\hline')
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
    leng = len(data[0])
    stroka = ''
    for k in len_array:
        stroka += ('m{' + str(k) + 'cm}|' )
    table.append('\\begin{tabular}{'.replace('//', '\\')+'|' + stroka+'}')
    table.append('\hline')
    for i in range(len(data)):
        table.append(' & '.join(data[i]) + ' \\\\')
        table.append('\hline')
    table.append("\end{tabular}".replace('/', '\\'))
    table.append("\end{table}".replace('/', '\\'))
    return table

len_array = [2, 3, 4]
A = read_csv(r"C:\Users\user\Downloads\23.csv")
for i in make_latex_table_with_length_columns(A, len_array):
    print(i)
