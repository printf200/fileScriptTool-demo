from config.common_args import clear
from methods.file_func import name_handling, get_folder_file_name, out_file
from methods.file_tk import msg_box


# 处理重命名文件夹命名
def set_doc_name(old, new):
    if old.get() == '' or new.get() == '':
        msg_box("未选择重命名文件或未填写修改文件夹名称！")
    else:
        name_handling(old, new)
        msg_box("重命名成功")
        clear(old, new)


# 处理重命名文件
def set_file_name(old, new):
    if old.get() == '' or new.get() == '':
        msg_box("未选择重命名文件或未填写修改文件夹名称！")
    else:
        name_handling(old, new)
        msg_box("重命名成功")
        clear(old, new)


# 获取文件名指定文件
def get_file(choose, out, path, arg_type, generate_type):
    if choose.get() == '' or out.get() == '':
        msg_box("输入/输出文件夹选择不允许为空！")
    elif arg_type.get() == '0':
        msg_box("类型不允许为空！")
    elif generate_type.get() == '0':
        msg_box("请选择要生成的文件类型")
    elif generate_type.get() == 'xls' or generate_type.get() == 'xlsx':
        msg_box("改版本未开发，敬请期待")
    else:
        file_name_arr = get_folder_file_name(choose, arg_type.get())
        out_file(out, file_name_arr, path, generate_type)
        msg_box("写入成功")
        clear(choose, out)
