<h1 align="center">Welcome to watchfile 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.2-blue.svg?cacheSeconds=2592000" />
  <a href="#" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/badge/License-MIT-yellow.svg" />
  </a>
</p>

> 一个基于inotify的Linux文件实时监控程序，同时调用河马扫描来检测文件。程序在python3下运行

## 安装

```sh
#第三方库
pip install pyinotify

#使用supervisor来守护进程
apt-get install supervisor
yum install supervisor
```

## 使用

```sh
#安装完成后需要启动，按需要修改配置文件
supervisord -c /etc/supervisor/supervisord.conf

#配置文件例子
; supervisor config file

[unix_http_server]
file=/var/run/supervisor.sock   ; (the path to the socket file)
chmod=0700                       ; sockef file mode (default 0700)

[supervisord]
logfile=/var/log/supervisor/supervisord.log ; (main log file;default $CWD/supervisord.log)
pidfile=/var/run/supervisord.pid ; (supervisord pidfile;default supervisord.pid)
childlogdir=/var/log/supervisor            ; ('AUTO' child log dir, default $TEMP)

; the below section must remain in the config file for RPC
; (supervisorctl/web interface) to work, additional interfaces may be
; added by defining them in separate rpcinterface: sections
[rpcinterface:supervisor]
supervisor.rpcinterface_factory = supervisor.rpcinterface:make_main_rpcinterface

[supervisorctl]
serverurl=unix:///var/run/supervisor.sock ; use a unix:// URL  for a unix socket

; The [include] section can just contain the "files" setting.  This
; setting can list multiple files (separated by whitespace or
; newlines).  It can also contain wildcards.  The filenames are
; interpreted as relative to this file.  Included files *cannot*
; include files themselves.

[include]
files = /data/vscode/watchfile/watchfile.conf    #修改自己的配置文件地址
```

由于调用了河马扫描程序来检测文件，所以大量文件同时变更时，检测会慢，建议系统做大量变更时可以停掉程序。

## 运行测试

```sh
在config.ini 中修改自己的配置，因为使用多线程来监控多目录，建议使用多目录配置
运行 python3 daemon.py来查看输出和测试邮件
```

## 异常处理

```
查看输出日志的时候，如果出现wd=-1   
需要修改 vim /etc/sysctl.conf
fs.inotify.max_user_watches = 128000    #决定了同时同一用户可以监控的目录数量

日志中看到Event Queue Overflow
max_queued_events太小需要调整参数
```

由于脚本程序的性质和功能决定了处理大量的文件变更会迟缓，只建议在监控不可控的变更中使用。

## Author

👤 **MisakiKata**

* Website: https://misakikata.github.io
* Github: [@MisakiKata](https://github.com/MisakiKata)



Give a ⭐️ if this project helped you!

***
