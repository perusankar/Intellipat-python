import matplotlib as mpl
import matplotlib.pyplot as plt


print(mpl.__version__)
x = [0,10]
y =[0,30]
plt.xlabel('Average')
plt.ylabel('Calorie')
plt.grid(linestyle='dotted',color='silver') #axis='x'
plt.title("Data analysis",pad=8,loc='left')
plt.plot(x,y,marker='o',markersize=10,mec='red',
         mfc='yellow',linestyle='dotted',color='red',linewidth=5)
x1 = [0,31]
y1 =[1,26]
plt.plot(x1,y1)
plt.show()
