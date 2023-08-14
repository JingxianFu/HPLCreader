# HPLCreader
## Intro
Welcome to use this web application based on python that can help you to extract and overview HPLC data! It is well known that HPLC data analysis is difficult and spend much time for every researchers that have huge data from HPLC. The main function of this web application is extracting effective data from lcd files generated by HPLC machine. Moreover, it can also draw a overview figure of these effectice data.
You can use it in my server. However, to use this application locally, it needs the python environments. Thus, I will teach you how to construct this web application in your PC.
## How to use
### Just try
I constructed this web application in my local server (it is working in a docker of linux), so you can use your PC to connect WIFI "jxfu" and "jxfu_5G" to link my LAN(Local Area Network) and then enter [HPLCreader](http:\\198.168.6.110:1314/ "因为还没有域名备案，所以只能暴露LAN的ip在Github上") to use it.
### local use
It is recommended that you use miniconda to construct this environment, because it can create a virtual evironment for you and this environment is of no ability to pollute your PC evironment. 
1. Install conda
   You can download [Miniconda package](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/ "mirrors from tsinghua university")
- MacOS and Linux
  Conducting these commands in terminal(MacOS) or shell(Linux)
  ```
  #For arm Mac
  wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh
  sh Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh
  ```

  ```
  #For x86 Linux
  wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py39_23.5.2-0-Linux-x86_64.sh
  sh Miniconda3-py39_23.5.2-0-Linux-x86_64.sh
  ```
  It is only a example, and you can replace Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh or Miniconda3-py39_23.5.2-0-Linux-x86_64.sh to which version you need.
- Windows
  Just refer to this [tutorial](https://blog.csdn.net/VistorsYan/article/details/109138602). Just notice how to set environment variation.
1. Create environment
   Conducting these commands in shell, and the python environment has been constructed.
   ```
   cd "HPLCreader's path"
   conda activate -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
2. Start program
   Conducting these commands in shell.
   ```
   cd "HPLCreader's path"
   conda activate -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
   Enter [this website](http://127.0.0.1:1314) and web application has worked!
