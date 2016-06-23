#第十次作业#

##· 摘要 ##
本次作业完成了第十次作业，按照课本顺序研究了洛伦兹模型，完成了作业L1 3.26题的实现：

>***在不同的区域(in different regimes)构建Figure 3.16和Figure 3.17的相空间图像。**

regimes我理解为不同坐标，相平面。

##· 背景介绍 ##
由教材，大气物理学家Lorenz在研究Rayleigh-Benard问题时，将流体力学基本方程组Navier-Stokes方程组化简为简单形式： 

![](http://i.imgur.com/5lV3SMR.jpg)

这个方程组被称为Lorenz方程组，或Lorenz模型。其中x,y,z为变量，其余为常数。

遵照惯例，设

sigma=10

b=8/3

##· 正文 ##

####**1.Figure 3.15——Lorentz模型在不同r下的行为**

运行程序[Figure 3.15](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20tenth%20homework/Figure%203.15.py)

改变r的大小，观察z随时间的变化情况。在这个模型中，r代表了流体顶部与底部的温度差，类似于单摆问题中外界驱动力的地位。

![](http://i.imgur.com/sz38pCu.jpg)

可以看到，与Figure3.15完全符合

同时，观察x,y随时间的变化情况

![](http://i.imgur.com/XeztGBN.jpg)

![](http://i.imgur.com/YG2re0W.jpg)

r=5时，图像一开始有一点振荡，随后振幅衰减，x,y,z变成一个与时间无关的常数。

r=10时，图像的特征相似，只是振幅衰减所花的时间要更长一些。

这两种情况对应于流体中的稳定对流运动。它类似于非混沌单摆的运动模式。

r=25时，图像变为混沌状态。

####**2.Figure 3.16——相空间中的混沌lorenz模型**

运行程序[Figure 3.16](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20tenth%20homework/Figure%203.16.py)

首先看x-z平面的

![](http://i.imgur.com/xdYNTtP.jpg)

可以看到，与Figure3.16完全符合

然后是x-y平面的

![](http://i.imgur.com/IZG7XY9.jpg)

然后是y-z平面

![](http://i.imgur.com/7uSXNfK.jpg)

可见 满足Wikipedia “Lorenz system”词条的示意图

![](https://upload.wikimedia.org/wikipedia/commons/1/13/A_Trajectory_Through_Phase_Space_in_a_Lorenz_Attractor.gif)

A sample solution in the Lorenz attractor when ρ = 28, σ = 10, and β = 8/3

非混沌状态（r=5,10）图像会汇聚到一个点，代表系统处于稳定状态。混沌状态（r=25）与混沌摆的情况类似。事实上这个图像非常眼熟——在进行“混沌通信”实验中示波器上显示的就是这样的图像。



####**3.Figure 3.17——相空间中的混沌lorenz模型**

运行程序[Figure 3.17](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20tenth%20homework/Figure%203.17.py)


这里x=0,y=0的条件由x,y绝对值≤0.01代替

![](http://i.imgur.com/iBCMu0F.jpg)

可以看到，与Figure3.17完全符合


####**4.Figure 3.18——混沌转变**

运行程序[Figure 3.18](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20tenth%20homework/Figure%203.17.py)

![](http://i.imgur.com/zlFLvDg.jpg)

![](http://i.imgur.com/3ceU626.jpg)

与Figure 3.18相吻合。

r=160，系统是周期性的。

r=163.8，系统开始出现一些非周期的因素，也就是开始变得混沌。

不过这里并不太明白与同样条件的Figure 3.15讨论的区别，为什么随着r增加，先出现非周期性（混沌状态），然后出现周期性，最后又出现非周期性（混沌状态）？

![](http://i.imgur.com/sz38pCu.jpg)



##· 结论 ##

①改变r的大小，观察z随时间的变化情况。在这个模型中，r代表了流体顶部与底部的温度差，类似于单摆问题中外界驱动力的地位。

r=5时，图像一开始有一点振荡，随后振幅衰减，x,y,z变成一个与时间无关的常数。

r=10时，图像的特征相似，只是振幅衰减所花的时间要更长一些。

这两种情况对应于流体中的稳定对流运动。它类似于非混沌单摆的运动模式。

r=25时，图像变为混沌状态。

r=160，系统是周期性的。

r=163.8，系统开始出现一些非周期的因素，也就是开始变得混沌。

似乎随着r增加，先出现非周期性（混沌状态），然后出现周期性，最后又出现非周期性（混沌状态）。

具体原因有待进一步研究

②非混沌状态（r=5,10）的相空间混沌图像会汇聚到一个点，代表系统处于稳定状态。混沌状态（r=25）与混沌摆的情况类似。


##· 学习笔记 ##

**from __future__ import division**

在进行4.Figure 3.18——混沌转变时，出现了r=160和r=163.8都混沌的情况

![](http://i.imgur.com/qDAWKjL.jpg)

与同学的代码对比发现，同学多了一个
from __future__ import division 模块

给自己的代码添上后就好了。

![](http://i.imgur.com/zlFLvDg.jpg)

百度得知，from __future__ import division的意思是

导入python未来支持的语言特征division(精确除法)，当我们没有在程序中导入该特征时，"/"操作符执行的是截断除法(Truncating Division),当我们导入精确除法之后，"/"执行的是精确除法，如下所示：


[in] 3/4

[out] 0

[in] from __future__ import division

[in] 3/4

[out] 0.75



导入精确除法后，若要执行截断除法，可以使用"//"操作符：

[in] 3//4

[out] 0


不过方程组的右边好像没出现除法啊

![](http://i.imgur.com/5lV3SMR.jpg)

不太明白是哪里影响的机制。


##· 致谢 ##

感谢吴雨桥同学，借鉴了代码与报告。
