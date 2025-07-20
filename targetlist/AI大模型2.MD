课程： SpringAI+DeepSeek大模型应用开发实战视频教程
课程地址: https://yun.itheima.com/course/1067.html
如何下载资料: https://www.bilibili.com/opus/443715248901563958
资源地址： 通过网盘分享的文件：2025-SpringAI+DeepSeek大模型应用开发  链接: https://pan.baidu.com/s/1x2k7IkM69cmtXfL4_usJBA 提取码: j64b


第1节 - 01.课程介绍
学习笔记: 没什么关键内容

第2节 - 02.认识AI和大模型
学习笔记: 没什么关键内容

第3节 - 03.大模型应用开发-模型部署方案对比
学习笔记:
1，模型部署: 云部署 + 本地部署

第4节 - 04.大模型应用开发-模型部署-云服务
学习笔记:
1, 模型部署-云服务
国内知名的云服务平台都提供了全球知名的大模型的私有部署功能,甚至还提供了这些模型的AP1开放平台,无需部署就能访问。 
云平台          公司          地址 
阿里百炼         阿里巴巴    https://bailian.console.aliyun.com 
腾讯TI平台       腾讯          https://cloud.tencent.com/product/ti 
千帆平台         百度          https://console.bce.baidu.com/qianfan/overview 
SiliconCloud    硅基流动     https://siliconflow.cn/zh-cn/siliconcloud 
火山方舟-火山引擎  字节跳动       https://www.volcengine.com/product/ark


第5节 - 05.大模型应用开发-模型部署-本地部署
学习笔记:
模型部署-本地部署 最简单的一种方案是使用ollama, 官网地址是: https://ollama.com

Tips:
1,  ollama --help
2, deepseek-r1
        1.5b  -- 1.1GB(指的是显存)
        7b  -- 4.7GB(指的是显存)
        8b  -- 4.9GB(指的是显存)
        14b  -- 9.0GB(指的是显存)
        32b  -- 20GB(指的是显存)
        70b  -- 43GB(指的是显存)
        671b  -- 404GB(指的是显存， 这个 671b就是所说的 满血版 ) 
3， ollama ps ： 查看运行中的大模型
启动大模型
root@WIN-7MT1R5NQOS1:~# ollama run deepseek-r1:1.5b
root@WIN-7MT1R5NQOS1:~# ollama run qwen2:1.5b

4,  启动 ollama
root@WIN-7MT1R5NQOS1:~# sudo systemctl start ollama
root@WIN-7MT1R5NQOS1:~# sudo systemctl status ollama

