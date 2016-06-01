#第九次作业#

##· 摘要 ##
本次作业完成了第九次作业，重现了课本的研究过程，并使用欧拉法完成了3.12题的实现：

>***研究庞加莱截面在不同外力相位取值时的情况，与Figure 3.9进行比较。**
>
##· 背景介绍 ##
上一次的作业中讨论了线性、强迫力以及摩擦这三种因素是如何分别作用于简单单摆并影响其运动轨迹的。

本次作业将讨论同时考虑这三种因素的单摆，也就是所谓的物理摆。

物理摆有许多性质与简单单摆一致，但是也有很多自身独有的奇特性质。其中最重要的可能就是所谓的混沌现象。

由教材
式（3.18），（3.19）

![](http://i.imgur.com/qGFX3n3.jpg)

其中,设置

g=9.8

l=9.8

q为摩擦系数

F_d为强迫力

Ω_d为强迫角频率

##· 正文 ##

####**1.不同驱动力下物理摆的运动**

运行程序

[study on the figure 3.6 of angle](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20ninth%20homework/study%20on%20the%20figure%203.6%20of%20angle.py)

[study on the figure 3.6 of omega](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20ninth%20homework/study%20on%20the%20figure%203.6%20of%20omega.py)


![](http://i.imgur.com/WhCwlOM.jpg)


![](http://i.imgur.com/HKnfkT8.jpg)


我也不知道为什么30s后就跟Figure 3.6不一样了。我跟其他做出来图像的同学对比过程序并没发现不同。


图中蓝色线表示Force=0的状态，可见没有外界驱动力下的单摆在阻力的影响下很快就停止了。

图中红线表示Force=0.5时的运动，可见单摆在开始阶段将初始条件决定的运动通过阻力消耗后，在之后的运动中做与外力同频率的简谐振动。

这两种单摆的运动与上一篇文章中描述的一样。

绿色的线表示Force=1.2时的运动状态，可以看到，单摆的运动是没有周期性的，这就是混沌的特征。图中竖直的线是由于当角度超过180度时，程序将其角度自动减小360度，反之亦然。

####**2.混沌摆对初值的敏感性**

混沌摆的最大特征是当初值仅仅改变了一点点时，结果就会有极大的变化。为了示意这种情况，选择两个摆，它们的初始角度仅仅相差0.001rad。之后观察它们分别在F=1.2（混沌）和F=0.5（非混沌）的情况下角度之差的变化规律。

运行程序[study on the figure 3.7](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20ninth%20homework/study%20on%20the%20figure%203.7.py)

![](http://i.imgur.com/Mmeb7wr.jpg)

蓝线为Force=0.5的情况。由图可知，对于两个初始位置差异很小的非混沌摆，其角度差会迅速减小，最终趋于0.这表明非混沌摆对初值不敏感。

绿线为Force=1.2的情况。由图可知，在混沌状态下，初始角度相差极小的两个物理摆的角度差随着时间推移会变大，最终趋于稳定。

####**3.混沌摆的角度与角速度的关系**

运行程序[study on the figure 3.8](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20ninth%20homework/study%20on%20the%20figure%203.8.py)


![](http://i.imgur.com/XzlumrV.jpg)

图像与Figure 3.8完美符合

蓝线为Force=0.5，即非混沌情况下单摆的角度与角速度的关系。由图可见，除开最初的一段线，这关系基本上是一个椭圆，这表明对应每一个角度由两个角速度，反之亦然。最终的轨迹与初始值无关，这与上面的结论相合，也是符合简谐振动的规律的。

绿线为Force=1.2，即混沌情况下的单摆的角度与角速度的关系。这里的图像明显比非混沌情况要复杂，但可以明显看出图像上的点并不是随机的，其中有一定的规律性。混沌系统一般都会显示这类的规律性。 


####**4.exercise 3.12 研究庞加莱截面在不同外力相位取值时的情况，与Figure 3.9进行比较。**

运行程序[exercise 3.12](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/chapter%203/for%20the%20ninth%20homework/exercise%203.12.py)


![](http://i.imgur.com/NuzcmNW.jpg)

Figure 3.9为t=驱动力周期倍数的时刻的情况

excise 3.12对t为不同外力相位的情况进行了讨论

可以看到，随着相位从0到pi/4再到pi/2，图像明显逐渐移动

##· 结论 ##

数值分析表明，混沌图像有一定规律性。参数的变化对混沌状态有较大影响，且混沌摆角度对初值依赖性也很大。庞加莱截面在不同外力相位取值时的情况下，逐渐移动。

##· 致谢 ##

感谢吴雨桥同学，借鉴了代码与报告。
