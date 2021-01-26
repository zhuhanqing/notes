# -*- coding: utf-8 -*-
# @Author: zhuhanqing
# @Date:   2021-01-26 22:01:47
# @Last Modified by:   zhuhanqing
# @Last Modified time: 2021-01-26 22:52:40
# coding:utf-8
import os
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", help="the path of your md file")


if __name__ == '__main__':
    args = ap.parse_args()
    path_md = args.path

    folder, name = os.path.split(path_md)

    dirname = os.path.basename(folder)
    # picture paths
    path_offline = "assets/"
    path_online = "https://github.com/zhuhanqing/notes/raw/main/"+ dirname +"/assets/"# online: github + father path + assets
    
    path_out = os.path.join(folder, "change/") # father path + backup
    if not os.path.exists(path_out):
    	os.mkdir(path_out)
    
    path_out_md = path_out + name

    print("Output files to", path_out_md)

    with open(path_md, 'r', encoding='utf-8') as f: # 需要手动指定解码的格式
        lines = f.readlines()

    out = [l.replace(path_offline, path_online) for l in lines]

    with open(path_out_md, 'w', encoding='utf-8') as f:
        f.writelines(out)