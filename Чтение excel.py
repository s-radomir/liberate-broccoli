import pandas as pd


def plotfile(data, x_name, y_name):
    df = pd.concat([data[x_name], data[y_name]], sort=False, axis=1)
    with(open('plotfile', 'w') as f):
        for i in range(len(df)):
            print(df.iloc[i][x_name], df.iloc[i][y_name], file=f, sep=' ')


def tablefile(df):
    with(open('tablefile', 'w') as f):
        for i in df.columns:
            s = ''
            for j in df[i].tolist():
                s += ' & ' + str(j)
            print(i + s, file=f)


plot_num = int(input())
path = input()
data = pd.read_excel("name" + ".xlsx")
for i in range(plot_num):
    x, y = input()
    plotfile(data, x, y)
    tablefile(data)
    # Код по графикам
