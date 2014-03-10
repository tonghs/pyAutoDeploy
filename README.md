pyAutoDeploy
============
`GitHub` 项目自动部署工具


**定义**

`GitHub` 项目：您要部署的，托管在 `GitHub` 上的项目
部署环境：您的 `GitHub` 项目将要部署的目标环境，可能是 Server、PC 或者 `VPS`
域名或 ip：您的部署环境的`外网`域名或 ip


**系统要求**

适用于 `Linux`，`Ubuntu 12.10` 已测试过，其他发行版本未测试。

**依赖**

Python（2.7） + web.py

**安装** （`Ubuntu 12.10`）

假设部署环境已安装 `Python` `web.py` `nginx` `uWSGI` `uwsgi-plugin-python`。

    sudo git clone https://github.com/tonghuashuai/pyAutoDeploy
    cd pyAutoDeploy
    sudo touch uwsgi.pid
    sudo uwsgi -x auto.xml
    sudo vim pyAutoDeploy

根据实际情况修改域名（ip）和 static 路径地址。

    sudo cp pyAutoDeploy /etc/nginx/sites-enabled/
    sudo nginx -s reload

访问 http://localhost:8080/install，跳转到首页后安装成功，以后可直接访问 http://localhost:8080。

**使用**

1. （在 `GitHub` 网站或 IDE 中操作）在 `GitHub` 项目中添加 cmd.sh 文件，可维护 cmd.sh 文件添加命令，这些命令将在 pull 代码后执行
1. （在 `GitHub` 网站中操作）在 GitHub 项目中设置 WebHook URL：http://公网域名或ip:8080/push
1. （在部署环境中操作）clone `GitHub` 项目到部署环境
1. （在 pyAutoDeploy 中操作）新建 job
1. （在 pyAutoDeploy 中操作）输入 `GitHub` 项目地址（结尾没有 .git）
1. （在 pyAutoDeploy 中操作）输入工作目录，即 clone 到本地的 `GitHub` 项目文件夹所在目录
1. （在 pyAutoDeploy 中操作）提交

至此，向 `GitHub` push 代码后 pyAutoDeploy 将会 pull 代码到部署环境，然后执行 cmd.sh 中的命令。

**to do**
* 任务计划
* 代码优化

**其他**

demo：http://tonghs.cn:8080 （demo 中已有的项目请不要删除，谢谢。）

项目博客：http://www.tonghs.com/?cat=588

@tonghs：http://www.tonghs.com
