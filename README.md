# 停更 请参阅 https://github.com/ansible/awx
### 关于
该平台为[ansible](https://github.com/ansible/ansible)的web程序


### 安装  (后续推出playbook一键安装)

##### 系统centos6.x:

##### 配置防火墙

```Bash
# yum install -y lokkit
# lokkit -p 80:tcp -p 8080:tcp -p 9001:tcp -p 22:tcp
```

##### 安装依赖

```Bash
# yum install -y python-devel openldap-devel gcc mysql-server mysql-devel epel-release
# yum install python-pip git
``` 
    
##### 配置pip源(可选)

```Bash
# mkdir ~/.pip
# vim ~/.pip/pip.conf
  [global]
  index-url = http://mirrors.aliyun.com/pypi/simple/
```

##### 安装virtualenv

```Bash
 # pip install virtualenv
```

##### 配置mysql服务

```Bash
 # /etc/init.d/mysqld start
 # chkconfig mysqld on
 # mysql
   mysql>  create database ansible CHARACTER SET utf8;
   mysql>  grant all on ansible.* to ansibleuser@'localhost' identified by 'password';
   mysql>  flush privileges;
```

##### 下载源码

```Bash
# cd /opt/
# git clone https://github.com/Firxiao/ansible_ui.git
```

##### 添加用户

```Bash
# cd /opt/
# useradd ansible_ui
# chown ansible_ui. -R ansible_ui
```

##### 切换至普通用户并配置虚拟python环境

```Bash
# su - ansible_ui
$ virtualenv ansible_ui_env
$ source ansible_ui_env/bin/activate
```

##### 安装python依赖

```Bash
$ pip install -r /opt/ansible_ui/requirements.txt
```
##### 配置ansible 免key检测

```Bash
$ cp /opt/ansible_ui/ansible-conf/ansible.cfg ~/.ansible.cfg
```

##### 配置并启动celery

```Bash
$ vim /opt/ansible_ui/celery-conf/supervisord.conf
  command = /home/ansible_ui/ansible_ui_env/bin/python /opt/ansible_ui/manage.py celeryd -B -l info
  user = ansible_ui
$ supervisord -c /opt/ansible_ui/celery-conf/supervisord.conf
$ netstat -tupln|grep 9001    #验证celery是否运行
```
    web 访问 http://ip:9001  默认用户名admin 密码password

##### 配置并初始化ansible_ui数据库

```Bash
$ vim /opt/ansible_ui/desktop/core/internal/settings_local.py #配置数据库信息及ansible-playbook命令的绝对路径
$ cd /opt/ansible_ui
$ python manage.py syncdb       #最后根据提示添加admin用户
```
##### 启动ansible_ui
```Bash
$ cd /opt/ansible_ui
$ python manage.py runserver 0.0.0.0:8080
```
    web 访问 http://ip:8080  默认用户名密码为初始化数据库时所创建的用户


##### 待续..
