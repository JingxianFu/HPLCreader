# HPLCreader
## Intro
&emsp;&emsp;Welcome to this web application based on python that can help you extract and overview HPLC data! It is well known that HPLC data analysis is difficult and spend much time for every researchers that have huge data from HPLC. The main function of this web application is extracting effective data from lcd files generated by HPLC machine. Moreover, it can also draw a overview figure of these effective data.<br/>
&emsp;&emsp;You can use it on my server. However, to use this application locally, it needs the python environments. Thus, I will teach you how to construct this web application in your PC.
* * *
## How to use
### Just try
&emsp;&emsp;I constructed this web application on my local server (it is working in a docker of linux), so you can use your PC to connect to WIFI "jxfu" and "jxfu_5G" to link my LAN(Local Area Network) and then enter [HPLCreader](http://192.168.6.110:1314/ "因为还没有域名备案，所以只能暴露LAN的ip在Github上") to use it. Moreover, you can also connect to "HNZWY" network to access [HPLCreader](http://210.77.80.91:1314 "Server in HNZWY LAN").
<br/>
&emsp;&emsp;On the website, you can see this page that contain 5 empty blanks, and it needs 5 parameters to fill them.
<img width="850" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/b4d12c41-1195-4a35-8247-14b58e5cf020">

<br/>
1. The first blank requires some text data transfered from lcd data in HPLC machine. You can upload one file or many files to this blank. There is a quick tutorial about how to get text file from lcd file.

- Open folder contained lcd files, and choose all of the files. <br/>注：原始.lcd文件的保存路径不能有中文，例如/system/李同学/data/test.lcd是不行的，需要改成/system/studentLi/data/test.lcd，可能后续的运行路径也需要全英文路径。存在中文路径可能导致运行过程中出现乱码，这个问题我还没有解决。
<img width="693" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/34c5551c-72c7-4bcd-810d-db75d7386972">

- As this figure, generate ASCII files.
<img width="845" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/1a4ae910-5eda-447a-9c0e-b657bf2086d2">

- Output these ACSII files.
<img width="810" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/f9d55830-4d28-44cf-a686-265055541c90">

2. The second blank requires a RT file that can locate your component and extract the effective data, such as peak area of this component. <br/>This type of file is csv, you can refer to my example "RT.csv" in /HPLCreader/test folder. <br/>Just replace the string with your own parameters in "RT.csv", and upload this modified "RT.csv" into the blank.
<img width="821" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/ce123919-b57e-461b-ace2-b0cbc6addb5f">

3. The third blank can group your text files that you input in the first blank, and it requires you to print the key word of each group. <br/>For instance, if your text files are a1.txt, a2.txt, a3.txt, b1.txt, b2.txt and b3.txt (both of a and b have 3 repeats), you can fill "a b"(sample A + blank space + sample B) in this blank to group a and b.
<img width="827" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/c7c04bd3-057b-4af7-8216-ed6bd8c6f995">

4. The 4st blank requires a number, and it can help determine the RT range to identify components. <br/>For instance, RT of 3.5 min determine compound A, and RT of 3.4 and 3.6 min can also represent compound A if you fill 0.1 here. <br/>However, if you do not fill this blank, it will give a default parameter of 0.1 min.
5. The final blank is also optional, you can choose the PDA channel you want. In my data, 1 is equal to PDA1, and PDA1 is the measured data in 370 nm wave of component.
<br/><br/>
### local use
&emsp;&emsp;It is recommended that you use miniconda to construct this environment, because it can create a virtual evironment for you and this environment is of no ability to pollute your PC evironment. 
#### Install conda
&emsp;&emsp;First of all, You should download [Miniconda package](https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/ "mirrors from tsinghua university"), and it is easy for Linux and MacOS because "wget" command can download this package automatically.
- MacOS and Linux
<br/>Conducting these commands in terminal(MacOS) or shell(Linux)
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
&emsp;&emsp;It is only a example, and you can replace Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh or Miniconda3-py39_23.5.2-0-Linux-x86_64.sh to which version you need.
- Windows
<br/>Just refer to this [tutorial](https://blog.csdn.net/VistorsYan/article/details/109138602). Just notice how to set environment variable.
#### Create environment
&emsp;&emsp;Conducting these commands in shell, and the python environment has been constructed.
   ```
   cd "HPLCreader's path"
   conda create -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
#### Start program
&emsp;&emsp;Conducting these commands in shell.
   ```
   cd "HPLCreader's path"
   conda activate -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
&emsp;&emsp;Get the [python script](https://github.com/JingxianFu/HPLCreader/archive/refs/heads/main.zip) from Github.
   ```
   # cd to path of main.py, and run these commands
   conda activate -n hplc python=3.11 -y
   python main.py
   # control + C can terminate this script
   # After begenning, it will give you an ip address to access, just like "Use http://192.168.6.126:1314/ to access the application ..."
   ```
&emsp;&emsp;Enter [this website](http://127.0.0.1:1314) and web application is working!
