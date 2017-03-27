#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

def transName(fileName):
    foreName = fileName.split(".")[0]
    #print "R.drawable." + foreName
    return "R.drawable." + foreName

def ListFilesToTxt(dir,file,wildcard,recursion):
    exts = wildcard.split(" ")
    files = os.listdir(dir)
    for name in files:
        fullname=os.path.join(dir,name)
        if(os.path.isdir(fullname) & recursion):
            ListFilesToTxt(fullname,file,wildcard,recursion)
        else:
            for ext in exts:
                if(name.endswith(ext)):
                    file.write(transName(name) + "\n")
                    break
def Test():
    dir="/home/xiaocaolsy/workspaceApp/xiaocao/xiaocao_new/newC0926/app/src/main/res/drawable-ldpi"
    outfile="binaries.txt"
    wildcard = ".jpg"
  
    file = open(outfile,"w")
    if not file:
        print ("cannot open the file %s for writing" % outfile)
    ListFilesToTxt(dir,file,wildcard, 1)
  
    file.close()

Test()
