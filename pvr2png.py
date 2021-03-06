# -*- coding: cp936 -*-
#!python

import os
import sys

#def GetTexturePackerPath():
    #return 'F:\CodeAndWeb\TexturePacker\bin\TexturePacker.exe'

def pvrToPng (_TPATH,_path,_OutPath):
    TPATH = _TPATH
    OutPath = _OutPath
    for(dirpath, dirnames, filenames) in os.walk(_path):
        for filename in filenames:
            if filename.endswith(SUFFIX):
                basename = os.path.basename(filename)
                newFileName = basename[0:basename.find(SUFFIX)]
                if not os.path.isabs(_OutPath):
                    OutPath = os.path.join(dirpath,_OutPath)
                # deltaPath = dirpath
                if not os.path.exists(OutPath):
                    os.makedirs(OutPath)
                outFileName = os.path.join(OutPath,newFileName + ".png")
                cmd = TPATH + " " + os.path.join(dirpath,filename) + " --data pvr2pngTmp.plist --sheet " + outFileName + " --opt RGBA8888 --allow-free-size --algorithm MaxRects --shape-padding 0 --border-padding 0 --trim --dither-fs"
                os.system(cmd)
                print "generator %s" % outFileName
    os.remove("pvr2pngTmp.plist")
    print "--------------------pvrToPng end--------------------"

# Tips: 1. Install TexturePacker Command Tools; 2. You should set TexturePacker to Pro mode;
if __name__ == '__main__':
    #currtenPath = os.getcwd()
    if len(sys.argv) < 3:
        print("usage : python pvr2png.py [suffix:pvr pvr.ccz] [source Path] [OutPath:option] [TexturePacker Path]")
    else:
        SUFFIX = sys.argv[1]
        if SUFFIX[0] != '.':
            SUFFIX = "." + SUFFIX
        OutPath = './'
        if len(sys.argv) == 3:
            OutPath = sys.argv[2]
        TPATH = "F://CodeAndWeb//TexturePacker//bin//TexturePacker.exe"
        if len(sys.argv) == 5:
            TPATH = sys.argv[4]
        pvrToPng(TPATH,sys.argv[2],OutPath)

#
