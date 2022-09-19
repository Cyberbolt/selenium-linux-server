# selenium-linux-server

[中文版](#selenium-linux-server (中文版))

This solution may be the simplest Linux server-side Selnenium running solution (no graphical interface) in the whole network. You don't need to install any extra environment, just pull the Docker image to run Selenium code.

The image is based on Python 3.7, Selenium 4.4.0 (can be updated using pip3), built-in Chrome browser and driver.

This solution only supports running Selenium in a Linux terminal without a graphical interface, and does not support testing code. Please complete the code in your native graphical interface first.

### Test run

Make sure the machine has the Docker environment installed, first pull the image

```bash
docker pull cyberbolt/selenium
````

Run Selenium test code

```bash
docker run --rm cyberbolt/selenium python3 /test/test.py
````

After receiving the following prompt

```bash
Selenium automates browsers. That's it!
````

Has run successfully! This test visits the [Selenium](https://www.selenium.dev/) official website and obtains the content of the h1 header.

### Recommended usage plan

Mount your tested code into the container, and use Docker to specify and run your own code file.

You can use this Selenium image just like a Python image. ( Docker [Official Tutorial](https://docs.docker.com/language/python/) for running Python images )

# selenium-linux-server (中文版)

此方案可能是全网最简的 Linux 服务端 Selnenium 运行方案(无图形界面)。您无需安装任何额外环境，拉取 Docker 镜像即可运行 Selenium 代码。

该镜像基于 Python 3.7，Selenium 4.4.0(可以使用 pip3 更新)，内置 Chrome 浏览器及驱动。

该方案仅支持在无图形界面的 Linux 终端运行 Selenium，不支持测试代码，请先在您的本机图形界面中完善代码。

### 测试运行

确保机器已安装 Docker 环境，首先拉取镜像

```bash
docker pull cyberbolt/selenium
```

运行 Selenium 测试代码

```bash
docker run --rm cyberbolt/selenium python3 /test/test.py
```

之后收到以下提示

```bash
Selenium automates browsers. That's it!
```

已经成功运行！本测试访问了 [Selenium](https://www.selenium.dev/) 官网并获取 h1 标题的内容。

### 推荐使用方案

将自己测试好的代码挂载至该容器中，使用 Docker 指定运行自己的代码文件。

您可以像使用 Python 镜像一样使用该 Selenium 镜像。（Docker 运行 Python 镜像的[官方教程](https://docs.docker.com/language/python/)）
