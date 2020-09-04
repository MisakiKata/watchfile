import pyinotify
import datetime
import configparser
import socket
from lib.semail import sendemail
from lib.scan import hmscan
import os

config = configparser.ConfigParser()
config.read('config.ini')
dirlist = config['DIR']['dir']
logfile = config['LOG']['log']
email = config['EMAIL']
scan = config['SCAN']
hostname = socket.gethostname()

def process_time():
    return datetime.datetime.now().__format__('%Y-%m-%d %H:%M:%S')

def Modifica(event):
    message = 'okok'
    data = {'hostname':hostname, 'time':process_time(), 'filename': str(event.name), 
        'maskname':str(event.maskname), 'filepath':str(event.pathname)}
    movefile = hmscan(scan, str(event.pathname))
    if movefile:
        if movefile == 'nosave':
            # message = "文件结果移动失败"
            movefile = os.getcwd()+'/lib/null2.csv'
            if sendemail(data, movefile):
                message = '邮件发送成功'
            else:
                message = '邮件发送失败'
            
        else:
            # message = '文件结果移动成功'
            if sendemail(data, movefile):
                message = '邮件发送成功'
            else:
                message = '邮件发送失败'
    else:
        # message = '文件扫描失败'
        movefile = os.getcwd()+'/lib/null.csv'
        if sendemail(data, movefile):
            message = '邮件发送成功'
        else:
            message = '邮件发送失败'

    print(message)


class Log(pyinotify.ProcessEvent):
    def my_init(self, event):
        self._fileobj = open(logfile, 'a')
        
    def process_default(self, event):
        self._fileobj.write(str(process_time())+'--'+str(event) + '\n')
        self._fileobj.flush()
        self._fileobj.close()

class TrackModifications(pyinotify.ProcessEvent):
    def process_IN_MODIFY(self, event):
        event.maskname = '文件修改'
        if event.wd == -1:
            return False
        if event.dir == False:
            Modifica(event)

    def process_IN_CREATE(self, event):
        event.maskname = '新建文件'
        if event.wd == -1:
            return False
        if event.dir == False:
            Modifica(event)

class Identity(pyinotify.ProcessEvent):
    def process_default(self, event):
        print(event.maskname)
        hand = TrackModifications(Log(event=event))
        hand(event)

for ds in dirlist.split(','):
    try:
        wm = pyinotify.WatchManager()
        s1 = pyinotify.Stats()
        notifier = pyinotify.ThreadedNotifier(wm, default_proc_fun=Identity(s1))
        notifier.start()
        wm.add_watch(ds.strip(), pyinotify.IN_MODIFY|pyinotify.IN_CREATE, auto_add=True)
        print('Start......')
    except:
        notifier.stop()
        
