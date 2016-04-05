#第四次作业#

##· 摘要 ##

折腾了这么久没动静，总得交点东西告诉助教老师进展啊。

于是即使没觉得完成了，还有很多地方想补充，也决定把这篇报告开个头！

第四次作业要求完成第一章的练习题（自己任选一题），于是我选择了1.3摩擦力这道题来小试牛刀。

##· 背景介绍 ##

首先尝试去重现课本例题，衰变曲线。课本范例运用的原理通俗讲就是设定dt，然后前一步得到的点变成后一步的初始点这样，一步步推进，去找点画线。

看了老师上传的uranium decay的范例后，把看得懂的代码提炼出来，就完成了重现。

[例题裂变曲线](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/study/git/chapter1/uranium_decay.py)

![](http://i.imgur.com/Tpw1rcO.jpg)

其中

**n_uranium**是粒子初始总数，设定的是一个list，然后往里面添加（.append）的形式。

**t**是经过的时间，同样是个list，初始值为0。

**tau**为时间常数，仔细对比衰变公式，其值其实对应的是半衰期的-1/ln2倍，一般定义为“平均寿命”的含义。

**dt**是步长，每走一步间隔多长时间。

**n**是走了几步。

然后添加输入值。

最后网上查找Co元素的半衰期为5.27年，设初始有1000个粒子，代入数据得到的图像是这样的。
![](http://i.imgur.com/l5AtLms.jpg)


然后用老师的程序运行出来是这样的
![](http://i.imgur.com/euXDAjO.jpg)

基本无差别啊，自己写的第一个程序成功绘图还是蛮开心的~~~~（虽然基本上就是copy的老师的代码...）


**老师的代码中，有一些地方并不懂所以删掉了：**

1，pickle 应该是自动形成文本保存数据的，又是插件什么什么的，觉得只是纯画图试试，没必要就先删掉了

2，global 是全局变量，这是老师上课强调一定要有的，但是为什么我也没太听懂，网上查的教程也是晕乎乎的，最后自己的程序没加上这个也没啥问题。

3，这里不太懂为什么老师要弄几个def initialize,def calculate，然后还有return 0。直接按我代码那样不是更简洁吗？

4，mfile，又read应该也是保存数据到文档，然后读取文档再画图的，我也没弄懂，就没加上去

5，plot里面的'--*'也不知道是干啥的，从老师的说明看好像是扫描的意思？但是不加的话就运行不出来，所以最后还是战战兢兢的加上了。

6，savefig应该是保存为图片的意思，这个我后来也老代码错误就也删掉了

7，show（）展示图片，保留了。read（）也不明白，删了似乎也没什么。

总之浑浑噩噩的完成了重现....


##· 正文 ##
#### 1.3题####
1.3较于背景中的例题，差别就是斜率的变化
由
![](http://i.imgur.com/6wwmBhm.jpg)
变成了
![](http://i.imgur.com/cTLhGZu.jpg)

最终表达式变为
![](http://i.imgur.com/6sj9qBG.jpg)

于是

[1.3摩擦力程序](https://github.com/DesertSunset/computationalphysics_N2013301020088/blob/master/study/git/chapter1/frictional_force.py)


可是谁也没想到，依葫芦画瓢只改动了几个式子，得到的图像却完全不一样

![](http://i.imgur.com/LNl9kHv.jpg)
![](http://i.imgur.com/ej5RT7o.png)

print 了一下v，发现数据非常混乱
![](http://i.imgur.com/tEHkv1J.png)


最后问了大神们， 大家都不知道怎么回事，打击非常大...明天上课时问问大家试试。

同时还想根据教程[Matplotlib 教程](http://ju.outofmemory.cn/entry/92100)去学习怎么加图标，坐标什么的。

还要clone老师在课上展示了的同学的代码，去研究一下还能怎么玩。

【所以这个作业还没完结，还要继续做下去】....


#### 装Visual####
上课老师展示的樱桃树深深震撼了我，于是我也去到[http://vpython.org/index.html](http://vpython.org/index.html)网站去按步骤装来玩。

1，首先按要求输入命令
pip install vpython。失败了，说没有pip

2，sudo apt-get install pip试试。说没有这个指令，叫我尝试安装一下python-pip。然后安装成功了！

3，可是再次尝试pip install vpython时又失败了，错误代码SSLError: The read operation timed out

4，百度了一下发现是要翻墙，也找到了一篇教程[使用国内镜像通过pip安装python的一些包
](http://www.xuebuyuan.com/1157602.html)

5，输入清华的第一个镜像
pip install vpython -i http://e.pypi.python.org/simple

还是失败了

![](http://i.imgur.com/CDckXQP.jpg)
触目惊心的红色和黄色让我想起了用goagent翻墙的时候各种IP不好用，也是各种红色黄色警报。

6，输入清华第二个镜像
pip install vpython -i http://pypi.v2ex.com/simple

这次是权限不够
could not create '/usr/local/lib/python2.7/dist-packages/vpython': Permission denied

7，sudo pip install vpython -i http://pypi.v2ex.com/simple

本来以为要成功了，然而
NameError: free variable 'install_kernel_spec' referenced before assignment in enclosing scope

这个百度了一下
“当你在一个作用域内为变量赋值的时候，变量会自动被Python当做局部作用域并屏蔽所有外层作用域的同名参数。”
这什么什么的直接让人想放弃治疗了.....

所以还是明天问一下小伙伴吧...

【于是3D的也没装好，双重打击....】

##· 结论 ##
革命尚未成功，同志仍需努力.......


##· 致谢 ##

感谢老师上传的例子！！不然感觉真的不知道怎么动手呢！已经能浅尝到编程运行成功的快乐了啊！

感谢小伙伴陈平涛同学和曹一同学的帮助~

同样感谢网络上大大们详细的教程

[使用国内镜像通过pip安装python的一些包](http://www.xuebuyuan.com/1157602.html)

[Matplotlib 教程](http://ju.outofmemory.cn/entry/92100)
