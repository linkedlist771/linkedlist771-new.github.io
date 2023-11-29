import os
import shutil

typro_image_dir_path = r"C:\Users\23174\AppData\Roaming\Typora\typora-user-images"
hexo_image_dir_path = r"C:\Users\23174\Desktop\blog\blog\source\images"

# 遍历Typora图片目录中的所有文件
for image_name in os.listdir(typro_image_dir_path):
    source_image_path = os.path.join(typro_image_dir_path, image_name)
    target_image_path = os.path.join(hexo_image_dir_path, image_name)

    # 检查目标目录中是否已经存在同名文件
    # 如果不存在，则复制
    try:
        shutil.copy(source_image_path, target_image_path)
        print(f"Copied {image_name} to Hexo image directory.")
    except Exception as e:
        print(f"Failed to copy {image_name} to Hexo image directory with error: {e}")
    else:
        print(f"{image_name} already exists in Hexo image directory. Skipping.")

# 然后修改其中md的图片路径
# 遍历当前文件夹下（包括子文件夹）的所有以md结尾的文件
# 将 ../../../../../AppData/Roaming/Typora/typora-user-images/
# 替换为 ../images/

def replace_image_path_in_md_files(root_dir):
    # 遍历当前文件夹及其子文件夹
    for foldername, subfolders, filenames in os.walk(root_dir):
        for filename in filenames:
            # 检查文件是否以.md结尾
            if filename.endswith('.md'):
                file_path = os.path.join(foldername, filename)
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_contents = file.read()
                    
                    # 替换图片路径
                    pattern1 = r'../../../../../AppData/Roaming/Typora/typora-user-images/'
                    pattern2 = r'../../../../AppData/Roaming/Typora/typora-user-images/'
                    pattern3 = r'C:/Users/23174/AppData/Roaming/Typora/typora-user-images/'
                    if pattern1 in file_contents:
                        new_contents = file_contents.replace(
                            pattern1,
                            r'../images/'
                        )
                    elif pattern2 in file_contents:
                        new_contents = new_contents.replace(
                            pattern2,
                            r'../images/'

                        )
                    elif pattern3 in file_contents:
                        new_contents = new_contents.replace(
                            pattern3,
                            r'../images/'
                        )
                    else:
                        new_contents = ""

                
                # 如果内容有变化，写回文件
                if new_contents != file_contents:
                    with open(file_path, 'w', encoding='utf-8') as file:
                        file.write(new_contents)
                    print(f"Updated image paths in {file_path}")

# 调用函数，传入你想开始搜索的根目录（这里是当前目录）

replace_image_path_in_md_files(os.getcwd())

# wait for user input to exit
input("Press Enter to exit.")