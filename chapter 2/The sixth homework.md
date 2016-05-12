#第六次作业#

##· 摘要 ##
本次作业完成了第六次作业的L1，完成了2.9题的两个要求的实现：

1.重现Figure 2.5 的图像，即给出初始速度(inital velocity)以及发射角度(firing angel)，考虑空气阻力以及空气密度随着高度的影响的情况下，展示出炮弹发射至落地的运动轨迹；

2.确定能给出最大X轴距离的发射角度。

##· 背景介绍 ##
定义类flight_state用于存储每一时刻的飞行状态，包括水平、垂直位置x、y，水平、垂直速度v_x，v_y，时刻t。

参考教材，有

![](http://i.imgur.com/2kX0sby.jpg)

其中，g = 9.8，B2/m = 4e-5。

T0为海平面的温度，由查找可知，国际标准化组织规定了标准海平面温度为15℃，即288.15K。

考虑到方程没有解析解，于是根据欧拉法递推确定下一时刻的飞行状态，直到y小于等于0。dt设为0.1。

同时，对落点的取值进行了修正，取了在地面上的最后一个点以及在地面下的第一个点对于对应距地距离比值的加权算术平均。

##· 正文 ##

**1.重现Figure 2.5 的图像**

下面我们运行程序[Cannon Shell for drawing with input of v and angle ](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%202/Cannon%20Shell%20for%20drawing%20with%20input%20of%20v%20and%20angle%20.py)

来完成Figure 2.5图像的重现

Figure 2.5的初始条件为V0=700，角度分别的35度和45度。

现在我们分别输入700，35和700，45

![](http://i.imgur.com/jhXukXb.png)

![](http://i.imgur.com/59Q6Vij.png)

由于Figure 2.5的虚实分别为有无空气密度随着高度的影响，我的程序的红蓝两条是有无空气阻力以及空气密度随着高度的影响，故应该对比Figure 2.5的实线与我的红线。

现在提出红线来看看是否吻合

![](http://i.imgur.com/WD4CqTb.png)

![](http://i.imgur.com/MbuJbvn.png)



![](http://i.imgur.com/SSn4wiY.png)

![](http://i.imgur.com/OvtbaBd.png)

可以看出，XY的位置与曲线形状都是吻合的



**2.确定能给出最大X轴距离的发射角度。**

下面我们运行程序[Cannon Shell for finding the angle that gives the maximum range](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%202/Cannon%20Shell%20for%20finding%20the%20angle%20that%20gives%20the%20maximum%20range.py)


输入初始速度，比如700

程序通过遍历0到90度，选取最大X距离。


![](http://i.imgur.com/VRkyHhg.jpg)

就可以得到在只有重力作用下，以及加上空气阻力以及空气密度随着高度影响后分别的，能达到的最大X距离和达到该距离的发射角度。

可以看到，在初始速度为700时，只有重力作用下最大距离为50049m，需要的角度为45度；加上空气阻力以及空气密度随着高度影响后，距离为24544m，需要的角度为44度。


**3.进一步研究**

![](http://i.imgur.com/3CttQxS.jpg)

![](http://i.imgur.com/a3A1hDC.jpg)

![](http://i.imgur.com/gRl1i2u.jpg)

![](http://i.imgur.com/bPntrb7.jpg)

可以看出

在初始速度比较小时，有无空气阻力以及空气密度随着高度影响，结果都相近。

随着初始速度变大，风速影响愈加明显。

这与实际情况是相符合的。


##· 结论 ##
通过程序，Figure 2.5的图像得到了重现。

并且找到了给定初始速度下，能得到最大X轴距离的发射角度。

风速对距离的具体影响也与实际情况相符合。

##· 学习笔记 ##
通过这次程序的编写，学会了很多新的python语言的方便用法。在这里写一下理解。

**1.类class**

def函数的高级模式。类似于自己编一个模板
然后后面直接引用，并代入数据就可以了。

**2.全局变量**

在class中定义的量，想在别的地方用（比如想在稍后遍历），就得global一下，把他变成整个程序通用的变量。

**3.遍历**

原来一直用的
for i in range(999):就是遍历，就是扫遍所有取值的一个小循环。

**4.切片**

这个在程序中没有显示了，因为最后发现达不到目的走偏了删掉了，但是我当时研究了好久。

我是多维数组[[i,x[-1]]]，想单独提出x[-1]组成一个数列。

用网上多元数组的切片方式[:,1]，一直报错，说list切片必须是整数，不能是tuple。

最后解决办法是[x[-1] for x in k]。

**5.lambda函数**

这就是避免了在外面又def的繁复，直接在式子里定义一个临时函数lambda x，满足“：”后面的性质。非常方便。

**6.sort函数**

这是python自带的排序函数，可以根据很多条件来进行排序。我这里用的是设定关键词key，这样就可以做到多维数组中根据其中一列来排序了！

##· 致谢 ##
隆重感谢小伙伴陈平涛的耐心讲解。

感谢刘文焘大大的报告，稍有借鉴！

感谢各位无私奉献经验的网络教程大大。

[廖雪峰 Python2.7教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/00138682004077376d2d7f8cc8a4e2c9982f92788588322000)

[python类、对象、方法、属性之类与对象笔记](http://blog.chinaunix.net/uid-22521242-id-4017965.html)

[Python笔记——类定义](http://blog.csdn.net/wklken/article/details/6313265)

[python 里面的单下划线与双下划线的区别(私有和保护)](http://blog.csdn.net/aries5555/article/details/8606246)

[Python自定义函数中，参数后面带了个=0是什么意思？（如图）](http://zhidao.baidu.com/link?url=O20l3aUFeIrzCLy_9LsEuMX9VIPLNeMusoaWcl570bq9xBAH7y4e0pb9xxhyWcwE4LVnEaAHwwdH3gfCkiBzwa)

[Python 类内方法函数的内部变量，命名，加'self.'变成 self.xxx 和不加直接 xxx 有什么区别？](https://www.douban.com/group/topic/49677973/)

[什么是Python的类，方法，对象，实例？](http://zhidao.baidu.com/link?url=nChgdV0vX9weVMxrBMPaZt5REn4ljvoN7vTH12wHapGu5kzbiaP9ng0lFMsjfFx04wzExYI_5vrRuSuqBvn2lq)

[numpy函数：[16]多维数组切片存取](http://jingyan.baidu.com/article/6f2f55a18033aeb5b83e6c41.html)

[“list indices must be integers, not tuple” but it worked before?](http://stackoverflow.com/questions/25498212/list-indices-must-be-integers-not-tuple-but-it-worked-before)

[python中List的sort方法（或者sorted内建函数）的用法](http://gaopenghigh.iteye.com/blog/1483864)

[今天才发现python的sort有个key参数,我好圡.](https://www.douban.com/note/27835755/)
