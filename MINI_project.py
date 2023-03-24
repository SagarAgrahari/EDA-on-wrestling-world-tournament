import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
print("Wrestling dataset")
dt=pd.read_csv("E:\Desktop\pyminipro\Wrestling.csv")
df=pd.DataFrame(dt)



print("************************************************************************")


#1.Relation between gender and nationality
plt.figure(figsize=(10,8))
sns.countplot(x='gender',hue='nationality',data=df)
plt.title("Relation between gender and nationality ")
plt.show()

#2.Comparision with strength and age
c=df[df['strength']>2].tail(10)
sns.scatterplot(x='age',y='strength',data=c)
plt.title("Strength of player according to their age")
plt.show()

#3.Year start in between 2002 to 2004 
d=df[df['year_start'].between(2002,2004)].tail(10)
sns.histplot(x='year_start',bins=20,data=d) 
plt.title("Player start their career between 2002-2004")
plt.show()

#4.count plot graph with weight
plt.figure(figsize=(10,8))
sns.countplot(x='weight',hue='gender',data=df)
plt.show()

#5.Rank between 60-90
e=df[df['rank'].between(60,90)].tail(10)
sns.barplot(x='federation',y='rank',data=e)
plt.title("rank and federation")
plt.show()


#6.number of player who have age less than 20
print(" Players Age less than 20 ")
f=df[df['age']<20].head(5)
print(f)


#7.kdeplot graph of wrestling
sns.kdeplot(df)
plt.title("Kernel Density Graph")
plt.show()

#8.highest strength of player
print("Highest strength of the players")
print(df['strength'].max())


#9.Maximum height
print("MAX HEIGHT OF WRESTLER")
print(df["height"].max())
print("\n\n")


#10.Nationality value count
print("Player's nationality in dataset")
print(df['nationality'].value_counts(10))



