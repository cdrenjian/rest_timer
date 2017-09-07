#-*-coding:utf-8-*-
from  Tkinter import *
import subprocess
from time import strftime,gmtime
import time
from datetime import datetime
import tkMessageBox,os
import threading
def  delay(t):
    e = threading.Thread(target=time.sleep, args=(t,))
    e.start()
    while e.is_alive()==True:
        pass
class  Exe:
    def __init__(self,pos):
        self.pos=pos           #获得执行文件路径
        print self.pos
        self.name=pos.split("/")[-1]    #获得程序名
    def startctrl(self):
        e=threading.Thread(target=self.start)
        e.start()
    def start(self):
        try:
            subprocess.check_output(self.pos,shell=True)
            print"运行成功"
        except:
            tkMessageBox.showwarning("message", "未找到正确的执行程序，请检查路径")
    def destroy(self):
        try:
            print "开始停止"
            subprocess.check_output("taskkill /f /im "+self.name, shell=True)
            print "成功停止"
        except:
            tkMessageBox.showwarning("message", "停止执行程序失败！")
class app(Frame):
    def __init__(self,master=None):  #主框架初始化
        Frame.__init__(self,master)
        self.pack()
        self.CreatWidgets()
    def CreatWidgets(self):
        self.jg=Label(self,text="时间间隔")
        self.jg.pack()
        self.h=Entry(self)
        self.h.pack()
        self.h.insert(0,"60")
        self.lj = Label(self, text="休息播放音乐程序路径")
        self.lj.pack()
        self.l = Entry(self)
        self.l.pack()
        self.sc= Label(self, text="休息时长")
        self.sc.pack()
        self.s= Entry(self)
        self.s.insert(0, "10")
        self.s.pack()
        self.l.insert(0, "D:\CloudMusic\cloudmusic.exe")
        self.b=Button(self,text="确定计时",command=self.jishi)
        self.b.pack()
    def jishi(self):  #点击button事件的处理函数
        t = self.h.get()
        t=int(t)*60
        s = self.s.get()
        s=int(s)*60
        l=self.l.get()
        l=l.replace("\\","/")
        print type(l)
        print l
        if l:
            exe=Exe(l)
        tkMessageBox.askyesno("message", "设置成功！马上开始计时！")  # 阻塞型消息框
        while 1:
            delay(t)
            while tkMessageBox.askyesno("message", "已经久坐多时了！快休息一下.")==False:
                tkMessageBox.showwarning("message", "必须休息一下！")
            exe.startctrl()
            delay(s)
            exe.destroy()
            while  tkMessageBox.askyesno("message", "休息够了？")==False:
                exe.startctrl()
                delay(300)
                exe.destroy()
a=app()
a.master.title("定时提醒小程序")
a.master.geometry('350x250')
a.master.wm_attributes('-topmost',1)
a.mainloop()