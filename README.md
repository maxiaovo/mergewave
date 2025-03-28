### 脚本说明文档

#### 1. 脚本概述
此 Python 脚本用于合并两个文件夹中的 `.wav` 音频文件。具体来说，它会将 `Numbers` 文件夹和 `Recording` 文件夹中同名的 `.wav` 文件进行合并，然后将合并后的所有文件按照自然数字顺序再次合并成一个最终的音频文件，最终文件将存储在 `Recording` 文件夹中。同时，脚本会将 `Numbers` 文件夹的路径存储在配置文件中，避免用户每次都需要手动选择。合并完成后，脚本会自动删除合并过程中产生的临时文件。

#### 2. 依赖库
运行此脚本需要安装以下 Python 库：
- `os`：用于文件和目录操作。
- `re`：用于正则表达式处理，实现自然排序。
- `configparser`：用于读取和写入配置文件。
- `tkinter`：用于创建图形用户界面，方便用户选择文件夹。
- `pydub`：用于音频文件的加载、合并和导出。

你可以使用以下命令安装 `pydub`：
```bash
pip install pydub
```

#### 3. 配置文件
脚本使用 `config.ini` 文件来存储 `Numbers` 文件夹的路径。如果该文件不存在，脚本会提示用户选择 `Numbers` 文件夹，并将路径保存到该文件中。配置文件的格式如下：
```ini
[Paths]
numbers_folder = /path/to/numbers/folder
```

#### 4. 使用步骤
1. **运行脚本**：在命令行中执行以下命令来运行脚本：
```bash
python /Users/maxiao/Desktop/mergewav.py
```
2. **选择文件夹**：
    - 如果 `config.ini` 文件中没有存储 `Numbers` 文件夹的路径，脚本会弹出一个文件夹选择对话框，让你选择 `Numbers` 文件夹。选择完成后，路径会被保存到 `config.ini` 文件中。
    - 接着，脚本会弹出另一个文件夹选择对话框，让你选择 `Recording` 文件夹。
3. **等待合并完成**：脚本会自动合并 `Numbers` 文件夹和 `Recording` 文件夹中同名的 `.wav` 文件，并将合并后的文件保存到当前工作目录中。然后，脚本会将所有合并后的文件按照自然数字顺序再次合并成一个最终的音频文件，最终文件将存储在 `Recording` 文件夹中。
4. **查看结果**：合并完成后，你可以在 `Recording` 文件夹中找到最终的音频文件，文件名与 `Recording` 文件夹的名称相同。同时，合并过程中产生的临时文件会被自动删除。

#### 5. 注意事项
- 确保 `Numbers` 文件夹和 `Recording` 文件夹中包含同名的 `.wav` 文件，否则脚本会跳过这些文件。
- 脚本会覆盖 `Recording` 文件夹中的原文件，请确保在运行脚本之前备份重要数据。
- 如果脚本在运行过程中出现错误，请检查文件夹路径是否正确，以及依赖库是否安装正确。
