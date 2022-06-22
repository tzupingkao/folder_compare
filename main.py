import os
import sys
from filecmp import dircmp

# Ref: https://coderzcolumn.com/tutorials/python/filecmp-compare-files-and-directories-using-python

class Directory:

    def __init__(self, dirs):
        self.__dir_list = os.listdir(dirs)
        self.__dir_map = dict()
        self.__password = '預設密碼 0000'
        for item in self.__dir_list:
            fullpath = os.path.join(dirs, item)
            self.__dir_map[item] = fullpath
            # print(item + ", " + str(os.path.isdir(fullpath)))

    def print_var(self):
        for a in self.__dir_map:
            print(self.__dir_map[a])

    @property
    def get_dir_map(self):
        return self.__dir_map

    # ------------- test property start -------------
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @password.deleter
    def password(self):
        del self.__password
        print('del complete')
    # ------------- test property end ---------------


if __name__ == '__main__':
    old = os.path.join(os.getcwd(), "old")
    new = os.path.join(os.getcwd(), "new")

    tt_old = Directory(old)
    a_old = tt_old.get_dir_map

    tt_new = Directory(new)
    a_new = tt_new.get_dir_map

    k = {'Apple': 400, 'Joey': 600, 'Bella': 50, '2th King': 10000}
    print(k)
    k = {key: k[key] for key in sorted(k.keys())}
    print(k)


    def print_diff_files(dcmp):
        for name in dcmp.diff_files:
            print("diff_file %s found in %s and %s" % (name, dcmp.left, dcmp.right))

        for sub_dcmp in dcmp.subdirs.values():
            print_diff_files(sub_dcmp)

    dcmp = dircmp(old, new)
    print_diff_files(dcmp)

    tt_old.password = "FFT"
    print(tt_old.password)
    del tt_old.password

    tzu = 1
