### 关于
该平台为[ansible](https://github.com/ansible/ansible)的web程序


### 安装


#### 系统centos6.x

#### 安装依赖

```Bash
# yum install -y python-devel openldap-devel gcc mysql-server mysql-devel epel-release
# yum install python-pip git
``` 
    
#### 配置pip源(可选)

```Bash
# mkdir ~/.pip
# vim ~/.pip/pip.conf
  [global]
  index-url # http://mirrors.aliyun.com/pypi/simple/
```

#### 安装virtualenv

```Bash
 # pip install virtualenv
```

#### 配置mysql服务

```Bash
 # /etc/init.d/mysqld start
 # chkconfig mysqld on
 # mysql
   mysql>  create database ansible CHARACTER SET utf8;
   mysql>  grant all on ansible.* to ansibleuser@'localhost' identified by 'password';
   mysql>  flush privileges;
```

#### 下载源码

```Bash
# cd /opt/
# git clone https://github.com/Firxiao/ansible_ui.git
```

#### 添加用户

```Bash
# cd /opt/
# useradd ansible_ui
# chown ansible_ui. -R ansible_ui
```

#### 切换至普通用户

```Bash
# su - ansible_ui
# virtualenv ansible_ui
# source ansible_ui/bin/activate
```

