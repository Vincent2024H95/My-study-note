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
  ```

- 在使用这些命令的时候会出现一个弹窗，内容是什么我也不清楚，全英文看不懂，我也懒得翻译，当时我很疑惑，因为我在安装蓝色版本的kali和早期紫色版本的kali时是没有这个弹窗的，我就不理解，后来键盘一顿乱按也就跳过了这个弹窗，就没有理会。

- 弹窗是这样的：![image-20241030111302283](C:\Users\heng\AppData\Roaming\Typora\typora-user-images\image-20241030111302283.png)

  我选择了no

  2.**设置root用户登陆，更改中文，安装中文输入法**