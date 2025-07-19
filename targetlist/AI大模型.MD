课程： 黑马程序员Python+AI大模型开发零基础到项目实战全套教程，基于DeepSeek和Qwen大模型，从大模型私有化部署、运行机制到独立搭建聊天机器人一套通关
课程地址: https://www.bilibili.com/video/BV1h1VbzHER2?spm_id_from=333.788.player.switch&vd_source=c60dd2f510df2780881492a99de9e169&p=18
如何下载资料: https://www.bilibili.com/opus/443715248901563958
资源地址： 通过网盘分享的文件：3、AI大模型开发入门   链接: https://pan.baidu.com/s/1oJt0kJOrAWvq9TNxJr65iw 提取码: tasy

人工智能开发热门教程：
AI大模型开发：BV1h1VbzHER2
Python数据挖掘：BV1xt411v7z9
3天玩转机器学习：BV1nt411r7tj
NLP自然语言处理技术：BV17y4y1m737
AI-OpenCV图像处理：BV1Fo4y1d7JL
人工智能深度学习：BV1L4411v7fB
图像与视觉处理：BV1Rz4y1R7Mb

以下是具体的课程目录：

00-AI大模型课程导学       视频耗时( 05:18 )
学习笔记: 没什么关键知识

01-大模型概念入门     视频耗时( 08:46 )
学习笔记: 没什么关键知识

02-大模型核心实现机制     视频耗时( 04:53 )
学习笔记: 没什么关键知识

03-DeepSeek和蒸馏模型     视频耗时( 07:41 )
学习笔记:
Deepseek为什么出名？ 性能高 、 成本低(GPU(显卡)资源-英伟达) 、 技术开源(gitHub)
deepseek-r1模型地址: https://github.com/deepseek-ai/DeepSeek-R1
Qwen模型地址:  https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B/tree/main

大模型的蒸馏 ： 假设你有一个超强的老师（大模型），他能讲解很复杂的知识。你想把这些知识传授给一群学生（小模型）。为了让学生们能在不需要过多时间和资源的情况下，快速掌握老师的知识，你可以通过“蒸馏”这种方式，让学生们只学习最精华、最重要的部分。这样，学生虽然没有老师那样强大，但依然能做出优秀表现。

本课程主要基于deepseek-r1，7b参数（约6GB显存需求）的模型进行开发和应用

04-私有化部署实战需求介绍     视频耗时( 06:30 )
学习笔记:
常见聊天机器人：
DeepSeek
由杭州深度求索人工智能基础技术研究有限公司研发,  其核心优势在于性能卓越、低成本开发和开源策略
Kimi智能助手
由月之暗面科技有限公司开发，支持超长上下文（最高200万汉字），适合长文本处理和复杂对话。
通义千问
阿里云推出的人工智能助手，适合办公场景，提供高效的信息处理能力。
讯飞星火
科大讯飞出品，支持语音输入和语音朗读回复，适合语音交互场景。
豆包
字节跳动推出，支持抖音和今日头条的内容信息获取，适合内容创作和信息检索。

05-私有化部署实战项目架构分析     视频耗时( 04:55 )
学习笔记:
不管是个人电脑还是云平台，搭建聊天机器人的步骤为：
1. 后端和模型部署。
   个人电脑: 后端使用Ollama框架搭配deepseek-r1、qwen模型
   云平台: 后端使用LangChain框架搭配阿里云百炼平台、通义千问
2. 前端部署，个人电脑或云平台均可使用Streamlit

06-Ollama简介     视频耗时( 04:00 )
学习笔记:
网址：https://ollama.com
ollama 官方模型库: https://ollama.com/library

07-Windows系统Ollama私有化模型部署    视频耗时( 11:04 )
学习笔记:
Windows系统安装Ollama
<1>. 下载Ollama，Windows系统安装包：https://ollama.com/download    (实测 下载很慢 只有 10KB/s )
<2>.双击提前下载好的OllamaSetup.exe安装包,选择install,然后一直默认安装即可
<3>, win+R打开终端,输入ollama -v命令查看是否安装成功
<4>,  ollama run deepseek-r1:1.5b
ollama run qwen2:1.5b

模型下载到哪里了?
默认安装路径: C:\Users\Lenovo\.ollama\models


