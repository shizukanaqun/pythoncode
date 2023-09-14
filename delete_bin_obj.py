import win32con
import win32api
import os
from win32con import FILE_ATTRIBUTE_NORMAL


def finddir(file_dir):
    for dirs in os.listdir(file_dir):
        pathname = os.path.join(file_dir, dirs)
        if (os.path.isdir(pathname)):
            if ('\obj' in pathname or '\\bin' in pathname):
                del_dir(pathname)
            else:
                finddir(pathname)


def del_dir(path):
    for file in os.listdir(path):
        file_or_dir = os.path.join(path, file)
        if (os.path.isdir(file_or_dir) and not os.path.islink(file_or_dir)):
            del_dir(file_or_dir)
        else:
            try:
                os.remove(file_or_dir)
            except:
                win32api.SetFileAttributes(file_or_dir, FILE_ATTRIBUTE_NORMAL)
                os.remove(file_or_dir)
    os.rmdir(path)
    print(f'{path} 已删除')


if __name__ == "__main__":
    path = 'C:\workspace\code\XPD\Demo\hyj'
    print('操作路径：' + path)
    finddir(path)
    print('删除完毕')