第6节 - 06.大模型应用开发-调用大模型
学习笔记:
问题: streamlit run deepseek_model.py 报如下错误?
开放人工智能。AuthenticationError： 错误代码： 401 - {'error'： {'message'： '身份验证失败， 您的 api 密钥： ****Key> 无效'， 'type'： 'authentication_error'， 'param'： 无， 'code'： 'invalid_request_error'}}

        openai.AuthenticationError: Error code: 401 - {'error': {'message': 'Authentication Fails, Your api key: ****Key> is invalid', 'type': 'authentication_error', 'param': None, 'code': 'invalid_request_error'}}
        
        File "/home/dhy/py_code/learn_ai/springai_deepseek/deepseek_model.py", line 8, in <module>
        response = client.chat.completions.create(
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/dhy/py_code/learn_ai/myenv/lib/python3.12/site-packages/openai/_utils/_utils.py", line 287, in wrapper
        return func(*args, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^
        File "/home/dhy/py_code/learn_ai/myenv/lib/python3.12/site-packages/openai/resources/chat/completions/completions.py", line 1087, in create
        return self._post(
        ^^^^^^^^^^^
        File "/home/dhy/py_code/learn_ai/myenv/lib/python3.12/site-packages/openai/_base_client.py", line 1256, in post
        return cast(ResponseT, self.request(cast_to, opts, stream=stream, stream_cls=stream_cls))
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        File "/home/dhy/py_code/learn_ai/myenv/lib/python3.12/site-packages/openai/_base_client.py", line 1044, in request
        raise self._make_status_error_from_response(err.response) from None
解决:
第一步：检查并修复 API 密钥
1，获取正确的 DeepSeek 密钥：

        登录 DeepSeek 控制台(登录 DeepSeek 开放平台)
        
        在 API Keys 中创建或复制有效密钥（以 sk- 开头） ： willdeepseek   sk-fbbc19ef3c0c41a38c7ee9c5fb67037f

2，安全传递密钥（任选一种方式）：
# 方法1：通过环境变量传递（推荐）
        import os
        from openai import OpenAI
        
        client = OpenAI(
        api_key=os.environ["DEEPSEEK_API_KEY"],  # 确保已提前设置环境变量
        base_url="https://api.deepseek.com/v1"    # DeepSeek 专属地址
        )

# 在终端设置环境变量（临时）
export DEEPSEEK_API_KEY='sk-你的真实密钥'

# 永久设置：写入 ~/.bashrc 或 ~/.zshrc
echo "export DEEPSEEK_API_KEY='sk-xxxx'" >> ~/.bashrc
source ~/.bashrc

# 方法2：直接写在代码中（仅测试用，勿提交到Git！）
client = OpenAI(
api_key="sk-你的真实密钥",  # 直接替换这里
base_url="https://api.deepseek.com/v1")

第二步：验证密钥有效性
在终端运行快速测试：

        curl https://api.deepseek.com/v1/models \
        -H "Authorization: Bearer $DEEPSEEK_API_KEY"
加上 sk-fbbc19ef3c0c41a38c7ee9c5fb67037f 就是如下指令

        curl https://api.deepseek.com/v1/models \
        -H "Authorization: Bearer sk-fbbc19ef3c0c41a38c7ee9c5fb67037f"
✅ 成功响应：返回模型列表（如 deepseek-chat）
❌ 失败响应：检查错误信息

第三步：检查代码关键配置
确保代码包含 DeepSeek 专属参数：

        from openai import OpenAI
        
        client = OpenAI(
        api_key="sk-...",              # 替换为你的 DeepSeek 密钥
        base_url="https://api.deepseek.com/v1"  # ⚠️ 必须指定此地址！
        )
        
        response = client.chat.completions.create(
        model="deepseek-chat",         # 指定 DeepSeek 模型
        messages=[{"role": "user", "content": "你好"}]
        )
第四步：账户排查
1，确认已注册 DeepSeek 平台 并开通 API 权限

        2，检查账户额度是否充足（免费额度通常够用）
完整代码示例

        from openai import OpenAI

        # 从环境变量读取密钥（推荐）
        client = OpenAI(
        api_key="sk-fbbc19ef3c0c41a38c7ee9c5fb67037f",
        base_url="https://api.deepseek.com/v1"  # DeepSeek 专属端点
        )
        
        try:
        response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": "1+2等于几？"}]
        )
        print(response.choices[0].message.content)
        except Exception as e:
        print(f"错误: {e}")

💡 关键提醒：
DeepSeek 与 OpenAI 密钥和接口地址不通用

        必须设置 base_url="https://api.deepseek.com/v1"
        
        模型名用 deepseek-chat 或 deepseek-coder


Ollama在本地部署时，会自动提供模型对应的Http接口，访问地址是：http://localhost:11434/api/chat
请求参数如下(用postman调用):

        {
        "model":"deepseek-r1:1.5b",
        "messages":[
        {
        "role":"user",
        "content":"你好，你是谁?"
        }
        ],
        "steam": false
        }

tips：
1，阿里云百炼平台 文本模型 - 文本调试  https://bailian.console.aliyun.com/?spm=5176.29597918.J_SEsSjsNv72yRuRFS2VknO.2.59027b083ojy9q&tab=model#/efm/model_experience_center/text?currentTab=textDebug
   system (设置背景):  你是一个可爱的小毛毛，你的名字叫小毛毛，请以小毛毛的身份和语气来回答问题嘛
   user (用户问问题)：  你是谁?
   assistant (回答结果):  嗨嗨~我是可爱的小毛毛呀！今年刚刚学会用电脑，特别想和大家交朋友呢！我是一只超级萌的小猫咪，最喜欢吃小鱼干和晒太阳啦。我的毛毛又软又暖和，经常被小伙伴们摸摸头呢。你愿意和我做朋友吗？我们可以一起玩耍聊天哦！喵~


第7节 - 07.大模型应用开发-什么是大模型应用
学习笔记:
下面我把常见的一些大模型对话产品及其模型的关系给大家罗列一下：
大模型                      对话产品           公司              地址
GPT-3.5、GPT-4o          ChatGPT         OpenAI          https://chatgpt.com/
Claude 3.5              Claude AI       Anthropic       https://claude.ai/chats
DeepSeek-R1             DeepSeek        深度求索            https://www.deepseek.com/
文心大模型3.5                文心一言            百度              https://yiyan.baidu.com/
星火3.5                   讯飞星火            科大讯飞            https://xinghuo.xfyun.cn/desk
Qwen-Max                通义千问            阿里巴巴            https://tongyi.aliyun.com/qianwen/
Moonshoot               Kimi            月之暗面            https://kimi.moonshot.cn/
Yi-Large                零一万物            零一万物            https://platform.lingyiwanwu.com/


第8节 - 08.大模型应用开发-大模型应用开发技术方案
学习笔记:
1， 目前，大模型应用开发的技术架构主要有四种：
4.1.1 纯Prompt模式
4.1.2 FunctionCalling

        简单来说，可以分为以下步骤：
                1. 我们可以把传统应用中的部分功能封装成一个个函数（Function）。
                   2. 然后在提示词中描述用户的需求，并且描述清楚每个函数的作用，要求AI理解用户意图，判断什么时候需要调用哪个函数，并且将任务拆解为多个步骤（Agent）。
                   3. 当AI执行到某一步，需要调用某个函数时，会返回要调用的函数名称、函数需要的参数信息。
                   4. 传统应用接收到这些数据以后，就可以调用本地函数。再把函数执行结果封装为提示词，再次发送给AI。
                   5. 以此类推，逐步执行，直到达成最终结果。
注意：并不是所有大模型都支持Function Calling，比如DeepSeek-R1模型就不支持。
4.1.3 RAG
4.1.4 Fine-tuning

4.2 技术选型
从开发成本由低到高来看，四种方案排序如下： Prompt < Function Calling < RAG < Fine-tuning

所以我们在选择技术时通常也应该遵循"在达成目标效果的前提下，尽量降低开发成本"这一首要原则。然后可以参考以下流程来思考：

第9节 - 09.SpringAI-课程安排
学习笔记:

第10节 - 10.SpringAI-对话机器人-快速入门
学习笔记:

第11节 - 11.SpringAI-对话机器人-会话日志
学习笔记:

第12节 - 12.SpringAI-对话机器人-对接前端
学习笔记:

第13节 - 13.SpringAI-对话机器人-会话记忆功能下载完整视频
学习笔记:

第14节 - 14.SpringAI-对话机器人-会话历史功能
学习笔记:



