# 小女子征战linux的初体验 #

##· 摘要 ##

学习任何一门技术就是一个不断发现问题然后解决然后熟练的过程。

本文件仅用乃记录征战过程，为遇到同样问题的后人提供解决途径。


##· 背景介绍 ##
**因在人群中多看了你一眼，才选了这门课** 

无任何编程基础！！！！！！！！根本看不懂设置！！！！！
学起来好痛苦！！！！！
QAQ只非常喜欢电脑，所以会努力→有信心的。

在第二次上课发现老师用ubuntu展示的，本来就蠢的小女子不跟着依葫芦画瓢似乎并跟不上节奏。于是决定装ubuntu。


##· 正文 ##
#### 装虚拟机 ####
同学直接传的安装包，在网上搜教程按照，一切进展顺利,然后一系列问题来袭
![](http://i.imgur.com/Vrqa9vw.png)

**Question1**
*virtualbox不能为虚拟电脑启动一个新任务*

![](http://i.imgur.com/Vh7eVhz.png)

***尝试1***重装virtualbox
重装了4.3.36版本的，还是跳出这个问题

***尝试2***破解主题
搜错误代码在网上找的了教程1
 [解决Unable to load R3 module ...VBoxDD.dll (VBoxDD):GetLastError=1790](http://www.aixq.com/post-328.html)
下载了他说的破解软件，结果发现自己电脑本来就是未破解状态的
![](http://i.imgur.com/nxktQny.png)

***尝试3***覆盖文件
搜错误代码在网上找的了教程2
 [win7安装virtualbox遇到的问题](http://blog.csdn.net/cuidiwhere/article/details/41893733<) 

发现原因是
宿主机win7用的ghost系统，会破解uxtheme.dll文件，导致virtualbox启动失败

博主给出的解决方案
使用原版的uxtheme.dll替换c:\windows\system32\uxtheme.dll即可。

![](http://i.imgur.com/kgELaTo.jpg)

我以为我的电脑是32位的，下了32位的uxtheme.dll覆盖，然后电脑崩了。
![](http://i.imgur.com/ralEx5G.jpg)
在我以为只能重装时，小伙伴伸出援助之手，通过U盘上的系统打开桌面覆盖回去了原来的。
这次下对了，终于可以正常启动了，同时也发现我是64位系统的要建64位的ubuntu。


**Question2** *安装完virtualbox后，新建虚拟机。类型选择为Linux时，版本下拉选项只有ubuntu 32bit，无ubuntu 64bit。*
![](http://i.imgur.com/VEpmvP2.jpg)

***尝试***

打开了计算机属性，发现自己真的是ghost系统啊。
![](http://i.imgur.com/PKqeQ1j.png)

正好上一个问题的博主同时也写到了这个问题
 [win7安装virtualbox遇到的问题](http://blog.csdn.net/cuidiwhere/article/details/41893733<) 

原因
64 bit 的虚拟机需要硬件虚拟化支持，而BIOS 默认将它关闭了。

解决方案

重启计算机，按F2进入BIOS设置。
在CPU设置下面，将“Intel虚拟化技术”状态设置为打开，保存并退出，重启计算机。再进入virtualbox就可以看到ubuntu 64bit这个选项了。

可是惠普电脑是F2是。。。
![](http://i.imgur.com/AiGXerA.jpg)

原来惠普的BIOS设置在F10
![](http://i.imgur.com/xTQoEIs.jpg)

**挂上ubuntu系统的镜像ios，终于！！！！！！**
![](http://i.imgur.com/DKDCJrj.jpg)


**Question3** *默认情况下 ubuntu 的分辨率最高只能设到800x600，窗口太小*

***尝试***

在网上又找到了教程
[VirtualBox虚拟机 Ubuntu分辨率太小的解决方案](hhttp://blog.csdn.net/yasi_xi/article/details/42388119)

使用VirtualBox的增强功能调好了。 


#### 装XSHELL ####
为了方便的不带电脑上课，选择了装XSHELL远程连接ubuntu系统

在安装过程中遵循小伙伴的指导，在此致谢！
[wdwycpt/computationalphysics_N2013301020128](https://github.com/wdwycpt/computationalphysics_N2013301020128)
![](http://i.imgur.com/PkWXLlR.jpg)
这是拿到连接我github账号的图片


#### 装贺翀师兄写的vim插件Thesaurus Query ####

安装Vundle
[https://github.com/VundleVim/Vundle.vim](https://github.com/VundleVim/Vundle.vim)

安装Thesaurus Query
[https://github.com/Ron89/thesaurus_query.vim](https://github.com/Ron89/thesaurus_query.vim)
![](http://i.imgur.com/EcI8GZS.png)

点赞
![](http://i.imgur.com/3Z6Eyfc.jpg)


##· 结论 ##
小白通过不懈的询问与查找，终于大概弄清楚了一些专有名词的含义与联系，在此谈谈自己的接地气的理解。

#### 关于Github ####
非常喜欢这篇科普文
[知乎：怎样使用 GitHub？](http://www.zhihu.com/topic/19566035/top-answers)
其中配图非常形象的说明了Github的运行方式
![](http://i.imgur.com/YVwdRLQ.png)

简单来说，需要输入命令行的就是

0、本机与github通过SSH key建立连接

1、在github上创建项目

2、使用git clone https://github.com/xxxxxxx/xxxxx.git克隆到本地

3、编辑项目

4、git add +文件名

5、git commit -m "提交说明"

6、git push origin master 将本地更改推送到远程master分支。

这样你就完成了向远程仓库的推送。 

如果在github的remote上已经有了文件，会出现错误。此时应当先pull一下，即：

git pull origin master

然后再进行：

git push origin master


#### 关于VIM与语法 ####

语法即python,markdown....

VIM就像word文档，而语法就是写在word里的文字指令，写好后保存，用python播放出指令对应的效果。
比如python就像是flash播放器，你可以用flash的指令来制作视频，也可以用flash来播放你制作的视频。
而markdown的语言更方便漂亮的排版文字，python更适合编程动起来。


##· 致谢 ##
首先也是最想感谢的就是小伙伴陈平涛同学的耐心教导！
[wdwycpt/computationalphysics_N2013301020128](https://github.com/wdwycpt/computationalphysics_N2013301020128)


感谢曹一同学的软件推荐！


感谢网络上大大们详细的教程

[win7安装virtualbox遇到的问题](http://blog.csdn.net/cuidiwhere/article/details/41893733<) 

[VirtualBox虚拟机 Ubuntu分辨率太小的解决方案](hhttp://blog.csdn.net/yasi_xi/article/details/42388119)

[知乎：怎样使用 GitHub？](http://www.zhihu.com/topic/19566035/top-answers)

最后感谢蔡老师带我走进了这个神奇的世界，要是上课能讲的再小白一点就好了：>

