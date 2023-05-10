from PIL import Image

def add_padding():
    # 打开图片
    image = Image.open("C:/Users/User/Desktop/计算机软件综合实验/计算机软件综合实验/navigation/resource/bg.png")

    # 获取原始图片的宽度和高度
    width, height = image.size

    # 计算填充后的图片宽度
    new_width = width + 10 * width

    # 创建一个新的图片对象，宽度为填充后的宽度，高度不变
    new_image = Image.new("RGB", (new_width, height), "white")

    # 计算图片在新图片中的左边距
    left_margin = 5 * width

    # 将原始图片粘贴到新图片中
    new_image.paste(image, (left_margin, 0))

    # 保存填充后的图片
    new_image.save("C:/Users/User/Desktop/计算机软件综合实验/计算机软件综合实验/navigation/resource/test02.png")

    print("图片填充完成！")

# 输入图片的文件路径
# 调用函数进行图片填充
add_padding()

