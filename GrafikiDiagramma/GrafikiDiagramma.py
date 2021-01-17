import numpy as np
import matplotlib
import matplotlib.pyplot as plt

x1 = np.arange(-7, 7, 1)
y1 = -3/49*x1**2+8
x2 = np.arange(-7, 7, 1)
y2 = 4/49*x2**2+1
x3 = np.arange(-6.8, -2, 1)
y3 = -0.75*(x3+4)**2+11
x4 = np.arange(2, 6.8, 1)
y4 = -0.75*(x4-4)**2+11
x5 = np.arange(-5.8, -2.8, 1)
y5 = (x5+4)**2+9
x6 = np.arange(2.8, 5.8, 1)
y6 = (x6+4)**2-9
x7 = np.arange(-4, 4, 1)
y7 = 4/9*x7**2-5
x8 = np.arange(-5.2, 5.2, 1)
y8 = 4/9*x8**2-9
x9 = np.arange(-7, -2.8, 1)
y9 = -1/16*(x9+3)**2-6
x10 = np.arange(2.8, 7, 1)
y10 = -1/16*(x10-3)**2-6
x11 = np.arange(-7, 0, 1)
y11 = 1/9*(x11+4)**2-11
x12 = np.arange(0, 7, 1)
y12 = 1/9*(x12-4)**2-11
x13 = np.arange(-7, -4.5, 1)
y13 = -(x13+5)**2
x14 = np.arange(4.5, 7, 1)
y14 = -(x14-5)**2
x15 = np.arange(-3, 3, 1)
y15 = 2/9*x15**2+2



plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
#plt.tick_params(axis="x", direction="in",length=10, width=0,color="red",labelsize=10, labelrotation=0)
plt.grid(axis="x", color="black", alpha=.3, linewidth=5, linestyle="")
plt.xticks(np.arange(-50, 50, 2))
plt.grid(True)
plt.plot(x1,y1 ,'-g',linewidth=1,label="Парабола")
plt.plot(x2,y2 ,'-g',linewidth=1,label="Парабола")
plt.plot(x3,y3 ,'-r',linewidth=1,label="Парабола")
plt.plot(x4,y4 ,'-r',linewidth=1,label="Парабола")
#plt.plot(x5,y5 ,'-g',linewidth=1,label="Парабола")
#plt.plot(x6,y6 ,'-r',linewidth=1,label="Парабола")
plt.plot(x7,y7 ,'-r',linewidth=1,label="Парабола")
plt.plot(x8,y8 ,'-g',linewidth=1,label="Парабола")
plt.plot(x9,y9 ,'-b',linewidth=1,label="Парабола")
plt.plot(x10,y10 ,'-b',linewidth=1,label="Парабола")
plt.plot(x11,y11 ,'-b',linewidth=1,label="Парабола")
plt.plot(x12,y12 ,'-b',linewidth=1,label="Парабола")
plt.plot(x13,y13 ,'-b',linewidth=1,label="Парабола")
plt.plot(x14,y14 ,'-b',linewidth=1,label="Парабола")
plt.plot(x15,y15 ,'-r',linewidth=1,label="Парабола")


plt.savefig("my_image.png") 
plt.show()


data = [
        ["Erinevate IKT turvameetodite kasutamine", 86],
        ["Tarkvara värskemate versioonide kasutamine", 70],
        ["Andmete varundamine eraldi keskkond", 64],
        ["Tugev paroolide autentimine", 61],
        ["Võrgujuurdepääsu kontroll", 60],
        ["VPN-i kasutamine",39],
        ["Turvaintsidendi logifailide kopeerimine ja säilitamine analüüsiks", 35],
        ["Andmete;dokumentide;e-kirjade krüpteerimine", 30],
        ["IKT turvatestid", 28],
        ["IKT riskianalüüside teostamine", 24],
        ["Kasutaja tuvastamine biomeetriliste meetoditega", 6]
    ]
values = [x[1] for x in data]
labels = [x[0] for x in data]
plt.pie(values,labels=labels,autopct="%.1f%%", radius=1.5)
plt.show()




x20 = np.arange(0, 9, 1)
y20 = 2/27*x20**2-3
x21 = np.arange(-10, 0, 1)
y21 = 0.04*x21**2-3
x22 = np.arange(-9, -3, 1)
y22 = 2/9*(x22+6)**2+1
x23 = np.arange(-3, 9, 1)
y23 = -1/12*(x23-3)**2+6
x24 = np.arange(5, 8, 1)
y24 = 1/9*(x24-5)**2+2
x25 = np.arange(5, 8, 1)
y25 = 1/8*(x25-7)**2+1.5
x26 = np.arange(-13, -9, 1)
y26 = -0.75*(x26*11)**2+6
x27 = np.arange(-15, -13, 1)
y27 = -0.5*(x27+13)**2+3
x28 = np.arange(-15, -10, 1)
y28 = [1] * len(x28)
x29 = np.arange(3, 4, 1)
y29 = [3] * len(x29)


plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(axis="x", color="black", alpha=.3, linewidth=5, linestyle="")
plt.xticks(np.arange(-50, 50, 2))
plt.grid(True)
plt.plot(x20,y20 ,'-b',linewidth=1,label="Парабола")
plt.plot(x21,y21 ,'-b',linewidth=1,label="Парабола")
plt.plot(x22,y22 ,'-b',linewidth=1,label="Парабола")
plt.plot(x23,y23 ,'-b',linewidth=1,label="Парабола")
plt.plot(x24,y24 ,'-b',linewidth=1,label="Парабола")
plt.plot(x25,y25 ,'-b',linewidth=1,label="Парабола")
#plt.plot(x26,y26 ,'-r',linewidth=1,label="Парабола")
plt.plot(x27,y27 ,'-b',linewidth=1,label="Парабола")
plt.plot(x28,y28 ,'-b',linewidth=1,label="Парабола")
plt.plot(x29,y29 ,'-b',linewidth=1,label="Парабола")



plt.savefig("my_image.png") 
plt.show()

x30 = np.arange(-12, 12, 1)
y30 = -1/18*x30**2+12
x31 = np.arange(-4, 4 ,1)
y31 = -1/8*x31**2+6
x32 = np.arange(-12, -4, 1)
y32 = -1/8*(x32+8)**2+6
x33 = np.arange(4, 12, 1)
y33 = -1/8*(x33-8)**2+6
x34 = np.arange(-4, -0.3, 1)
y34 = 2*(x34+3)**2-9
x35 = np.arange(-4, 0.2, 1)
y35 = 1.5*(x35+3)**2-10


plt.subplots()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(axis="x", color="black", alpha=.3, linewidth=5, linestyle="")
plt.xticks(np.arange(-50, 50, 2))
plt.grid(True)
plt.plot(x30,y30 ,'-g',linewidth=1,label="Парабола")
plt.plot(x31,y31 ,'-g',linewidth=1,label="Парабола")
plt.plot(x32,y32 ,'-r',linewidth=1,label="Парабола")
plt.plot(x33,y33 ,'-r',linewidth=1,label="Парабола")
plt.plot(x34,y34 ,'-g',linewidth=1,label="Парабола")
plt.plot(x35,y35 ,'-r',linewidth=1,label="Парабола")


plt.savefig("my_image.png") 
plt.show()