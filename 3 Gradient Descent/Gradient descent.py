import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0             # M current and B current starts from 0 initially
    iterations = 1000
    n = len(x)                      # n is the length of the array x
    learning_rate = 0.01


    for i in range(iterations):
        y_predicted = m_curr * x + b_curr       # y-mx+b
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])        # we need to reduce the cost at each iteration
        md = -(2/n)*sum(x*(y-y_predicted))      # md is M derivative using the formula 
        bd = -(2/n)*sum(y-y_predicted)          # bd is B derivative
        m_curr = m_curr - learning_rate * md    # update M
        b_curr = b_curr - learning_rate * bd    # update B
        print("m{}, b{}, cost{}, iterations{}".format(m_curr, b_curr, cost, i))



x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13])

gradient_descent(x,y)