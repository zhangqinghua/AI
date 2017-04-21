# 支持向量机

在很久以前的情人节，大侠要去救他的爱人，但魔鬼和他玩了一个游戏。

魔鬼在桌子上似乎有规律放了两种颜色的球，说：“你用一根棍分开它们？要求：尽量在放更多球之后，仍然适用。”

![img](https://pic2.zhimg.com/5aff2bcdbe23a8c764a32b1b5fb13b71_b.png)

于是大侠这样放，干的不错？ 

![img](https://pic2.zhimg.com/3dbf3ba8f940dfcdaf877de2d590ddd1_b.png)

然后魔鬼，又在桌上放了更多的球，似乎有一个球站错了阵营。

![img](https://pic4.zhimg.com/0b2d0b26ec99ee40fd14760350e957af_b.png)

**SVM就是试图把棍放在最佳位置，好让在棍的两边有尽可能大的间隙。**

![img](https://pic2.zhimg.com/4b9e8a8a87c7982c548505574c13dc05_b.png)

现在即使魔鬼放了更多的球，棍仍然是一个好的分界线。

![img](https://pic4.zhimg.com/7befaafc45763b9c4469abf245dc98cb_b.png)

然后，在SVM 工具箱中有另一个更加重要的 **trick**。 魔鬼看到大侠已经学会了一个trick，于是魔鬼给了大侠一个新的挑战。

![img](https://pic4.zhimg.com/558161d10d1f0ffd2d7f9a46767de587_b.png)

现在，大侠没有棍可以很好帮他分开两种球了，现在怎么办呢？当然像所有武侠片中一样大侠桌子一拍，球飞到空中。然后，凭借大侠的轻功，大侠抓起一张纸，插到了两种球的中间。

![img](https://pic4.zhimg.com/55d7ad2a6e23579b17aec0c3c9135eb3_b.png)

现在，从魔鬼的角度看这些球，这些球看起来像是被一条曲线分开了。

![img](https://pic3.zhimg.com/e5d5185561a4d5369f36a9737fc849c6_b.png)

再之后，无聊的大人们，把这些球叫做 **「data」**，把棍子 叫做 **「classifier」**, 最大间隙trick 叫做**「optimization」**， 拍桌子叫做**「kernelling」**, 那张纸叫做**「hyperplane」。**

![www.youtube.com/watch%3Fv%3D3liCbRZPrZA]()