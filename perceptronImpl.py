import numpy as np
import matplotlib.pyplot as plt
from util import sign, gerar_dados, divide_data

# matplotlib.use("TkAgg")


# Data = np.loadtxt('DataAV2.csv', delimiter=',')
Data = gerar_dados()

X, y, X_teste, y_teste = divide_data(Data[:, :-1], Data[:, -1])

N, p = X.shape
X = X.T
X = np.concatenate((-np.ones((1, N)), X))

LR = 0.001
erro = True
max_epoch = 10
epoch = 0

w = np.zeros((p + 1, 1))

#train
while erro and epoch < max_epoch:
    erro = False
    w_anterior = w
    e = 0
    for t in range(N):
        x_t = X[:, t].reshape((p + 1, 1))
        u_t = (w.T @ x_t)[0, 0]

        y_t = sign(u_t)
        # d_t = y[t, 0]
        d_t = y[t]

        e_t = int(d_t - y_t)
        w = w + (e_t * x_t * LR) / 2
        if y_t != d_t:
            erro = True
            e += 1

    print("epoch training: "+str(epoch))
    epoch += 1


print("Training weights (w):")
print(w)

plt.scatter(X_teste[y_teste == 1, 0], X_teste[y_teste == 1, 1], color='blue', edgecolors='k', label='Class 1')
plt.scatter(X_teste[y_teste == -1, 0], X_teste[y_teste == -1, 1], color='red', edgecolors='k', label='Class -1')

plt.xlim(X_teste[:, 0].min() - 1, X_teste[:, 0].max() + 1)
plt.ylim(X_teste[:, 1].min() - 1, X_teste[:, 1].max() + 1)

x_axis = np.linspace(-15,8,100)
x2 = w[0,0]/w[2,0] - x_axis*(w[1,0]/w[2,0])


plt.plot(x_axis, x2, color='green')

plt.show()