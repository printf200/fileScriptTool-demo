import tkinter.filedialog as tk_fld
import tkinter.messagebox as messagebox


# 设置目录
def set_directory(arg):
    set_path = tk_fld.askdirectory()
    arg.set(set_path)


# 提示窗口
def msg_box(arg):
    messagebox.showinfo("提示窗口", arg)


def set_file(arg):
    file_name = tk_fld.askopenfilename()
    arg.set(file_name)
