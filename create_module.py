#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os   #Python的标准库中的os模块包含普遍的操作系统功能
import sys

name = sys.argv[1]

def creatFiles():
    if len(name) <=0 :
        return
    os.system("mkdir %s" % name)
    os.chdir('./%s' % name)
    os.system("pod spec create %s" % name)
    os.system("mkdir Sources")
    os.system("mkdir ./Sources/View")
    os.system("mkdir ./Sources/ViewModel")
    os.system("mkdir ./Sources/ViewController")
    os.system("mkdir ./Sources/Model")

    os.system("touch ./Sources/Export.swift")
    os.system("touch ./Sources/View/View.swift")
    os.system("touch ./Sources/ViewModel/ViewModel.swift")
    os.system("touch ./Sources/ViewController/ViewController.swift")
    os.system("touch ./Sources/Model/Model.swift")

print(name)
creatFiles()

