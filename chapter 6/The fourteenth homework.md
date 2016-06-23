#第十四次作业#

##· 摘要 ##
本次作业完成了第十四次作业，完成了作业6.6题的要求：

>***6.6 证明波包不会被相互碰撞而影响，即两个波包会穿过彼此而不发生形状与速度的改变**

##· 背景介绍 ##
由波动方程

![](http://i.imgur.com/DyBhRqN.png)

一维情况时，y代表弦上各点相对于其平衡位置的位移，x代表各点在弦上的坐标，t代表时间，c代表波在弦上的传播速度。

固定边界条件，即边界处y=0，用迭代方法逐步求解绳波随时间的演化：

![](http://i.imgur.com/UlsYgUz.jpg)

初始时刻在弦上施加两个高斯型的干扰，选择弦长为1m，c=300m/s，dx=0.01m，dt=dx/c，则r=c*dt/dx=1

初始波形为

![](http://i.imgur.com/k42KVJc.png)

选取x0=0.3m和0.7m，k=1000m^(-2)。

齐次线性偏微分方程的一个重要特征是有限个解的线性组合也是方程的解，故在弦上运动的两个波包的运动是独立的，应看到两个波包会穿过彼此而不发生形状与速度的改变的现象。

##· 正文 ##

####6.6 证明波包不会被相互碰撞而影响，即两个波包会穿过彼此而不发生形状与速度的改变

运行程序[wave.py](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%206/The%20fourteenth%20homework/wave.py)

观察初始位置在0.3m和0.7m处波包的后续运动。

![](http://i.imgur.com/N8hL3Lk.gif)

可以看到，首先初始是0.3m和0.7m位置的两个波

![](http://i.imgur.com/DHj2EgC.jpg)

高斯型的干扰变为了两个相反方向的波传播，这两个波的峰值为原干扰的一半。且当其传播到了边界点时，波峰变为波谷，波谷变为波峰，这直接对应于物理中的半波损失，即波从光疏介质传播到光密介质时相位会减少180°。

![](http://i.imgur.com/PCQK2lG.jpg)

![](http://i.imgur.com/Vk7CPSE.jpg)

发生碰撞合成峰值是两波峰之和的一个峰。

![](http://i.imgur.com/PlD77dq.jpg)

然后分开，并不改变形状与速度。

![](http://i.imgur.com/ZgU7irF.jpg)

![](http://i.imgur.com/6bhi1wa.jpg)

得证。

##· 结论 ##

高斯型的干扰变为了两个相反方向的波传播，这两个波的峰值为原干扰的一半。且当其传播到了边界点时，波峰变为波谷，波谷变为波峰，这直接对应于物理中的半波损失，即波从光疏介质传播到光密介质时相位会减少180°。

发生碰撞合成峰值是两波峰之和的一个峰。然后分开，并不改变形状与速度。

##· 学习笔记 ##
由于本单元使用了python的动图制作这个原来没学过的内容，本章在书写时较多的参考了其他同学的代码，对自己贫乏的编程能力进行了恶补。

1.

line, = ax.plot([],[],lw=2)

line.set_data（x,y）

将x,y数据打包成了一条线，然后统一输出为数据line

其中lw为浮点数个数，即小数点后几位


2.animation.FuncAnimation（fig, animate, init_func=init, frames=200, interval=5）

画动图的函数。

使用前首先要从模块里拿到动图模块

from matplotlib import animation

init_func=init是初始线函数
其中animate是运动后的线函数
frames参数,指的读写的参数，不写的话，framenum会从1一直增加下去直到无穷
interval参数指的区间为5个

##· 致谢 ##


感谢吴雨桥、刘文焘、陈洋遥同学，借鉴了代码与报告。

感谢网络教程[matplotlib绘制动画的示例](http://blog.csdn.net/rumswell/article/details/11731003)