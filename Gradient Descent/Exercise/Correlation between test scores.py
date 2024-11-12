
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import math

def prediction_using_sklearn():
    df=pd.read_csv(r"F:\Machine Learning all Algorithms\Day 1\Gradient Descent\test_scores.csv")
    reg=LinearRegression()
    reg.fit(df[['math']], df['cs'])
    return reg.coef_, reg.intercept_

def gradient_descent(x,y):
    m_curr=0
    b_curr=0
    iterations=1000
    n=len(x)
    learning_rate=0.01
    cost_previous=0

    for i in range(iterations):
        y_predicted=m_curr * x + b_curr         # y=mx+b
        cost=(1/2)*sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))      
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr-learning_rate*md
        b_curr = b_curr-learning_rate*bd
        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous=cost
        print("m{}, b{}, cost{}, iterations{}".format(m_curr, b_curr, cost, i))

    return m_curr, b_curr

if __name__=="__main__":
    df=pd.read_csv(r"F:\Machine Learning all Algorithms\Day 1\Gradient Descent\test_scores.csv")
    x=np.array(df.math)
    y=np.array(df.cs)

    m,b=gradient_descent(x,y)
    print("Using Gradient Descent function: coef {}, intercept {}".format(m,b))

    m_sklearn, b_sklearn=prediction_using_sklearn()
    print("Using sklearn: coef {}, intercept {}".format(m_sklearn, b_sklearn))
