"""
AI CDN Tools - AI CDN工具
支持CDN配置、缓存策略、性能优化
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AICDNTools:
    """
    AI CDN工具
    支持：配置、缓存、优化
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def design_cdn_strategy(self, website: str, regions: List[str]) -> Dict:
        """设计CDN策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        regions_text = ", ".join(regions)

        prompt = f"""请为{website}设计CDN策略：

覆盖区域：{regions_text}

请返回JSON格式：
{{
    "provider": "推荐提供商",
    "edge_locations": ["边缘节点"],
    "caching_rules": ["缓存规则"],
    "purge_strategy": "清除策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"cdn": content}

    def generate_cloudflare_config(self, domain: str, features: List[str]) -> str:
        """生成Cloudflare配置"""
        if not self.client:
            return "LLM客户端未配置"

        features_text = ", ".join(features)

        prompt = f"""请为{domain}生成Cloudflare配置：

功能：{features_text}

要求：
1. DNS配置
2. 缓存规则
3. 安全规则"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def design_cache_rules(self, content_types: List[str]) -> Dict:
        """设计缓存规则"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        types_text = ", ".join(content_types)

        prompt = f"""请设计缓存规则：

内容类型：{types_text}

请返回JSON格式：
{{
    "rules": [
        {{"content_type": "类型", "ttl": "TTL", "cache_key": "缓存键"}}
    ],
    "invalidation": "失效策略"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"cache": content}

    def generate_nginx_cdn(self, upstream: str, cache_path: str) -> str:
        """生成Nginx CDN配置"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请生成Nginx CDN配置：

上游：{upstream}
缓存路径：{cache_path}

要求：
1. 代理配置
2. 缓存配置
3. 压缩配置"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        return response.choices[0].message.content

    def optimize_cdn_performance(self, metrics: Dict) -> Dict:
        """优化CDN性能"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        metrics_text = json.dumps(metrics, ensure_ascii=False)

        prompt = f"""请优化CDN性能：

{metrics_text}

请返回JSON格式：
{{
    "issues": ["问题"],
    "optimizations": ["优化建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"optimization": content}

    def compare_cdn_providers(self, requirements: List[str]) -> Dict:
        """比较CDN提供商"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        req_text = ", ".join(requirements)

        prompt = f"""请比较CDN提供商：

需求：{req_text}

请返回JSON格式：
{{
    "providers": [
        {{"name": "提供商", "strengths": ["优势"], "weaknesses": ["劣势"]}}
    ],
    "recommendation": "推荐"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"comparison": content}


def create_tools(**kwargs) -> AICDNTools:
    """创建CDN工具"""
    return AICDNTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI CDN Tools")
    print()

    # 测试
    cdn = tools.design_cdn_strategy("电商网站", ["中国", "东南亚"])
    print(json.dumps(cdn, ensure_ascii=False, indent=2))
