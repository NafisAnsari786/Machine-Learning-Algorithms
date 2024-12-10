![image](https://github.com/user-attachments/assets/392535d1-f63e-4867-bf16-ee2fbd3244e9)

This data science project series walks through step by step process of how to build a real estate price prediction website. We will first build a model using sklearn and linear regression using banglore home prices dataset from kaggle.com. Second step would be to write a python flask server that uses the saved model to serve http requests. Third component is the website built in html, css and javascript that allows user to enter home square ft area, bedrooms etc and it will call python flask server to retrieve the predicted price. During model building we will cover almost all data science concepts such as data load and cleaning, outlier detection and removal, feature engineering, dimensionality reduction, gridsearchcv for hyperparameter tunning, k fold cross validation etc. 
**Technology and tools wise this project covers,**

1. Python
2. Numpy and Pandas for data cleaning
3. Matplotlib for data visualization
4. Sklearn for model building
5. Jupyter notebook, visual studio code and pycharm as IDE
6. Python flask for http server
7. HTML/CSS/Javascript for UI

# **Deploy this app to cloud (AWS EC2)**
1. Create EC2 instance using amazon console, also in security group add a rule to allow HTTP incoming traffic
2. Now connect to your instance using a command like this,
```bash
ssh -i "C:\Users\Nafis Ansari\.ssh\bhp.pem" ubuntu@ec2-16-171-7-165.eu-north-1.compute.amazonaws.com
```
3. nginx setup
    i. Install nginx on EC2 instance using these commands,
   ```bash
   sudo apt-get update
   sudo apt-get install nginx
   ```
