pyAutoDeploy
============
自动部署工具

**系统要求**

适用于 `Linux`，`Ubuntu` 12.10 已测试过，其他发行版本未测试。

**依赖**

Python（2.7） + web.py

**安装** （Ubuntu 12.10）

假设已安装 `Python` `web.py` `nginx` `uWSGI`。

    git clone https://github.com/tonghuashuai/pyAutoDeploy
    cd pyAutoDeploy
    touch uwsgi.pid
    sudo uwsgi -x auto.xml
    vim pyAutoDeploy

根据实际情况修改域名（ip）和 static 路径地址。

	sudo cp pyAutoDeploy /etc/nginx/sites-enabled/
    sudo nginx -s reload

访问 http://localhost:8080/install，跳转到首页后安装成功，以后可直接访问 http://localhost:8080/。

**使用**

1. 新建 job
2. 输入 GitHub 项目地址（结尾没有 .git），

**to do**
* 添加执行日志
* 控制台内容记录
* 代码优化

**其他**

demo：http://tonghs.cn:8080