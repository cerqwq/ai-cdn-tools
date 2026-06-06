# 🌐 AI CDN Tools

AI CDN工具，支持CDN配置、缓存策略、性能优化。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🏗️ CDN策略设计
- ⚙️ Cloudflare配置
- 📋 缓存规则设计
- 🖥️ Nginx CDN配置
- ⚡ 性能优化
- ⚖️ 提供商比较

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_cdn_tools import create_tools

tools = create_tools()

# CDN策略
cdn = tools.design_cdn_strategy("电商网站", ["中国", "东南亚"])

# Cloudflare配置
cloudflare = tools.generate_cloudflare_config("example.com", ["缓存", "安全"])

# 缓存规则
cache = tools.design_cache_rules(["HTML", "CSS", "JS", "图片"])

# Nginx CDN
nginx = tools.generate_nginx_cdn("http://backend", "/var/cache/nginx")

# 性能优化
optimized = tools.optimize_cdn_performance(metrics)

# 提供商比较
comparison = tools.compare_cdn_providers(["高性能", "低成本"])
```

## 📁 项目结构

```
ai-cdn-tools/
├── tools.py       # CDN工具核心
└── README.md
```

## 📄 许可证

MIT License
