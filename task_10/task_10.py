# Task 10

# Implement gradient descent in python on the data:
# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# y = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Plot the fit after every few iterations.

# References:
# matplotlib

import numpy as np
import matplotlib.pyplot as plt


def init_params():
    W = np.random.rand(1, 1)
    b = np.random.rand(1, 1)
    return W, b


def feed_forward(W, b, x):
    return np.squeeze(W @ x + b)


def loss_function(y_pred, y):
    return np.mean((y_pred - y) ** 2)


def plot_fit(x, y, W, b, iterations, plot_interval=30):
    fig, ax = plt.subplots()
    ax.plot(x.flatten(), y.flatten(), color="blue")
    (line,) = ax.plot([], [], color="red")
    for i in range(iterations):
        y_pred = feed_forward(W, b, x)
        if i % plot_interval == 0:
            line.set_data(x.flatten(), y_pred)
            ax.set_title(f"Iteration {i}")
            fig.canvas.draw()
            plt.pause(0.2)
    plt.show()


def gradient_descent(x, y, learning_rate, iterations):
    W, b = init_params()
    loss_history = []
    for _ in range(iterations):
        y_pred = feed_forward(W, b, x)
        loss = loss_function(y_pred, y)
        loss_history.append(loss)
        dl_dW = -2 / len(x) * np.sum(x * (y - y_pred))
        dl_db = -2 / len(x) * np.sum(y - y_pred)
        W = W - learning_rate * dl_dW
        b = b - learning_rate * dl_db
    return W, b, loss_history


if __name__ == "__main__":
    x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    print(x.shape)
    y = np.array([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]])

    learning_rate = 0.001
    iterations = 1000

    W, b, loss_history = gradient_descent(x, y, learning_rate, iterations)

    plot_fit(x, y, W, b, iterations)

    # Plot the final fit
    plt.figure()
    plt.plot(x.flatten(), y.flatten(), color="blue")
    plt.plot(x.flatten(), feed_forward(W, b, x), color="red")
    plt.title("Final Fit")
    plt.show()

    # Plot the cost function over iterations
    plt.figure()
    plt.plot(range(len(loss_history)), loss_history)
    plt.xlabel("Iteration")
    plt.ylabel("Loss")
    plt.title("Loss Function over Iterations")
    plt.show()
