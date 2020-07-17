#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

from PIL import Image
import os

def combine2Pdf( folderPath, pdfFilePath ):
    files = os.listdir( folderPath )
    pngFiles = []
    sources = []
    # if 和 elif 是一个阵营的else则是完全对立面，所以这里要用if和elif的组合
    for file in files:
        if 'jpg' in file:
            pngFiles.append( folderPath + file )

        elif 'png' in file:
            pngFiles.append( folderPath + file )
    pngFiles.sort()
    output = Image.open( pngFiles[0] )
    pngFiles.pop( 0 )
    for file in pngFiles:
        pngFile = Image.open( file )
        if pngFile.mode == "RGB":
            pngFile = pngFile.convert( "RGB" )
        sources.append( pngFile )
    output.save( pdfFilePath, "pdf", save_all=True, append_images=sources )

if __name__ == "__main__":
    l_path = os.getcwd()
    folder = "{0}/pngFiles/".format(l_path)
    pdfFile = "{0}/contract.pdf".format(l_path)
    combine2Pdf( folder, pdfFile )