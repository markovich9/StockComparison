from matplotlib import pylab as plt
import pandas as pd
#loading the data sets for Mercedes and Toyota stock price history 2021-22
df1 = pd.read_csv(r"C:\Users\User\Desktop\MBG.DE.csv")
print(df1.head())

df2 = pd.read_csv(r"C:\Users\User\Desktop\TM.csv")
print(df2.head())
#calculating averages
avg1 = df1["Close"].mean()
avg2 = df2["Close"].mean()
#using matplotlib to plot stock prices
plt.figure("Mercedes Stock")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.5, label="Mercedes Stock Price 2021-22"+str(avg1))
plt.figure("Toyota Stock")
plt.plot("Date", "Close", 'r-', linewidth=0.5, label="Toyota Stock Price 2021-22"+str(avg2), data=df2)

plt.show()

plt.scatter(df1["Date"], df1["Close"], color="k")
plt.scatter(df2["Date"], df2["Close"], color="g")
plt.show()
#I decided to analyse these two stock price averages as they come from two different car companies
#Mercedes being the more luxurious one and Toyota being a more 'middle class' brand
#Mercedes stock price remained higher overall during the entire period
#However the two stocks recorded a similar trend over the past year, with Toyota crashing slightly earlier
#Both experienced a fall with the start of the Russia-Ukraine war
#This is due to exacerbated crises regarding fuel and semiconductors which are produced in Russia and Ukraine