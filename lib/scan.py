import subprocess
import os
import shutil

#pathname:传入的文件路径名  filedir:设置的目录地址
def filesave(pathname, filedir):
    f = os.path.split(pathname)
    path,name = f[0], f[1]
    movefile = filedir+path+'/'+name+'.csv'
    try:
        if os.path.exists(filedir+path):
            shutil.move(os.getcwd()+'/lib/shellpub/result.csv', movefile)
            return movefile
        else:
            os.makedirs(filedir+path)
            shutil.move(os.getcwd()+'/lib/shellpub/result.csv', movefile)
            return movefile
    except:
        False

#是否生成文件
def filexist():
    file = os.getcwd()+'/lib/shellpub/result.csv'
    if os.path.exists(file):
        return True
    else:
        return False

def hmscan(hm, path):
    hmfile, scan, scandir = hm['hm'], hm['scan'], hm['scandir']
    sub = subprocess.Popen([hmfile, scan, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='utf-8')
    sub.wait()
    if sub.poll() == 0:
        if not filexist():
            return False
        movefile = filesave(path, scandir)
        print(movefile)
        if movefile:
            return movefile
        else:
            return 'nosave'
        
        # return True
    else:
        out, err = sub.communicate()
        return False

