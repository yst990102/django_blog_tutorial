import re
import requests
import os
from urllib.parse import unquote

def save_images_from_md(md_file, folder):
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        image_urls = re.findall(r"!\[.*\]\((.*?)\)", content)
        for img_url in image_urls:
            response = requests.get(img_url)
            if response.status_code == 200:
                os.makedirs(f"{folder}\{md_file.replace('.md', '')}", exist_ok=True)
                img_name = unquote(img_url.split('/')[-1])  # 解码URL编码的文件名
                file_path = os.path.join(folder, md_file.replace('.md', ''), img_name)
                with open(file_path, 'wb') as file:
                    file.write(response.content)
                print(f"图片 {img_url} 已成功下载并保存到 {file_path}")
            else:
                print(f"图片 {img_url} 下载失败")

# 调用函数并传入Markdown文件路径和保存文件夹路径
for file in os.scandir('.'):
    if file.name.endswith('md'):
        save_images_from_md(file.name, "assets")