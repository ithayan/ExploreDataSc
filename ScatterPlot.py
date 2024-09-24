import pandas as pd 
import matplotlib
import matplotlib.pyplot as plt

apple= pd.read_csv('blackapple.csv')
samsung = pd.read_csv('samsung_op1.csv')

matplotlib.rcParams['figure.figsize'] = (15,10)
plt.scatter(apple.High,apple.Low,color='blue',label='Apple', s=50)
plt.scatter(samsung.High,samsung.Low,marker='+', color='green',label='Samsung', s=50)
plt.xlabel("High")
plt.ylabel("Low")
plt.title('Apple Vs Samsung Price comparision')
plt.legend()