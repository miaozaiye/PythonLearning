#!-*- coding = utf-8 -*-
#linqiliang_fd@163.com

1\ bacpypes 暂停，使用bac0 基于py3 实现基本的通讯模拟
2、要完成bac0 的模拟，必须安装相关bac0 的包，step1 需要进行python 3 安装，step2 bac0 安装 
3、运行相关的示范代码
4、细节
  确定运行哪个代码？
  做到何种程度算完成模拟？
            可以修改属性，可以读取属性
  可以深入一步么？

  bac0 的好处是啥？
    
  bac0 除去bac0 有其他的替代方案么？

5、第一步： 1.device IP： 192.168.0.10 subnetmask 255.255.0.0 gateway 192.168.0.1
            2.workstation：192.168.0.11 subnetmask： 255.255.0.0
            3.Networknumber：2000  anything betweet 1 to  0xFFFE
            4.Device identifier:1000,workstation :1001
            5.Device name: anything is ok
            6.Maximum APDU Lenth accetped:
            7.segmentation supported A:
    第二步：
            
            使用Example进行实例代码操作，使用模拟器和wireshark 可以查看实际的通信
            记住一点，10048 错误是端口被占用的意思，要注意


