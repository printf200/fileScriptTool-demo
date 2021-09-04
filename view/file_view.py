#!/usr/local/bin/python3

import tkinter as tk

# 创建窗口
from config.file_args import *
from control.file_control import get_file, set_doc_name, set_file_name
from methods.file_tk import set_directory, set_file

window = tk.Tk()

# 设置窗口标题
window.title('文件处理小工具')

# 设置窗口大小，使用小写x
window.geometry("1000x800")

# 创建子容器
container = tk.LabelFrame(window, text="获取文件夹内全部文件名", font=24)
container.grid(row=0, column=0, padx=5, pady=5)
label_choose = tk.Label(container, text="要选择的文件夹", font=30, width=15)

var_choose = tk.StringVar()
var_choose.set('')

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_out_path = tk.Entry(container, textvariable=var_choose, font=(30), width=60)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_path = tk.Button(container, text="设置输入目录", font=(30),
                           command=lambda: set_directory(var_choose))

# 格式排版
label_choose.grid(row=0, column=0, padx=5, pady=5)
label_out_path.grid(row=0, column=1, padx=5, pady=5)
btn_label_path.grid(row=0, column=2, padx=5, pady=5)
# 输出文件夹目录
label_out = tk.Label(container, text="要输出的文件夹", font=30, width=15)

var_out = tk.StringVar()
var_out.set('')

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_out_path = tk.Entry(container, textvariable=var_out, font=(30), width=60)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_out_path = tk.Button(container, text="设置输入目录", font=(30),
                               command=lambda: set_directory(var_out))

# 格式排版
label_out.grid(row=1, column=0, padx=5, pady=5)
label_out_path.grid(row=1, column=1, padx=5, pady=5)
btn_label_out_path.grid(row=1, column=2, padx=5, pady=5)

# 输出文件夹指定名称
label_path = tk.Label(container, text="设置输出的文件名", font=30, width=15)

var_path = tk.StringVar()

var_path.set('')

label_path_out = tk.Entry(container, textvariable=var_path, font=(30), width=60)

# 格式排版
label_path.grid(row=2, column=0, padx=5, pady=5)
label_path_out.grid(row=2, column=1, padx=5, pady=5)

label_radio = tk.Label(container, text="请选择要获取的文件类型", font=30, width=18)

label_radio_type = tk.StringVar()

for file_type, num in voice_types:
    b = tk.Radiobutton(container, text=file_type, variable=label_radio_type, value=file_type)
    b.grid(row=4, column=num, sticky=tk.W)

for doc_type, num1 in doc_types:
    b = tk.Radiobutton(container, text=doc_type, variable=label_radio_type, value=doc_type)
    b.grid(row=5, column=num1, sticky=tk.W)

for image_type, num2 in image_types:
    b = tk.Radiobutton(container, text=image_type, variable=label_radio_type, value=image_type)
    b.grid(row=6, column=num2, sticky=tk.W)

for text_type, num3 in text_types:
    b = tk.Radiobutton(container, text=text_type, variable=label_radio_type, value=text_type)
    b.grid(row=7, column=num3, sticky=tk.W)

for xls_type, num4 in xls_types:
    b = tk.Radiobutton(container, text=xls_type, variable=label_radio_type, value=xls_type)
    b.grid(row=8, column=num4, sticky=tk.W)

# 格式排版
label_radio.grid(row=3, column=0, sticky=tk.W)

label_radio_type.set(0)

# 生成文件类型
label_generate = tk.Label(container, text="请选择要生成的文件类型", font=30, width=18)

label_generate_type = tk.StringVar()

for doc_type_1, index1 in doc_types:
    b = tk.Radiobutton(container, text=doc_type_1, variable=label_generate_type, value=doc_type_1)
    b.grid(row=10, column=index1, sticky=tk.W)

for text_type_1, index2 in text_types:
    b = tk.Radiobutton(container, text=text_type_1, variable=label_generate_type, value=text_type_1)
    b.grid(row=11, column=index2, sticky=tk.W)

for xls_type_1, index3 in xls_types:
    b = tk.Radiobutton(container, text=xls_type_1, variable=label_generate_type, value=xls_type_1)
    b.grid(row=12, column=index3, sticky=tk.W)

# 格式排版
label_generate.grid(row=9, column=0, sticky=tk.W)

label_generate_type.set(0)

btn_get_file_name = tk.Button(container, text='获取文件名称生成指定文件', font=(
    30), command=lambda: get_file(var_choose, var_out, var_path, label_radio_type, label_generate_type))
btn_get_file_name.grid(row=13, column=2, padx=5, pady=5)

# 创建子容器
container_rename = tk.LabelFrame(width=1200, height=800, text="重命名文件", font=24)
container_rename.grid(row=17, column=0, padx=5, pady=5)
# 选择重命名文件夹
label_rename = tk.Label(container_rename, text="选择重命名的文件夹", font=30, width=15)

var_rename = tk.StringVar()

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_rename_file = tk.Entry(container_rename, textvariable=var_rename, font=(30), width=75)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_rename = tk.Button(container_rename, text="设置输入目录", font=(30),
                           command=lambda: set_directory(var_rename))

var_rename.set('')

# 格式排版
label_rename.grid(row=18, column=0, padx=5, pady=5)
label_rename_file.grid(row=18, column=1, padx=5, pady=5)
btn_label_rename.grid(row=18, column=2, padx=5, pady=5)

# 重命名文件夹
label_rename_doc = tk.Label(container_rename, text="重命名的文件夹", font=30, width=15)

var_rename_doc_name = tk.StringVar()

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_rename_doc_name = tk.Entry(container_rename, textvariable=var_rename_doc_name, font=(30), width=75)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_rename_doc = tk.Button(container_rename, text="重命名文件夹", font=(30),
                           command=lambda: set_doc_name(var_rename, var_rename_doc_name))

var_rename_doc_name.set('')

# 格式排版
label_rename_doc.grid(row=19, column=0, padx=5, pady=5)
label_rename_doc_name.grid(row=19, column=1, padx=5, pady=5)
btn_label_rename_doc.grid(row=19, column=2, padx=5, pady=5)


# 选择重命名文件
label_rename_filename = tk.Label(container_rename, text="选择重命名的文件", font=30, width=15)

var_rename_file = tk.StringVar()

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_rename_file_name = tk.Entry(container_rename, textvariable=var_rename_file, font=(30), width=75)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_rename_file = tk.Button(container_rename, text="设置输入文件", font=(30),
                           command=lambda: set_file(var_rename_file))

var_rename_file.set('')

# 格式排版
label_rename_filename.grid(row=20, column=0, padx=5, pady=5)
label_rename_file_name.grid(row=20, column=1, padx=5, pady=5)
btn_label_rename_file.grid(row=20, column=2, padx=5, pady=5)

# 重命名文件
label_rename_files = tk.Label(container_rename, text="重命名的文件", font=30, width=15)

var_rename_files_name = tk.StringVar()

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_rename_files_name = tk.Entry(container_rename, textvariable=var_rename_files_name, font=(30), width=75)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_rename_files = tk.Button(container_rename, text="重命名文件", font=(30),
                           command=lambda: set_file_name(var_rename_file, var_rename_files_name))

var_rename_files_name.set('')

# 格式排版
label_rename_files.grid(row=21, column=0, padx=5, pady=5)
label_rename_files_name.grid(row=21, column=1, padx=5, pady=5)
btn_label_rename_files.grid(row=21, column=2, padx=5, pady=5)



# 进入消息循环, window不断刷新
window.mainloop()



if __name__ == "__main__":
    print("begin run " + __file__)
