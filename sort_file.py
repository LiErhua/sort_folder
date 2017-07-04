import os
import shutil
import re

path = '/Volumes/大白菜/影视材料/4K.Ultra.HD.Wallpapers/6/new'

#新建文件夹
sort_folder_number = [x for x in range(0,8)]
for number in sort_folder_number:
    new_folder_path = os.path.join(path,'%s'%number)
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)

#列出文档
file_list = os.listdir(path)
#提取出文档名称内的数字，并根据数字决定将问价发往那个文件夹
for i in range(len(file_list)):
    old_file_path = os.path.join(path,file_list[i])
    if os.path.isdir(old_file_path):
        pass
    elif not os.path.exists(old_file_path):
        pass
    else:
        file_name_number = re.findall(r'\d+',file_list[i])[0]
        file_name_number = int(file_name_number)
        new_file_path = os.path.join(path,'%s'%(file_name_number%8))
        shutil.move(old_file_path,new_file_path)
