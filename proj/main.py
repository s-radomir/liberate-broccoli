import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set()   

def is_True(c):
    return c == 'y' or c == 'Y' or c == '1' or c == 'True' or c == 'yes' or c == 'Yes'


#Это просто базовые вопросы 
print("Retain previous settings? y/n")
if (not is_True(input())):
    print("Build a graph in just a few seconds!\nEnter lab number:")
    lab_num = input()
    print("Enter graph name/number:")
    graph_num = input()
    GRAPHFILEPATH = '/home/fima/Documents/uni/labs/' + lab_num + '/figs/graph_' + graph_num + '.png' 

    print("Enter datafile name:(in same directory as this program)")
    DATA_FILE = input()

    print('X-axis?(latex)')
    X_axis = input()
    print('Y-axis?(latex)')
    Y_axis = input()
    print("Round to what precision?")
    ROUND_ON_GRAPH_TO = input()
    f = open('settings', 'w', encoding = 'utf-8')
    f.write(GRAPHFILEPATH + '\n' +  DATA_FILE + '\n' + X_axis + '\n' + Y_axis + '\n' + ROUND_ON_GRAPH_TO)
    f.close()
f = open('settings', 'r', encoding = 'utf-8')

[GRAPHFILEPATH, DATA_FILE, X_axis, Y_axis, ROUND_ON_GRAPH_TO] = f.read().split('\n')
ROUND_ON_GRAPH_TO = int(ROUND_ON_GRAPH_TO)
f.close()

print("Display or save. Display? /n")
if is_True(input()):
    GRAPHFILEPATH = ''

f = open(DATA_FILE, "r", encoding="utf-8")
ar = list(map(lambda x: x.rstrip().split(), f.readlines()))
f.close()
ar = [[float(y) for y in x] for x in ar]

X = []
Y = []
erX = []
erY = []

plt.xlabel(r'M $ \cdot  10^{-2} \: Н \cdot м $')
plt.ylabel(Y_axis)

for [x, y] in ar:
    X.append(x)
    Y.append(y)
    erY.append(0)
    erX.append(0)


def count_MNK(X, Y):
    def avg(a):
        return np.sum(a)/a.size
    x1=x = np.array(X)
    y1=y = np.array(Y)
    n = x1.size
    k1 = (avg(x1*y1)-avg(x1)*avg(y1))/(avg(x1*x1) - avg(x1)**2)
    b1 = avg(y1) - k1 * avg(x1) 
    sk = (1/(n ** 0.5)) * ((avg(y * y) - avg(y) ** 2)/(avg(x * x) - avg(x) ** 2) - k1 ** 2) ** 0.5
    sb = sk * (avg(x * x) - avg(x) ** 2)
    return (k1, sk, b1, sb)

def fitline(xdata, xerror, ydata, yerror, col):
    [k, b] = np.polyfit(np.array(xdata),np.array(ydata),1)
    plt.scatter(X, Y, color = col)
    plt.errorbar(X, Y, xerr=erX, yerr=erY , fmt="o", color = col)
    x = np.linspace(min(xdata) * 0.9 ,max(xdata)*1.1,100)
    strL = r'$Y \approx$ ' + str(round(k, ROUND_ON_GRAPH_TO)) + ' $X$ + ' + str(round(b, ROUND_ON_GRAPH_TO));
    [k,dk,b,db] = count_MNK(xdata, ydata)
    strL += '\n'+r'$\sigma_k=$' + str(round(dk, ROUND_ON_GRAPH_TO)) + r';  $\sigma_b=$' + str(round(dk, ROUND_ON_GRAPH_TO));
    plt.plot(x, k*x+b, '-', color = 'green', label=strL)
fitline(X, erX, Y, erY, 'green')


plt.scatter(X, Y, s=20)
plt.legend()    
if (GRAPHFILEPATH == ''):
    plt.show()
else:
    plt.savefig(GRAPHFILEPATH)   # save the figure to file
