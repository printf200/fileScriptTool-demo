import os


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
def out_file(out, arr, path, arg_type):
    if path.get() == '':
        full_path = "result" + '.' + arg_type.get()  # 也可以创建一个.doc的word文档
    else:
        full_path = path.get() + '.' + arg_type.get()  # 也可以创建一个.doc的word文档
    file = open(out.get() + '/' + full_path, 'w')  # w 的含义为可进行读写
    for value in arr:
        file.write(value)

    file.close()


# 处理文件夹重命名方法
def name_handling(old, new):
    old_path = old.get()
    old_arr = old_path.split("/")
    name = old_arr[-1]
    file_type = name.split('.')
    file_path = old_path[:old_path.index(name)]
    if len(file_type) > 1:
        new_path = str(file_path + new.get() + '.' + file_type[1]).encode()
        os.rename(old_path, new_path)
    else:
        new_path = str(file_path + new.get()).encode()
        os.renames(old_path, new_path)
