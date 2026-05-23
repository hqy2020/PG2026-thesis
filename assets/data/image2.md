图像生成
第三方 API 接入
使用 API Key 调用开放接口，适合 Python 脚本、自动化任务和外部系统。
基础地址
https://mikucode.xyz
生图接口
POST /v1/images/generations
改图接口
POST /v1/images/edits
鉴权：请求头使用 Authorization: Bearer <API Key>。
令牌分组：在令牌页面创建 API Key，令牌分组决定可用渠道、模型权限和计费。
响应：兼容 OpenAI Images 响应，可能返回 b64_json 或 url；脚本需要自行解码或下载保存。
官网内部 /pg/images/* 依赖网页登录态，不建议第三方接入。
Python 示例依赖 requests，可先执行 pip install requests。
改图上传多张参考图时重复传入 image[] 字段；只改一张图时传入一个 image[] 即可。
页面内 /pg/images/* 会携带 group；/v1/images/* 走 API Key 的令牌分组。
常用参数
model - 模型名称
prompt - 提示词
n - 数量
size - 预设尺寸或自定义 WxH，最长边不超过 3840，宽高比不超过 3:1
quality - auto | low | medium | high
output_format - png | jpeg | webp
output_compression - 仅 jpeg/webp 可用，0 到 100，100 通常省略
group - 页面请求会携带分组，后端按该分组路由到对应渠道
image[] - 改图时上传的图片文件，可重复传入多张
安装 Python 依赖bash
pip install requests
Python 生图并保存python
import base64
import pathlib
import requests

BASE_URL = "https://mikucode.xyz"
API_KEY = "sk-xxxx"
OUTPUT_FILE = pathlib.Path("image.png")

response = requests.post(
    BASE_URL + "/v1/images/generations",
    headers={"Authorization": "Bearer " + API_KEY},
    json={
            "model": "gpt-image-2",
            "prompt": "一只白色小猫坐在窗边，柔和自然光，照片风格",
            "n": 1,
            "size": "1024x1024",
            "quality": "auto",
            "output_format": "png"
    },
    timeout=120,
)
response.raise_for_status()
payload = response.json()
image = payload["data"][0]

if image.get("b64_json"):
    OUTPUT_FILE.write_bytes(base64.b64decode(image["b64_json"]))
elif image.get("url"):
    image_response = requests.get(image["url"], timeout=120)
    image_response.raise_for_status()
    OUTPUT_FILE.write_bytes(image_response.content)
else:
    raise RuntimeError("No image data returned")

print("saved to", OUTPUT_FILE)
Python 改图并保存python
import base64
import contextlib
import pathlib
import requests

BASE_URL = "https://mikucode.xyz"
API_KEY = "sk-xxxx"
INPUT_FILES = [
    pathlib.Path("reference-1.png"),
    pathlib.Path("reference-2.png"),
]
OUTPUT_FILE = pathlib.Path("edited.png")

with contextlib.ExitStack() as stack:
    image_files = [
        stack.enter_context(input_file.open("rb"))
        for input_file in INPUT_FILES
    ]
    response = requests.post(
        BASE_URL + "/v1/images/edits",
        headers={"Authorization": "Bearer " + API_KEY},
        data={
            "model": "gpt-image-2",
            "prompt": "保留主体构图，改成黄昏电影感光线",
            "n": "1",
            "size": "1024x1024",
            "quality": "auto",
            "output_format": "png",
        },
        files=[
            ("image[]", (input_file.name, image_file, "image/png"))
            for input_file, image_file in zip(INPUT_FILES, image_files)
        ],
        timeout=120,
    )
response.raise_for_status()
payload = response.json()
image = payload["data"][0]

if image.get("b64_json"):
    OUTPUT_FILE.write_bytes(base64.b64decode(image["b64_json"]))
elif image.get("url"):
    image_response = requests.get(image["url"], timeout=120)
    image_response.raise_for_status()
    OUTPUT_FILE.write_bytes(image_response.content)
else:
    raise RuntimeError("No image data returned")

print("saved to", OUTPUT_FILE)
cURL 生图bash
BASE_URL="https://mikucode.xyz"
API_KEY="sk-xxxx"

curl -X POST "$BASE_URL/v1/images/generations" \
  -H "Authorization: Bearer $API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "model": "gpt-image-2",
  "prompt": "一只白色小猫坐在窗边，柔和自然光，照片风格",
  "n": 1,
  "size": "1024x1024",
  "quality": "auto",
  "output_format": "png"
}'
cURL 改图bash
BASE_URL="https://mikucode.xyz"
API_KEY="sk-xxxx"

curl -X POST "$BASE_URL/v1/images/edits" \
  -H "Authorization: Bearer $API_KEY" \
  -F model="gpt-image-2" \
  -F prompt="保留主体构图，改成黄昏电影感光线" \
  -F n="1" \
  -F size="1024x1024" \
  -F quality="auto" \
  -F output_format="png" \
  -F "image[]=@reference-1.png" \
  -F "image[]=@reference-2.png"
© 2026 MikuCode. 版权所有
