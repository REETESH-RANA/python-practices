import numpy as np
import math
# price=np.array([2000,2045,2067,2400,1900])
# time=np.array([9.0,11.0,13.0,15.0,17.0])
# pricemean=np.mean(price)
# print(pricemean)

# timemean=np.mean(time)
# print(timemean)

# mp=(price-pricemean*time-timemean)*(price-pricemean*time-timemean)
# print(mp)

# sd=np.std(mp,axis=0)
# print(sd)

# merging method for finding standard deviation
# x=np.array([2000,2045,2067,2400,1900])
# xm=x.mean()
# v=(x-xm)**2
# # print(v)
# vs=v.sum()
# sd=math.sqrt(vs/x.size-1)
# print(sd)
# print(x.std())


# finding median

# x=np.array([2000,2045,2067,2400,1900])
# x.sort()
# print(x)
# xm=x.size
# print("size of  array",xm)
# if(xm%2!=0): #if total no of  terms are odd
#     median=(xm+1)/2
# else:#if total no of terms are even
#     median=xm/2
# print(median)


# coeficient of correlation function
x=np.array([2000,2045,2067,2400,1900])
y=np.array([3000,2345,8683,1233,2222])
xmean=x.mean()
ymean=np.mean(y)
print(xmean)
xi=((x-xmean)*(y-ymean)).sum()
# print(xi.sum())
xu=((x-xmean)**2).sum()
xv=((y-ymean)**2).sum()
xc=math.sqrt(xu*xv)
print(xi/xc)