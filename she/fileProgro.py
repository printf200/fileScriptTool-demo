#!/usr/local/bin/python3

import tkinter as tk
import tkinter.filedialog as tk_fld
import tkinter.messagebox as messagebox
import os

voice_types = [
    ("pcm", 0),
    ("wav", 1)
]
text_types = [
    ("text", 0),
    ("txt", 1)
]
doc_types = [
    ("doc", 0),
    ("docx", 1)
]

xls_types = [
    ("xls", 0),
    ("xlsx", 1)
]

image_types = [
    ("jpg", 0),
    ("png", 1)
]


def set_directory(arg):
    set_path = tk_fld.askdirectory()
    arg.set(set_path)


def msg_box(arg):
    messagebox.showinfo("提示窗口", arg)


def get_type(arg):
    print(arg)


def get_file(choose, out, arg_type):
    if arg_type.get() == '0':
        msg_box("类型不允许为空！")
    else:
        file_name_arr = get_folder_file_name(choose, arg_type.get())
        out_file(out, file_name_arr)
        msg_box("写入成功")
        var_choose.set('')
        var_out.set('')

# 获取文件夹内指定文件类型名称
def get_folder_file_name(choose, arg):
    list_arr = []
    for root, dirs, files in os.walk(choose.get()):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        for f in files:
            if f.endswith(arg):
                file_name = os.path.join(root, f)
                new_file_name = file_name.replace(choose.get(), '').replace('/', '') + ":" + "\n"
                list_arr.append(new_file_name)

    return list_arr


# 生成文本
def out_file(out, arr):
    full_path = "result" + '.txt'  # 也可以创建一个.doc的word文档
    file = open(out.get() + '/' + full_path, 'w')  # w 的含义为可进行读写
    for value in arr:
        file.write(value)

    file.close()


# 创建窗口
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

# 文本属性textvariable  可变文本，与StringVar等配合着用
label_out_path = tk.Entry(container, textvariable=var_choose, font=(30), width=60)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_path = tk.Button(container, text="设置输入目录", font=(30),
                           command=lambda: set_directory(var_choose))

# 格式排版
label_choose.grid(row=0, column=0, padx=5, pady=5)
label_out_path.grid(row=0, column=1, padx=5, pady=5)
btn_label_path.grid(row=0, column=2, padx=5, pady=5)

label_out = tk.Label(container, text="要输出的文件夹", font=30, width=15)

var_out = tk.StringVar()
# 文本属性textvariable  可变文本，与StringVar等配合着用
label_out_path = tk.Entry(container, textvariable=var_out, font=(30), width=60)

# 设置输入目录 command: 指定按钮消息的回调函数；
btn_label_out_path = tk.Button(container, text="设置输入目录", font=(30),
                               command=lambda: set_directory(var_out))

# 格式排版
label_out.grid(row=1, column=0, padx=5, pady=5)
label_out_path.grid(row=1, column=1, padx=5, pady=5)
btn_label_out_path.grid(row=1, column=2, padx=5, pady=5)

label_radio = tk.Label(container, text="请选择要获取的文件类型", font=30, width=18)

label_radio_type = tk.StringVar()

for file_type, num in voice_types:
    b = tk.Radiobutton(container, text=file_type, variable=label_radio_type, value=file_type)
    b.grid(row=3, column=num, sticky=tk.W)

for doc_type, num1 in doc_types:
    b = tk.Radiobutton(container, text=doc_type, variable=label_radio_type, value=doc_type)
    b.grid(row=4, column=num1, sticky=tk.W)

for image_type, num2 in image_types:
    b = tk.Radiobutton(container, text=image_type, variable=label_radio_type, value=image_type)
    b.grid(row=5, column=num2, sticky=tk.W)

for text_type, num3 in text_types:
    b = tk.Radiobutton(container, text=text_type, variable=label_radio_type, value=text_type)
    b.grid(row=6, column=num3, sticky=tk.W)

for xls_type, num4 in xls_types:
    b = tk.Radiobutton(container, text=xls_type, variable=label_radio_type, value=xls_type)
    b.grid(row=7, column=num4, sticky=tk.W)

# 格式排版
label_radio.grid(row=2, column=0, sticky=tk.W)

label_radio_type.set(0)

btn_get_file_name = tk.Button(container, text='获取文件名称生成指定文件', font=(
    30), command=lambda: get_file(var_choose, var_out, label_radio_type))
btn_get_file_name.grid(row=8, column=2, padx=5, pady=5)

# 进入消息循环, window不断刷新
window.mainloop()

if __name__ == "__main__":
    print("begin run " + __file__)
