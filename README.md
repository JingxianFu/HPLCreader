# HPLCreader
## Intro
&emsp;&emsp;Welcome to this web application based on Python that can help you to extract and provide overview HPLC data! It is well-known that HPLC data analysis is difficult and time consuming for researchers who have huge data derived from HPLC machine. The main function of this web application is extracting effective data from lcd files generated by HPLC machine. As well as providing an overview figure of these effective data.<br/>
&emsp;&emsp;You may use it on this server. However, in order to use this application in local drive, it needs a python environment. Hereby, it is a guide for you to set up your own application.
* * *
## How to use
### Just try
&emsp;&emsp;I constructed this web application on my local server (it is working in a docker of linux), so you can use your PC to connect to WIFI "jxfu" and "jxfu_5G" to link my LAN(Local Area Network) and then enter [HPLCreader_jxfu](http://jxfu.xyz:1314/ "因为还没有域名备案，所以只能暴露LAN的ip在Github上") to use it. Moreover, you can also connect to "HNZWY" network to access [HPLCreader_HWZWY](http://jxfu.xyz:1314 "Server in HNZWY LAN").
<br/>
&emsp;&emsp;On the website, you can see this page that contain 5 empty blanks, and it needs 5 parameters to fill them.
<img width="850" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/b4d12c41-1195-4a35-8247-14b58e5cf020">

<br/>
1. The first inputbox requires some ".txt" transferred from ".lcd" in HPLC machine. You can upload one or multiple files into this inputbox. There is a quick tutorial about how to get text file from lcd file.

- In HPLC machine, open folder contained ".lcd" data, and choose all of documents. <br/>注：原始.lcd文件的保存路径不能有中文，例如/system/李同学/data/test.lcd是不行的，需要改成/system/studentLi/data/test.lcd，可能后续的运行路径也需要全英文路径。存在中文路径可能导致运行过程中出现乱码，这个问题我还没有解决。
<img width="693" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/34c5551c-72c7-4bcd-810d-db75d7386972">

- According to the figure below, generate ASCII files. (from HPLC machine)
<img width="845" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/1a4ae910-5eda-447a-9c0e-b657bf2086d2">

- Output these ACSII files into your drive. (from HPLC machine)
<img width="810" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/f9d55830-4d28-44cf-a686-265055541c90">

2. The second inputbox requires a RT file that can locate your biochemical compound and extract the effective data, such as peak area of this compound. <br/>This type of file is csv, you can refer to my example "RT.csv" in /HPLCreader/test folder. <br/>Just replace the parameters with your own parameters in "RT.csv", and upload this edited "RT.csv" into the inputbox.
<img width="821" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/ce123919-b57e-461b-ace2-b0cbc6addb5f">

3. The third inputbox can group up your text files that you input in the first inputbox, and it requires you to type the keyword of each group. <br/>For instance, if your text files are "a1.txt, a2.txt, a3.txt" & "b1.txt, b2.txt, b3.txt" (both of a and b have 3 replicates), you can fill "a b"(sample A + blank space + sample B) in this inputbox to differentiate "a" and "b".
<img width="827" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/c7c04bd3-057b-4af7-8216-ed6bd8c6f995">

4. The forth inputbox requires a number, and it may help to determine the RT range to identify compounds. <br/>For instance, if the determined compound fall on RT of 3.5 min, then you need to fill "0.1" in this input box to represent the confidence interval of this compound that can be adjusted from 3.4 to 3.6 min.
<br/>If this input box is empty, it will be given a default parameter of 0.1 min.
5. The final input box is an optional, you may choose any PDA channel you want. From the given data, 1 equals to PDA1 and PDA1 refers to the absorbance reading in 370nm wavelength on the biochemical compounds.
6. Click submit to get your result.
<br/><br/>
### Local use
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
&emsp;&emsp;It is only an example, and you can replace Miniconda3-py39_23.5.2-0-MacOSX-arm64.sh or Miniconda3-py39_23.5.2-0-Linux-x86_64.sh to which version you need.
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
   conda create -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
&emsp;&emsp;Get the [python script](https://github.com/JingxianFu/HPLCreader/archive/refs/heads/main.zip) from Github.
   ```
   # cd to path of main.py, and run these commands
   conda activate hplc
   python main.py
   # control + C can terminate this script
   # After begenning, it will give you an ip address to access, just like "Use http://192.168.6.126:1314/ to access the application ..."
   ```
&emsp;&emsp;Enter [this website](http://127.0.0.1:1314) and web application is working!
# Acknowledge
[Pywebio](https://github.com/pywebio/PyWebIO) is an avaliable package, because it can help you develop python script on web and does not requires that you have many knowledge about front end. In this project, I just use it easily, but recommend it for everyone who learn python, and you can learn it more on its website.
