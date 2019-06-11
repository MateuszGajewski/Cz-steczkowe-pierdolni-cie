import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import csv
import pandas as pd

def zlicz():
    n = 10
    array = np.zeros((n+1,n+1,n+1,n+1))

    print(array[0,0,0,0])
    a = 1
    wynik =[]
    with open('symulacja', 'r') as csvFile, open('symulacjav', 'r') as csvFile1:
        plots = csv.reader(csvFile, delimiter=',')
        plots1 = csv.reader(csvFile1, delimiter=',')
        first_row = True
        for row, row1 in zip(plots, plots1):
            #print(a)
            if (a % 2) == 1:
                x = []
                for i in row:
                    x.append(float(i))
                vx =[]
                for i in row1:
                    vx.append(float(i))
            else:
                y = []
                for i in row:
                    y.append(float(i))
                vy = []
                for i in row1:
                    vy.append(float(i))
                array = np.zeros((n, n, n, n))
                c = mikro([x, y, vx, vy], array, n)
                wynik.append(c)

            a += 1
    print(wynik)
    return wynik
def mikro(lista, array, n):
    #print(lista)
    xmax = 30
    ymax = 2*(2/8)
    a = xmax/ 10
    b = ymax/10
    for i in range(0, len(lista[0])):
        w1 = int(lista[0][i] // a)
        w2 = int(lista[1][i] //a)
        w3 = int((lista[2][i] + (ymax/2)) //b)
        w4 = int((lista[3][i] + (ymax/2))//b)
        if w1 >= 0 and w2 >=0 and w1< 10 and w2 < 10 and w3 >= 0 and w4 >=0 and w3< 10 and w4 < 10 :
            array[(w1,w2,w3,w4)] +=1
    #print(array)
    return prawdopodobieństwo(array, n)


def prawdopodobieństwo(array, n):
    iloczyn = 1
    for i in range(0, len(array[0])):
        for j in range(0, len(array[0])):
            for k in range(0, len(array[0])):
                for l in range(0, len(array[0])):
                    iloczyn = iloczyn * np.math.factorial(array[i][j][k][l])
                    #print(iloczyn)
    praw = np.math.factorial(n)/iloczyn

    return np.log(praw)




wynik = zlicz()
# Data for plotting


fig, ax = plt.subplots()
ax.plot(wynik)

plt.show()