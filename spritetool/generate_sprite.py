from PIL import Image
import json
import os

def generate_sprite(images_folder, output_sprite_path, output_json_path):
    # 获取文件夹中的所有PNG图像文件路径
    png_files = [file for file in os.listdir(images_folder) if file.endswith('.png')]

    # 读取所有图像并获取最大宽度和总高度
    images = []
    max_width = 0
    max_height = 0
    for png_file in png_files:
        image = Image.open(os.path.join(images_folder, png_file))
        images.append((png_file, image))
        max_width = max(max_width, image.width)
        max_height = max(max_height, image.height)

      # 计算合并后图片的行数和列数
    num_images = len(images)
    num_rows = int((num_images - 1) ** 0.5) + 1
    num_cols = (num_images + num_rows - 1) // num_rows

    # 计算合并后图片的宽度和高度
    output_width = max_width * num_cols
    output_height = max_height * num_rows

    # 初始化sprite图像和JSON描述文件
    sprite_image = Image.new('RGBA', (output_width, output_height), (255, 255, 255, 0))
    sprite_json = {}

    # 初始化偏移量
    x_offset = 0
    y_offset = 0

    # 逐个将图像粘贴到sprite图像中
    for png_file, image in images:
        # 如果当前行已经放不下当前图标，换行
        if x_offset + image.width > sprite_image.width:
            x_offset = 0
            y_offset += max_height
            num_rows -= 1

        # 将图标粘贴到sprite图像中
        sprite_image.paste(image, (x_offset, y_offset))

        # 记录图标的位置和大小信息
        sprite_json[png_file] = {
            'x': x_offset,
            'y': y_offset,
            'width': image.width,
            'height': image.height,
            'pixelRatio': 1,
        }

        # 更新x偏移量
        x_offset += max_width

    # 保存sprite图像
    sprite_image.save(output_sprite_path)

    # 保存sprite JSON描述文件
    with open(output_json_path, 'w') as f:
        json.dump(sprite_json, f, indent=4)

    print("Sprite图像和JSON描述文件已生成！")

# 使用示例
images_folder = "output_icons"        # 包含PNG图像的文件夹路径
output_sprite_path = "genrate_sprite/sprite.png"     # 输出的sprite图像路径
output_json_path = "genrate_sprite/sprite.json"      # 输出的sprite JSON描述文件路径

generate_sprite(images_folder, output_sprite_path, output_json_path)
