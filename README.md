# Weather AI Assistant

一个基于 FastAPI 和 OpenAI 的天气智能助手项目。

## 项目简介

本项目实现了一个天气问答系统，支持三种模式：

1. **工具模式 `/chat`**
   - 先从自然语言中提取城市
   - 再查询天气数据
   - 最后基于天气数据生成建议
   - 特点：准确、可控，但响应稍慢

2. **快速模式 `/chat2`**
   - 直接由大模型根据用户问题生成回答
   - 特点：响应快，但可能偏离预设天气数据

3. **自动路由模式 `/chat_router`**
   - 先判断问题类型
   - 天气相关问题走工具模式
   - 其他问题走快速模式
   - 特点：平衡准确性与响应速度

## 技术栈

- Python
- FastAPI
- Uvicorn
- OpenAI API
- Git / GitHub

## 项目结构

```text
weather_project/
├── app.py
├── llm_service.py
├── main.py
└── README.md
````

## 运行方式

### 1. 安装依赖

```bash
pip install fastapi uvicorn openai
```

### 2. 配置环境变量

Windows Git Bash:

```bash
export OPENAI_API_KEY="你的API_KEY"
```

### 3. 启动服务

```bash
uvicorn app:app --reload
```

### 4. 打开文档

```text
http://127.0.0.1:8000/docs
```

## 接口说明

### `/health`

健康检查接口

### `/weather?city=beijing`

返回天气信息

### `/chat?query=北京今天适合穿什么？`

严格工具模式

### `/chat2?query=北京今天适合穿什么？`

快速模式

### `/chat_router?query=北京今天适合穿什么？`

自动路由模式

## 设计思路

本项目重点对比了两类 LLM 应用架构：

### 1. Tool-based

流程：
自然语言 -> 提取城市 -> 查询天气 -> 生成建议

优点：

* 准确
* 可控
* 结果与天气数据一致

缺点：

* 延迟较高
* 调用链路更长

### 2. Prompt-based

流程：
自然语言 -> 单次 LLM 回答

优点：

* 速度快
* 实现简单

缺点：

* 可能出现幻觉
* 可能偏离工具数据

### 3. Router-based

根据问题类型自动选择链路，在准确性、速度和成本之间做平衡。

## 当前收获

通过这个项目，我掌握了：

* Git / GitHub 基本工作流
* FastAPI 接口开发
* LLM API 调用
* Prompt 优化
* 多链路 AI 系统设计
* Tool-based 与 Prompt-based 架构对比



