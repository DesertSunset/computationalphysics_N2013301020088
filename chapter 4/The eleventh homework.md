#第十一次作业#

##· 摘要 ##
本次作业完成了第十一次作业，完成了作业4.7 4.9题的实现：

>***4.7 研究在质量相同与不同情况下的双星系统轨道**

>***4.9 研究在beta值不为2时，不同初速度导致的轨道近圆程度对轨道行为稳定性的影响**


##· 背景介绍 ##
万有引力公式

![](http://i.imgur.com/T2KE2sq.png)

由书本设定其中一个行星质量远大于另一个，于是固定位置，由另一个行星绕之运动的公式推导

![](http://i.imgur.com/JzeElZN.jpg)

![](http://i.imgur.com/g01urvh.jpg)

![](http://i.imgur.com/9epeVMY.jpg)

取GM为4Pi方，得到欧拉法递推公式

![](http://i.imgur.com/RBapeFo.jpg)


双星系统初始瞬间在相互引力作用下欲进行稳定的圆周运动，可推导初始速度

![](http://i.imgur.com/0wyZEe9.jpg)

那么在设定质量比K的情况下，便可以通过欧拉公式求得双星运动轨道

##· 正文 ##

####4.7 研究在质量相同与不同情况下的双星系统轨道**

运行程序

**①质量相同**

k=1 

![](http://i.imgur.com/SPvLj61.jpg)

**②质量不同**

k=2

![](http://i.imgur.com/J1QnWCt.jpg)

k=5

![](http://i.imgur.com/fOSrp2o.jpg)

k=15

![](http://i.imgur.com/DgdIjrh.jpg)

k=25

![](http://i.imgur.com/pqekK1R.jpg)

k=31

![](http://i.imgur.com/ne4lnmT.jpg)

k=32

![](http://i.imgur.com/HLvfifs.jpg)

k=100
![](http://i.imgur.com/AXgtN0S.jpg)

**可以看出，随着k逐渐变大，逐渐不能维持椭圆稳定轨道，大质量行星运行速度逐渐变慢，运动轨迹变小，小行星运动速度加快，逐渐挣脱引力轨道束缚，最终扬长而去。**

**③当大行星质量远大于小行星时**

取总动量为0，即可得到大行星类似固定不动质量下降，小行星围绕大行星运动的简化模型。

运行程序

令大行星初始速度为0，小行星自取。

V0=pi

![](http://i.imgur.com/YUadfcw.jpg)

V0=2pi

![](http://i.imgur.com/FDyiWtD.jpg)

V0=3pi

![](http://i.imgur.com/971t7KZ.jpg)

**可见V0=2pi时做圆周运动。v0过大时，离心力大于引力，小行星挣脱束缚。这与现实情况相符合。**


####4.9 研究在beta值不为2时，不同初速度导致的轨道近圆程度对轨道行为稳定性的影响**

运行程序

**①beta值对图像的影响**

V0=1pi

![](http://i.imgur.com/QvYZF3d.jpg)

V0=1.5pi

![](http://i.imgur.com/pgimFcf.jpg)

V0=2pi

![](http://i.imgur.com/ipSxhJ7.jpg)

**V0=1.5Pi时图像与课本一致，可见课本图像的初始速度应该在1.5Pi左右**

课本

![](http://i.imgur.com/riz26E5.png)

![](http://i.imgur.com/q9b76Gb.png)

![](http://i.imgur.com/IA2tu9K.png)

**V0=2Pi时各曲线几乎重合，说明在最近似圆周运动时，轨道稳定性最好**

**②初速度对图像的影响**

运行程序

当beta=2.05时改变初始速度

![](http://i.imgur.com/iInEAyj.jpg)

**可见仍然是最近似圆周运动时稳定性最好。与题干结论一致。**

##· 结论 ##

**4.7 研究在质量相同与不同情况下的双星系统轨道**

随着k逐渐变大，逐渐不能维持椭圆稳定轨道，大质量行星运行速度逐渐变慢，运动轨迹变小，小行星运动速度加快，逐渐挣脱引力轨道束缚，最终扬长而去。

在大行星质量远大于小行星时，固定大行星不动，形成太阳系模型，V0=2pi时做圆周运动。v0过大时，离心力大于引力，小行星挣脱束缚。这与现实情况相符合。

**4.9 研究在beta值不为2时，不同初速度导致的轨道近圆程度对轨道行为稳定性的影响**

最近似圆周运动时稳定性最好。与题干结论一致


##· 致谢 ##

感谢吴雨桥、刘文焘、张琦同学，借鉴了代码与报告。