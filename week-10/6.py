import os
fnameAry = []
folderName = "/root/University/OOP2_Study/week-10"
for dirName, subDirList, fnames in os.walk(folderName):
    for fname in fnames:
        fnameAry.append(fname)
print(fnameAry)