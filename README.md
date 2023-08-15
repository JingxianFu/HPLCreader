# HPLCreader
## Intro
&emsp;&emsp;Welcome to use this web application based on python that can help you to extract and overview HPLC data! It is well known that HPLC data analysis is difficult and spend much time for every researchers that have huge data from HPLC. The main function of this web application is extracting effective data from lcd files generated by HPLC machine. Moreover, it can also draw a overview figure of these effectice data.<br/>
&emsp;&emsp;You can use it in my server. However, to use this application locally, it needs the python environments. Thus, I will teach you how to construct this web application in your PC.
* * *
## How to use
### Just try
&emsp;&emsp;I constructed this web application in my local server (it is working in a docker of linux), so you can use your PC to connect WIFI "jxfu" and "jxfu_5G" to link my LAN(Local Area Network) and then enter [HPLCreader](http://192.168.6.110:1314/ "因为还没有域名备案，所以只能暴露LAN的ip在Github上") to use it. Moreover, you can connect "HNZWY" network to access [HPLCreader](http://210.77.80.91:1314 "Server in HNZWY LAN").
<br/>
&emsp;&emsp;In website, you can see this page that contain 5 empty blanks, and it needs 5 parameters to fill them. 
<img width="898" alt="image" src="https://github.com/JingxianFu/HPLCreader/assets/65908422/5c0b3571-d718-4553-be43-5fddc7eb8694">
<br/>
+ &emsp;&emsp;The first blank requires some text data transfered from lcd data in HPLC machine. You can fill one file or many files in this blank.
<br/>&emsp;&emsp;Open folder contained lcd files, and choose all of files.
![IMG_1149](https://github.com/JingxianFu/HPLCreader/assets/65908422/0361710b-b897-448c-8e44-890b0d691779)
<br/>&emsp;&emsp;As this figure, generate ASCII files.
![IMG_1150](https://github.com/JingxianFu/HPLCreader/assets/65908422/f64e8a1c-84ce-483e-bfbc-fce2c7762627)
<br/>&emsp;&emsp;Output these ACSII files.
![IMG_1151](https://github.com/JingxianFu/HPLCreader/assets/65908422/51c922c0-5b39-4441-bc6d-0360321aae61)
+ &emsp;&emsp;The second blank requires a RT file that can locate your component and extract the effective data, such as peak area of this component. This file is a csv file, you can refer my example RT.csv in /HPLCreader/test folder.
|  RT   | compounent  |
| :---  | ---:  |
| Residence Time 1 (min)  | compounent 1 |
| Residence Time 2 (min)  | compounent 2 |
+ &emsp;&emsp;The third blank requires .
+ &emsp;&emsp;The 4st blank requires a number, and it can help determine the RT range to identify components.
+ &emsp;&emsp;The final blank is a choice, you can choose the PDA channel you want. In my data, 1 is equal to PDA1, and PDA1 can measure 370 nm wave of component.
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
<br/>Just refer to this [tutorial](https://blog.csdn.net/VistorsYan/article/details/109138602). Just notice how to set environment variation.
#### Create environment
&emsp;&emsp;Conducting these commands in shell, and the python environment has been constructed.
   ```
   cd "HPLCreader's path"
   conda activate -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
#### Start program
&emsp;&emsp;Conducting these commands in shell.
   ```
   cd "HPLCreader's path"
   conda activate -n hplc python=3.11 -y
   pip install -r requirements.txt
   ```
&emsp;&emsp;Enter [this website](http://127.0.0.1:1314) and web application has worked!
