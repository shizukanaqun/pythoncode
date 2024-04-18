from PIL import Image
import json

def split_sprite(sprite_image_path, sprite_json_path, output_folder):
    # 读取sprite的JSON描述文件
    with open(sprite_json_path, 'r') as f:
        sprite_data = json.load(f)

    # 打开sprite图像
    sprite_image = Image.open(sprite_image_path)

    # 遍历JSON数据中的每个图标描述
    for icon_name, icon_info in sprite_data.items():
        # 从JSON中提取图标的位置和大小信息
        x, y = icon_info['x'], icon_info['y']
        width, height = icon_info['width'], icon_info['height']

        # 根据位置和大小裁剪图像
        icon_image = sprite_image.crop((x, y, x + width, y + height))

        # 保存裁剪后的图像
        icon_image.save(f"{output_folder}/{icon_name}.png")

    print("图像分割完成！")

# 使用示例
sprite_image_path = "sprite.png"  # sprite图像路径
sprite_json_path = "sprite.json"  # sprite JSON描述文件路径
output_folder = "output_icons"    # 保存分割图像的文件夹路径

split_sprite(sprite_image_path, sprite_json_path, output_folder)
