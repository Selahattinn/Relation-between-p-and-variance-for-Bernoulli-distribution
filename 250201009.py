import matplotlib.pyplot as plt

#this is the p list
pList=[]
#this is the variation list
var=[]
#intial p value
p=float(0)
#
x = int(input("write integer(I didnt have try- catch block ) : "))
for i in range(0,x):
    #appending  p to p list 
    pList.append(p)
    #appending variation to variation list
    var.append(p-(p*p))
    #regenearete p value
    p+=1/x
#plot    
plt.plot(pList,var)
plt.xlabel("p")
plt.ylabel("variation")
plt.show()

#in my tests variation not changing and it always 0.25