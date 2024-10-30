**安装Kali Linux后的一些基本操作**

------

1. **更新国内源**

- 获取最高权限：sudo -i

- 编辑软件源配置：vim /etc/apt/sources.list

- 点击“i”键进入编辑状态，”#“注释掉原来的源地址

- CTRL+shift+V粘贴源地址到文件中，先按esc，然后按:wq保存

  ```
  #清华大学
  deb http://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
  deb-src https://mirrors.tuna.tsinghua.edu.cn/kali kali-rolling main contrib non-free
  ```

  ```
  #阿里云
  deb http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
  deb-src http://mirrors.aliyun.com/kali kali-rolling main non-free contrib
  ```

  这里我只列举了两个，因为我一般只用这两个

- 接下来是更新丝滑连招：

  ```
  apt-get update          #更新索引
  apt-get upgrade         #更新软件
  apt-get dist-upgrade    #升级
  apt-get clean           #删除缓存包
  apt-get autoclean       #删除未安装的deb包
  apt-get autoremove      #移除不需要的软件包
  ```

- 在使用这些命令的时候会出现一个弹窗，内容是什么我也不清楚，全英文看不懂，我也懒得翻译，当时我很疑惑，因为我在安装蓝色版本的kali和早期紫色版本的kali时是没有这个弹窗的，我就不理解，后来键盘一顿乱按也就跳过了这个弹窗，就没有理会。

- 弹窗是什么样的，我放在文件夹了，等我学会了怎么把图片在GitHub的md文件正常显示，我再更新。

- 更新：弹窗是这样的：![](https://github.com/Vincent2024H95/My-study-note/blob/78b0228b00fbf4a7637b7eb22e5ed6e1cdbda939/Vincent's%20study%20diary/image/2222.png)

- 解决：这个时候不管你是按空格还是回车都没有用，得摁方向键，但是上下左右我忘了，当时胡乱摁方向键才发现可以

  2.**设置root用户登陆，更改中文，安装中文输入法**

- 当完成第一步的内容后，一定要保存快照，不然出问题了只能重装

- 设置root登录：sudo passwd root

- 然后输入新的密码，保存快照，重启root登录

- 设置中文：

- 前提：已经进行了第一步的操作

  - 安装locales包：sudo apt-get install -y locales
  - 开始设置：sudo dpkg-reconfigure locales
  - 方向键上下或滚轮，找到zh_CN.UTF-8
  - 空格选中，tab键确认
  - 选中zh_CN，依旧是tab键确认，回车
  - reboot

- 有个很恶心的点，不知道为什么，我在root用户下设置中文，重复了很多次，也找了很多方法设置，它就是一直显示中文。它只能在普通用户下才能显示中文，草！

​	