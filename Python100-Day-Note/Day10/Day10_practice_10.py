#如果使用多线程将耗时间的任务放到一个独立的线程中执行，这样就不会因为执行耗时间的任务而阻塞了主线程，修改后的代码如下所示。

from curses import panel
from faulthandler import disable
import time
import tkinter
import tkinter.messagebox
from threading import Thread



    
def main():
    class DonwloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)
            
    def download():
        #禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        #通过deamon参数将线程设置为守护线程（主程序退出后就不再保留执行）
        #在线程中处理耗时间的下载任务
        DonwloadTaskHandler(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于','作者:linfeiwu')
        
        
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)
    
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel,text='下载',command = download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel,text = '关于', command = show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    
    tkinter.mainloop()

if __name__ == '__main__':
    main()
