# selenium-linux-server
The simplest solution to run Selenium on Linux server (based on Docker). --Linux 服务端运行 Selenium 的最简方案（基于 Docker）。

# selenium-linux-server (中文版)

此方案可能是全网最简的 Linux 服务端 Selnenium 运行方案(无图形界面)。您无需安装任何额外环境，拉取 Docker 镜像即可运行 Selenium 代码。

该方案仅支持在无图形界面的 Linux 终端运行 Selenium，不支持测试代码，请先在您的本机图形界面中完善代码。

### 测试运行

确保机器已安装 Docker 环境，首先拉取镜像

```
docker pull cyberbolt/selenium
```

git 拉取测试代码

```
git clone https://github.com/Cyberbolt/selenium-linux-server.git
```

运行 Selenium 测试代码

```
cd selenium-linux-server
docker run --rm -v /<该目录的绝对路径>/test.py:/test.py cyberbolt/selenium python3 test.py
```