问题1： C:\Users\Administrator>ollama -v
Warning: could not connect to a running Ollama instance
Warning: client version is 0.9.6
解决办法： 需要单独开一个CMD ，执行  执行命令：ollama serve  (原文链接：https://blog.csdn.net/abbiz/article/details/140383148)

问题2： C:\Users\Administrator>ollama run deepseek-r1:1.5b
Error: ollama server not responding - timed out waiting for server to start
解决办法： 需要单独开一个CMD ，执行  执行命令：ollama serve  (原文链接：https://blog.csdn.net/abbiz/article/details/140383148)

<5>, Ctrl + D : 退出cmd的"提问聊天"


08-Windows系统-基于Chatbox部署大模型前端      视频耗时( 09:10 )
学习笔记:
Chatbox AI 官网: https://chatboxai.app/zh   下载 安装包

Chatbox 安装：
1，选择  "使用自己的API Key或本地模型" -- 就是本地安装的 Ollama API,
2，API 域名:  http://127.0.0.1:11434  (就用默认的)
3，模型(如果没有选项，需要启动Ollama ): deepseek-r1:1.5b
其中启动Ollama 的方法 ： C:\Windows\System32>ollama serve

09-[扩展]Mac系统部署Ollama私有化模型      视频耗时( 07:43 )
学习笔记:
暂时略过，目前只部署windows

10-[扩展]Mac系统-基于Chatbox部署大模型前端    视频耗时( 08:38 )
学习笔记:
暂时略过，目前只部署windows

11-Windows配置WSL(Ubuntu)环境     视频耗时( 14:56 )
学习笔记:
<1>，WSL（Windows Subsystem for Linux）是Win10系统推出的全新功能，让我们可以在Windows环境下获得绝佳的Linux操作系统体验。可以在Linux环境下直接使用宿主机的CPU、内存、显卡等硬件，提供比传统虚拟机更好的硬件性能。,
<2>，简而言之：
Windows10/11的WSL功能，可以无需单独虚拟一套硬件设备
就可以直接使用主机的物理硬件，构建Linux操作系统
并不会影响Windows系统本身的运行
<3>，部署 WSL(Ubuntu)
<3.1>开启 WSL(Ubuntu)： 控制面板 - 程序和功能 - 启用或关闭windows功能 - 勾选"适用于linux的windows子系统" - 立刻重新启动电脑
<3.2>安装WSL的操作系统: 打开Windows应用商店(MicroSoft Store) - 搜索Ubuntu - 第一个"Ubuntu" - 获取 和 安装
<3.3> 点击"打开"按钮
输入用户名用以创建一个用户：itheima
输入两次密码确认（注意，输入密码没有反馈，不用理会，正常输入即可）：123456
注意： 可能之前安装过 Ubuntu，所以当下没有让设置用户名 和 密码 (所以，用户名 和 密码 不是  itheima  / 123456 )

完成以上三步，就得到了 一个可用的 WSL(Ubuntu) 操作系统环境
<4> 安装Windows Terminal软件
Ubuntu自带的终端窗口软件不太好用，我们可以使用微软推出的：Windows Terminal 软件
在应用商店中搜索terminal关键字，找到Windows Terminal软件下载并安装


问题: "打开" Ubuntu 时，报如下错误：
Installing, this may take a few minutes...
WslRegisterDistribution failed with error: 0x8007019e
Error: 0x8007019e ?????? Linux ? Windows ????????? ?wsl.exe --install? ?????
?????????? https://aka.ms/wslinstall
Press any key to continue...
解决办法:  C:\Windows\System32> wsl -l -v   (该指令的效果如下:
适用于 Linux 的 Windows 子系统必须更新到最新版本才能继续。可通过运行 “wsl.exe --update” 进行更新。
正在下载: 适用于 Linux 的 Windows 子系统 2.5.9 )

12-Linux部署Ollama    视频耗时( 21:08 )
学习笔记:
1, CUDA是英伟达（NVIDIA）推出的一种并行计算平台和编程模型。
它允许开发者利用英伟达 GPU（图形处理单元）的强大计算能力来加速计算密集型任务，而不仅仅是用于图形渲染。
注意: 大模型是计算密集型任务
2， 验证CUDA是否可用
WSL在安装好Ubuntu后，自动安装了显卡驱动以及CUDA，可以通过命令：nvidia-smi验证
3， Linux系统安装一键部署ollama
3.1 打开Ollama官网，https://ollama.com/download/linux
可以看到，只需要一行命令( curl -fsSL https://ollama.com/install.sh | sh )，即可在Linux系统中部署Ollama
注意: 一键直接安装很容易失败（网络）,所以 采用手动安装的模式( Manual install instructions )
3.2 手动安装的模式: 下载Ollama Linux系统安装包：https://ollama.com/download/ollama-linux-amd64.tgz
在课程资料中，已经为大家提供好了，大家可以从课程资料中得到安装包
3.3 , 将ollama-linux-amd64.tgz复制到当前的home目录中:   cp ollama-linux-amd64.tgz  ~/
3.4 , 解压Ollama到/usr文件夹 ：    sudo tar -xvf ollama-linux-amd64.tgz -C /usr


ollama serve： 前台启动ollama， 关闭窗口 或 Ctrl+C 会 停止

ollama serve： 后台静默启动ollama
1，添加用户(ollama) 和 将ollama添加到用户组
创建Ollama运行所用用户:
sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama
将ollama添加到ollama用户组:
sudo usermod -a -G ollama $(whoami)

    注意： 指定的home目录：  root@WIN-7MT1R5NQOS1:~# cd /usr/share/ollama/

    2. 配置Ollama为系统服务，方便启动、停止
    创建新文件： sudo touch /etc/systemd/system/ollama.service
    将下面内容保存到上述文件内

    [Unit]
    Description=Ollama Service
    After=network-online.target

    [Service]
    ExecStart=/usr/bin/ollama serve
    User=ollama
    Group=ollama
    Restart=always
    RestartSec=3
    Environment="PATH=$PATH"

    [Install]
    WantedBy=multi-user.target

    3,执行如下命令生效
    sudo systemctl daemon-reload

    4,命令使用
    sudo systemctl enable ollama	开启ollama开机自启
    sudo systemctl disable ollama	关闭ollama开机自启
    sudo systemctl start ollama	启动ollma
    sudo systemctl status ollama	查看ollama运行状态
    sudo systemctl stop ollama	停止ollama

    7. 启动Ollama查看运行状态
    sudo systemctl start ollama
    sudo systemctl status ollama
    8. 下载模型文件（或第一次启动模型的时候，也会自动下载）
    ollama pull deepseek-r1:7b
    ollama pull qwen2:7b
    9. 在命令启动模型使用
    ollama run deepseek-r1:7b



ollama -v： 查看当前的版本
问题:
ls: cannot access 'd': Input/output error
ls: cannot access 'c': Input/output error
total 0
d????????? ? ?    ?      ?            ? c
d????????? ? ?    ?      ?            ? d
drwxrwxrwt 2 root root  60 Jul 13 11:13 wsl
drwxrwxrwt 7 root root 300 Jul 13 11:14 wslg
解决办法:
在WSL中尝试重新挂载驱动器
- 在WSL终端中，先卸载有问题的挂载点，然后重新挂载：
  sudo umount /mnt/c
  sudo umount /mnt/d
  然后重新挂载：
  sudo mount -t drvfs C: /mnt/c
  sudo mount -t drvfs D: /mnt/d

常见指令:
cd ：回到当前 home 目录中
ls -a : 可以查看隐藏目录
ollama pull deepseek-r1:1.5b  下载文件
模型文件存放目录: cd /usr/share/ollama/.ollama/models/blobs       ( ls -h : 看文件最大的文件)
ollama -h : 帮助指令
mkdir learn_ai : 创建文件夹


13-Linux部署Python开发环境    视频耗时( 10:46 )
学习笔记:

命令使用
sudo systemctl enable ollama	开启ollama开机自启
sudo systemctl disable ollama	关闭ollama开机自启
sudo systemctl start ollama	启动ollma
sudo systemctl status ollama	查看ollama运行状态
sudo systemctl stop ollama	停止ollama


Python所需库的安装
WSL（Ubuntu）内置了Python（版本3.8），所以无需部署Python，但如果需要编写代码调用Ollama，需要安装Ollama库。
1. 安装pip工具
   sudo apt install python3-pip
2. 验证pip的使用
   pip -V   注意V是大写字母
3. 安装ollama库(用于Python调用Ollama）
   pip install ollama
4. 安装Streamlit库（用于Python开发对话页面）
   pip install streamlit


问题:
root@WIN-7MT1R5NQOS1:~# pip install ollama
error: externally-managed-environment

× This environment is externally managed
╰─> To install Python packages system-wide, try apt install
python3-xyz, where xyz is the package you are trying to
install.

    If you wish to install a non-Debian-packaged Python package,
    create a virtual environment using python3 -m venv path/to/venv.
    Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
    sure you have python3-full installed.

    If you wish to install a non-Debian packaged Python application,
    it may be easiest to use pipx install xyz, which will manage a
    virtual environment for you. Make sure you have pipx installed.

    See /usr/share/doc/python3.12/README.venv for more information.

note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-packages.
hint: See PEP 668 for the detailed specification.  

解决办法:  使用虚拟环境（推荐）：
# 安装虚拟环境工具
sudo apt install python3-venv
# 创建虚拟环境
python3 -m venv myenv
# 激活虚拟环境
source myenv/bin/activate
# 在虚拟环境中安装
pip install ollama


问题: Traceback (most recent call last):
File "/home/dhy/py_code/learn_ai/test.py", line 2, in <module>
import streamlit as st
ModuleNotFoundError: No module named 'streamlit'  什么意思 怎么解决

原因： 这个错误 ModuleNotFoundError: No module named 'streamlit' 表示 Python 找不到 Streamlit 库，通常是因为：
错误原因
未安装 Streamlit：你还没有在 Python 环境中安装 Streamlit
安装在错误的环境：可能安装到了系统 Python 而非你当前使用的环境
虚拟环境未激活：如果你在虚拟环境中安装了 Streamlit，但运行脚本时未激活该环境
Python 解释器路径问题：IDE 或终端使用了错误的 Python 解释器

解决办法： 方法 1：在正确环境中安装 Streamlit
# 1. 创建并激活虚拟环境（避免系统冲突）
python3 -m venv streamlit-env
source streamlit-env/bin/activate  # Linux/Mac
# streamlit-env\Scripts\activate   # Windows
# 2. 安装 Streamlit
pip install streamlit
# 3. 验证安装
python -c "import streamlit as st ; print(st.__version__)"



PyCharm连接WSL（Ubuntu）:
IDE PyCharm内置WSL的支持，可以将Python解释器程序直接连接到WSL内。
实现：用Windows的PyCharm，在Linux上写代码，并在Linux上运行。


关于import Streamlit 报错 no moudle named ‘Streamilt‘
解决办法1(没效果): root@WIN-7MT1R5NQOS1:~# pip install streamlit
        但是报如下错误:
        error: externally-managed-environment
        
        × This environment is externally managed
        ╰─> To install Python packages system-wide, try apt install
        python3-xyz, where xyz is the package you are trying to
        install.
        
            If you wish to install a non-Debian-packaged Python package,
            create a virtual environment using python3 -m venv path/to/venv.
            Then use path/to/venv/bin/python and path/to/venv/bin/pip. Make
            sure you have python3-full installed.
        
            If you wish to install a non-Debian packaged Python application,
            it may be easiest to use pipx install xyz, which will manage a
            virtual environment for you. Make sure you have pipx installed.
        
            See /usr/share/doc/python3.12/README.venv for more information.
        
        note: If you believe this is a mistake, please contact your Python installation or OS distribution provider. You can override this, at the risk of breaking your Python installation or OS, by passing --break-system-package
解决办法2(没效果):
        遇到externally-managed-environment错误时，说明当前Python环境受系统保护，直接通过pip安装可能影响系统稳定性‌12。以下是几种解决方案：
        ‌推荐方案：创建虚拟环境‌
        执行 python3 -m venv /path/to/venv 创建独立环境‌
        激活环境后使用 /path/to/venv/bin/pip install streamlit 安装‌
        优点：完全隔离，不影响系统环境‌
解决办法3(成功):
        # 创建虚拟环境
        python3 -m venv ~/streamlit_venv
        source ~/streamlit_venv/bin/activate  # 激活环境
        pip install streamlit                # 在虚拟环境中安装

问题: import streamlit as st 时报错 (为什么 streamlit 安装成功了，但是在PyCharm 的代码中  import streamlit as st  会报导包失败呢?)
Installing packages failed Installing packages: error occurred
解决办法:🟢 推荐方案：创建虚拟环境（新手友好）
1,打开终端（保持当前窗口就行）
2,创建专属环境（相当于给你的项目建个独立房间）：
 python -m venv myenv  # 创建名为 myenv 的虚拟环境
3.进入这个环境：
source myenv/bin/activate  # 激活环境
4，在专属环境里安装：
pip install streamlit -i https://mirrors.aliyun.com/pypi/simple/
5，测试是否成功：
 python -c "import streamlit; print('安装成功啦！')"

注意： 
1，📝 使用虚拟环境后的操作指南
每次使用时，先激活环境： source myenv/bin/activate
2，在 PyCharm 中设置虚拟环境：
打开 PyCharm
右下角点击当前 Python 版本
选择「添加解释器」→「现有环境」
找到 myenv/bin/python 文件
点击「确定」
3， 创建测试文件 test.py：
import streamlit as st
st.title("恭喜AI新手！")
st.write("你成功解决了安装问题🎉")
4， 运行：
右键点击文件 → Run 'test'
等待浏览器自动打开显示结果

🌟 给新手的贴心提示:
1,虚拟环境就像"游戏副本"，安装任何新包前都要先 source myenv/bin/activate
2,看到 (myenv) 前缀表示在安全环境里
3,关闭终端后下次使用需要重新激活

问题:
/home/dhy/py_code/learn_ai/myenv/bin/python /home/dhy/py_code/learn_ai/test.py
2025-07-19 18:04:12.414 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-19 18:04:12.432
Warning: to view this Streamlit app on a browser, run it with the following
command:
    streamlit run /home/dhy/py_code/learn_ai/test.py [ARGUMENTS]
2025-07-19 18:04:12.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-19 18:04:12.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-19 18:04:12.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-19 18:04:12.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
2025-07-19 18:04:12.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.
Process finished with exit code 0
解决:
方法一: 方法1：通过终端命令运行（推荐）
其实，在 打开 PyCharm 的 Terminal（终端）: streamlit run test.py  (是正常的，查看网站   Local URL: http://localhost:8501
Network URL: http://172.18.121.248:8501
)

方法2：配置 PyCharm 的运行方式
1,在 PyCharm 顶部菜单：Run → Edit Configurations
2,点击左上角 + 号 → 选择 Python
3,按这样配置：
    Script path: 选择 streamlit 的位置（在 myenv/bin/streamlit）
    Parameters: 输入 run test.py
    Working directory: 选择你的项目文件夹 (我的目录:  /home/dhy/py_code/learn_ai)
4,点击 Apply → OK
5,现在可以点击绿色三角按钮运行了









Tips: 
1, 要确认Streamlit包是否已安装，可通过以下方法验证：
解答:
要确认Streamlit包是否已安装，可通过以下方法验证：
<1>命令行检查‌
执行pip show streamlit，若显示版本信息则已安装‌
或运行streamlit --version，输出版本号即表示成功安装‌
<2>交互式验证‌
在Python环境中输入：
import streamlit
print(streamlit.__version__)
无报错且输出版本号即正常‌
<3>运行测试应用‌
执行streamlit hello，若自动打开浏览器并显示欢迎页面则安装成功‌
<4>PyCharm环境检查‌
在IDE的Python Interpreter设置中查看已安装包列表‌
若使用虚拟环境，需先激活对应环境再检查‌

若上述方法均未检测到，建议通过pip install streamlit重新安装‌。

2, 打开cmd窗口使用pip list查看pip的版本是多少，pycharm也可以这样查询。
然后使用 python -m pip install --upgrade pip 这行命令对pip进行升级

3, 怎么卸载 streamlit
以下是卸载 Streamlit 的完整操作指南：

1. 标准卸载方法（推荐）
   pip uninstall streamlit
执行后会提示确认，输入 y 完成卸载。
适用场景‌：通过 pip 安装的常规卸载。
2. 彻底清除残留文件
若需完全清理：
# 查找安装路径
pip show streamlit | grep Location
# 进入包目录（示例路径）
cd /usr/local/lib/python3.12/site-packages/
# 删除相关文件
rm -rf streamlit* __pycache__/streamlit*
同时清理用户目录配置文件：
rm -rf ~/.streamlit/   # 配置文件
rm -rf ~/.cache/streamlit/  # 缓存文件
3. 虚拟环境卸载方案
若安装在虚拟环境中：
# 激活环境
source /path/to/venv/bin/activate
# 卸载包
pip uninstall streamlit
# 彻底删除环境（可选）
deactivate
rm -rf /path/to/venv
4. Windows 系统特殊处理
通过控制面板卸载：
Win+R 输入 appwiz.cpl
找到 Python 相关条目
选择 卸载 或 修改
同时删除：
C:\Users\<用户名>\AppData\Local\streamlit
C:\Users\<用户名>\AppData\Roaming\streamlit
验证卸载效果
pip list | grep streamlit  # 应无输出
streamlit --version        # 应显示"command not found"

注意‌：
系统级安装需 sudo 权限
macOS/Linux 残留路径：~/Library/Application Support/Steam/（仅当通过 Steam 安装时）
推荐优先使用虚拟环境避免系统污染


4, 检查已安装包列表： pip list | grep streamlit

5, 安装 Altair 和 Pandas
pip install pandas
pip install altair
建议同时安装示例数据集包： pip install vega_datasets
✅ 验证安装：
import pandas as pd
import altair as alt
print(pd.__version__, alt.__version__)


14-Ollama基础Python代码       视频耗时( 10:46 )
学习笔记:

15-Streamlit的基础API使用     视频耗时( 17:33 )
学习笔记:

16-Streamlit开发对话网页      视频耗时( 23:02 )
学习笔记:

17-Ollama&Streamlit开发聊天机器人界面     视频耗时( 11:10 )
学习笔记:




