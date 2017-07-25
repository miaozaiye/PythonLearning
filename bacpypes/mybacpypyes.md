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

代码已经可以运行
1、学习使用cmd命令
看Samplecmd.py
第一步先建立设备
    this_device = LocalDeviceObject(
        objectName=args.ini.objectname,
        objectIdentifier=int(args.ini.objectidentifier),
        maxApduLengthAccepted=int(args.ini.maxapdulengthaccepted),
        segmentationSupported=args.ini.segmentationsupported,
        vendorIdentifier=int(args.ini.vendoridentifier),
        )

class SampleApplication(BIPSimpleApplication):

    def __init__(self, device, address):
        if _debug: SampleApplication._debug("__init__ %r %r", device, address)
        BIPSimpleApplication.__init__(self, device, address)

    def request(self, apdu):
        if _debug: SampleApplication._debug("request %r", apdu)
        BIPSimpleApplication.request(self, apdu)

    def indication(self, apdu):
        if _debug: SampleApplication._debug("indication %r", apdu)
        BIPSimpleApplication.indication(self, apdu)

    def response(self, apdu):
        if _debug: SampleApplication._debug("response %r", apdu)
        BIPSimpleApplication.response(self, apdu)

    def confirmation(self, apdu):
        if _debug: SampleApplication._debug("confirmation %r", apdu)
        BIPSimpleApplication.confirmation(self, apdu)


@bacpypes_debugging
class SampleConsoleCmd(ConsoleCmd):
     
    my_cache= {}
    def do_nothing(self, args):
        """nothing can be done"""
        args = args.split()
        if _debug:
            SampleConsoleCmd._debug("do_nothing %r", args)

    def do_set(self, arg):
        """set <key> <value> - change a cache value"""
        if _debug: SampleConsoleCmd._debug("do_set %r", arg)
        key, value = arg.split()
        self.my_cache[key] = value

    def do_del(self, arg):
        """del <key> - delete a cache entry"""
        if _debug: SampleConsoleCmd._debug("do_del %r", arg)
        try:
            del self.my_cache[arg]
        except:
            print(arg, "not in cache")

    def do_dump(self, arg):
        """dump - nicely print the cache"""
        if _debug: SampleConsoleCmd._debug("do_dump %r", arg)
        print(self.my_cache) 

#简单的cmd命令应用和简单的BIPSimpleApplication

        添加指令很简单，继承ConsoleCmm，然后使用do_"cmd"方法，可以使用共有变量来协调

20170725 
IOCB
IOCBcontroler 
1疑问： icop和ICOBcontrol
没有目标地址，他是往哪里发送IOCB了?
IOCB 不仅仅包含基本信息，还有回调方法

每一个IOCB还可以进行基本的线程等待；

20170726 HandsonSample
1、例子1，简单app
可以通过App模拟一个设备，不需要使用设备模拟器，可以自己写模拟器，通过两者通讯来试验代码；
基本就是一个SimpleApplication 类，在类里面进行基本的 request response confirm indication等功能


