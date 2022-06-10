import os
import sys

old = "C:\\Users\\tzuping.kao\\Desktop\\folder_compare\\old"
new = "C:\\Users\\tzuping.kao\\Desktop\\folder_compare\\new"


class Directory:

    __dir_obj = dict()

    def __init__(self, dirs):
        dir_list = os.listdir(dirs)
        self.__a = dict()
        for item in dir_list:
            fullpath = os.path.join(dirs, item)
            self.__a[item] = fullpath
            # print(item + ", " + str(os.path.isdir(fullpath)))

    def print_var(self):
        for a in self.__a:
            print(self.__a[a])

    @property
    def get(self):
        return self.__a


# a = dirs = os.listdir(old)
# for item in a:
#     fullpath = os.path.join(old, item)
#     print(item + ", " + str(os.path.isdir(fullpath)))

tt = Directory(old)
tt.print_var()
tg = tt.get()
tzu = 1
