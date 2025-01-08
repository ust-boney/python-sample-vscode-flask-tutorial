import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[6,7,8,9,10]
plt.title("Pie graph ")
plt.xlabel="Weekdays"
plt.ylabel="Values"
# plt.scatter(x,y)
# plt.bar(x,y)
a=["SUN","MON","TUE","WED","THU","FRI","SAT"]
b=[10,20,30,40,50,60,70]
plt.pie(b,labels=a)
plt.show()