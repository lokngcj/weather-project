# Weather AI Assistant

一个基于 FastAPI 和大模型 API 的天气智能助手项目，支持多种问答链路与自动路由策略。

---

## 🚀 项目简介

本项目实现了一个天气问答系统，支持三种模式：

### 1️⃣ 工具模式 `/chat`

* 从自然语言中提取城市
* 查询天气数据
* 基于天气数据生成建议
  👉 特点：**准确、可控，但响应较慢**

---

### 2️⃣ 快速模式 `/chat2`

* 直接由大模型根据用户问题生成回答
  👉 特点：**响应快，但可能偏离预设天气数据**

---

### 3️⃣ 自动路由模式 `/chat_router`

* 判断问题类型
* 天气问题 → 工具模式
* 其他问题 → 快速模式
  👉 特点：**平衡准确性与响应速度**

---

📌 项目同时提供：

* ✅ GET 调试接口
* ✅ POST 正式接口（更接近真实服务）

---

## 🧱 技术栈

* Python
* FastAPI
* Uvicorn
* OpenAI / DeepSeek API
* python-dotenv
* Git / GitHub

---

## 📁 项目结构

```text
weather_project/
├── app/
│   ├── main.py                # FastAPI入口
│   └── services/
│       ├── llm_service.py     # LLM逻辑（提取城市 / 生成建议）
│       └── weather_service.py # 天气数据处理
├── README.md
├── requirements.txt
└── .env
```

---

## ⚙️ 运行方式

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

或：

```bash
pip install fastapi uvicorn openai python-dotenv
```

---

### 2. 配置环境变量

在项目根目录创建 `.env`：

```env
OPENAI_API_KEY=你的API_KEY
```

---

### 3. 启动服务

```bash
uvicorn app.main:app --reload
```

---

### 4. 打开接口文档

```text
http://127.0.0.1:8000/docs
```

---

## 📡 接口说明

---

### 🔹 `GET /health`

健康检查接口

---

### 🔹 `GET /weather?city=beijing`

返回天气信息

---

### 🔹 `GET /chat?query=北京今天适合穿什么？`

工具模式（结构化 → 工具 → LLM）

---

### 🔹 `GET /chat2?query=北京今天适合穿什么？`

快速模式（单次 LLM）

---

### 🔹 `GET /chat_router?query=北京今天适合穿什么？`

自动路由模式

---

### 🔥 `POST /chat_router`（推荐）

正式聊天接口

#### 请求：

```json
{
  "query": "北京今天适合穿什么？"
}
```

#### 响应：

```json
{
  "success": true,
  "mode": "tool",
  "data": {
    "query": "北京今天适合穿什么？",
    "city": "beijing",
    "weather": "晴朗，温度25°C",
    "advice": "北京今天晴朗25°C，建议穿轻薄长袖或短袖。"
  }
}
```

---

## 🧠 系统设计

---

### 🔹 Tool-based 模式

流程：

```text
用户输入
→ LLM 提取城市
→ 查询天气数据
→ LLM 生成建议
→ 返回结果
```

优点：

* 准确
* 可控
* 与数据源一致

缺点：

* 延迟较高
* 多次模型调用

---

### 🔹 Prompt-based 模式

流程：

```text
用户输入
→ 单次 LLM 生成回答
→ 返回结果
```

优点：

* 响应快
* 实现简单

缺点：

* 可能出现幻觉
* 与数据源不一致

---

### 🔹 Router 模式

流程：

```text
用户输入
→ 路由判断
→ 选择 Tool / Fast
→ 执行对应链路
→ 返回结果
```

👉 在准确性、速度、成本之间做平衡

---

## 📊 性能与链路对比

### Tool 模式

* 查询：北京今天适合穿什么？
* 流程：2 次 LLM + 工具调用
* 耗时：约 **6.12 秒**

---

### Fast 模式

* 查询：你好，你是谁？
* 流程：1 次 LLM
* 耗时：约 **3.20 秒**

---

### 📌 结论

* Tool 模式 → 更适合**高准确性场景**
* Fast 模式 → 更适合**低延迟场景**
* Router 模式 → 实现**智能折中**

---

## 🧩 工程特性

* 模块化结构（services 分层）
* 支持 GET + POST 两种接口
* 使用 `.env` 管理 API Key
* 基础日志系统（记录链路 / 城市提取 / 状态）
* 请求耗时统计（性能分析）
* 多链路 AI 系统设计（Tool / Prompt / Router）

---

## 📚 当前收获

通过本项目，我掌握了：

* Git / GitHub 工作流
* FastAPI 后端开发
* LLM API 调用
* Prompt 工程（控制输出）
* 自然语言 → 结构化数据
* 多链路 AI 架构设计
* Tool-based vs Prompt-based 对比
* 路由层设计（Agent 雏形）

---

## 🎯 项目亮点（面试重点）

* 实现三种 AI 推理链路并进行对比分析
* 设计自动路由系统平衡准确性与延迟
* 引入日志与耗时统计进行性能验证
* 完整工程结构（配置管理 + 模块化 + API设计）

---
