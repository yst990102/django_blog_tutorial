import re
import os
from urllib.parse import unquote

def rewrite_image_links(md_file):
    md_filename = os.path.splitext(md_file)[0]
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
        image_urls = re.findall(r"!\[.*\]\((.*?)\)", content)
        for img_url in image_urls:
            decoded_url = unquote(img_url)
            img_name = os.path.basename(decoded_url)
            updated_url = f"![](./assets/{md_filename.replace('md', '')}/{img_name})"
            content = content.replace(img_url, updated_url)
    
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"图片链接已成功改写并保存到 {md_file}")

# 调用函数并传入Markdown文件路径
for file in os.scandir('.'):
    if file.name.endswith('md'):
        rewrite_image_links(file.name)