import os
import re
import configparser
from tkinter import Tk
from tkinter.filedialog import askdirectory
from pydub import AudioSegment

# 读取配置文件
config = configparser.ConfigParser()
config_file = 'config.ini'
if os.path.exists(config_file):
    config.read(config_file)
    numbers_folder = config.get('Paths', 'numbers_folder', fallback=None)
else:
    numbers_folder = None

# 创建一个Tkinter根窗口并隐藏它
root = Tk()
root.withdraw()

# 获取Numbers文件夹
if numbers_folder is None:
    print("请选择Numbers文件夹")
    numbers_folder = askdirectory(title="选择Numbers文件夹")
    # 保存Numbers文件夹路径到配置文件
    config['Paths'] = {'numbers_folder': numbers_folder}
    with open(config_file, 'w') as configfile:
        config.write(configfile)

# 提示用户选择Recording文件夹
print("请选择Recording文件夹")
recording_folder = askdirectory(title="选择Recording文件夹")

# 检查文件夹是否存在
if not os.path.exists(numbers_folder) or not os.path.exists(recording_folder):
    print("所选文件夹不存在，请检查路径。")
else:
    # 遍历Numbers文件夹中的所有文件
    for filename in os.listdir(numbers_folder):
        if filename.endswith('.wav'):
            # 构建完整的文件路径
            numbers_file = os.path.join(numbers_folder, filename)
            recording_file = os.path.join(recording_folder, filename)

            # 检查Recording文件夹中是否存在同名文件
            if os.path.exists(recording_file):
                try:
                    # 加载音频文件
                    audio1 = AudioSegment.from_wav(numbers_file)
                    audio2 = AudioSegment.from_wav(recording_file)

                    # 合并音频文件
                    combined_audio = audio1 + audio2

                    # 保存合并后的文件
                    output_file = os.path.join(os.getcwd(), f"combined_{filename}")
                    combined_audio.export(output_file, format="wav")
                    print(f"已合并 {filename} 并保存为 {output_file}")
                except Exception as e:
                    print(f"合并 {filename} 时出错: {e}")
            else:
                print(f"Recording文件夹中不存在 {filename}，跳过。")

    # 获取合并后的所有文件
    combined_files = [f for f in os.listdir(os.getcwd()) if f.startswith("combined_") and f.endswith('.wav')]

    # 定义自然排序函数
    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

    # 按自然数字顺序排序
    combined_files.sort(key=natural_sort_key)

    if combined_files:
        # 初始化最终合并的音频
        final_combined_audio = AudioSegment.empty()

        # 依次合并所有文件
        for file in combined_files:
            file_path = os.path.join(os.getcwd(), file)
            audio = AudioSegment.from_wav(file_path)
            final_combined_audio += audio

        # 获取Recording文件夹的名字
        recording_folder_name = os.path.basename(recording_folder)
        final_output_file = os.path.join(recording_folder, f"{recording_folder_name}.wav")

        # 保存最终合并的文件
        final_combined_audio.export(final_output_file, format="wav")
        print(f"已将所有合并后的文件合并并保存为 {final_output_file}")

        # 删除过程文件
        for file in combined_files:
            file_path = os.path.join(os.getcwd(), file)
            os.remove(file_path)
            print(f"已删除过程文件 {file_path}")
    else:
        print("没有找到合并后的文件。")