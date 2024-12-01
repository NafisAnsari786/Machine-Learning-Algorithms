## **Outlier Detection and Handling Using Interquantile Range**

```python
Q1 = df['abc'].quantile(0.25)

Q2 = df['abc'].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5*IQR
upper_limit = Q3 + 1.5*IQR
```
