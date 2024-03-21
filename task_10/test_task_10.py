from task_10 import  init_params, feed_forward, loss_function, gradient_descent
import pytest
import numpy as np

def test_init_params():
    W, b = init_params()
    assert W.shape == (1, 1)
    assert b.shape == (1, 1)

def test_feed_forward():
    W = np.array([[2]])
    b = np.array([[1]])
    x = np.array([[1, 2, 3, 4]])
    expected = np.array([2,4,6,8])
    y_pred = feed_forward(W, b, x)
    np.testing.assert_allclose(y_pred, expected)

def test_loss_function():
    y_pred = np.array([2, 4, 6])
    y = np.array([1, 3, 5])
    loss = loss_function(y,y_pred)
    expected_loss = 1.0
    assert loss == expected_loss

def test_gradient_descent():
    x = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
    y = np.array([[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]])
    learning_rate = 0.001
    iterations = 3000
    W, b, loss_history = gradient_descent(x, y, learning_rate, iterations)
    expected_y = y.flatten()
    y_pred =  feed_forward(W, b, x).flatten()
    np.testing.assert_allclose(y_pred, expected_y)
    assert loss_history[-1] < loss_history[0]