import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# x= [10,2,50,43,15]
# y= list(range(0,5))
# plt.axis([0,60,0,5])
# plt.plot(x,y)
# plt.show()


# Line Plot
data = {
    "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "Temperature": [22, 21, 23, 24, 25]
}

df = pd.DataFrame(data)
plt.plot(df["Day"], df["Temperature"], marker='o')
plt.title("Weekly Temperature")
plt.xlabel("Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Bar Chart
data = {
    "Product": ["A", "B", "C", "D"],
    "Quantity": [30, 45, 10, 20]
}

df = pd.DataFrame(data)

plt.bar(df["Product"], df["Quantity"])
plt.title("Product Quantities")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.show()


# Scatter Plot
data = {
    "Hours_Studied": [1, 2, 3, 4, 5],
    "Score": [50, 60, 65, 70, 80]
}

df = pd.DataFrame(data)

plt.scatter(df["Hours_Studied"], df["Score"])
plt.title("Study Hours vs Score")
plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.show()

data = {
    "Day": ["Mon", "Tue", "Wed", "Thu", "Fri"],
    "Visitors": [100, 120, 130, 115, 140]
}
df = pd.DataFrame(data)
plt.plot(df["Day"], df["Visitors"], marker='o', linestyle='--')
plt.title("Website Visitors Over a Week")
plt.xlabel("Day")
plt.ylabel("Number of Visitors")
plt.grid(True)
plt.show()


data = {
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
}
df = pd.DataFrame(data)
sns.barplot(x="Category", y="Values", data=df)
plt.title("Category Values")
plt.show()

data = {
    "X": [1, 2, 3, 4, 5],
    "Y": [5, 7, 6, 8, 7]
}
df = pd.DataFrame(data)
sns.scatterplot(x="X", y="Y", data=df)
plt.title("Scatter Plot Example")
plt.show()


data = {
    "Group": ["A", "A", "B", "B", "C", "C"],
    "Value": [5, 7, 8, 6, 9, 10]
}
df = pd.DataFrame(data)
sns.boxplot(x="Group", y="Value", data=df)
plt.title("Boxplot Example")
plt.show()

sns.violinplot(x="Group", y="Value", data=df)
plt.title("Violin Plot Example")
plt.show()

data = {
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
}

df = pd.DataFrame(data)
sns.heatmap(df, annot=True)
plt.title("Heatmap Example")
plt.show()

sns.pairplot(df)
plt.show()

data1 = {"X": [1, 2, 3], "Y": [3, 2, 1]}
data2 = {"X": [1, 2, 3], "Y": [1, 4, 9]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)
fig, axs = plt.subplots(1, 2, figsize=(10, 4))
axs[0].plot(df1["X"], df1["Y"])
axs[0].set_title("Graph 1")
axs[1].plot(df2["X"], df2["Y"])
axs[1].set_title("Graph 2")
plt.show()


plt.plot([1, 2, 3], [4, 5, 6], label="Line 1")
plt.plot([1, 2, 3], [6, 5, 4], label="Line 2")
plt.legend()
plt.show()

sns.set_style("darkgrid")
sns.barplot(x=["A", "B", "C"], y=[5, 7, 3])
plt.show()


plt.plot([1, 2, 3], [4, 5, 6])
plt.savefig("myplot.png")
plt.savefig("myplot.pdf")



