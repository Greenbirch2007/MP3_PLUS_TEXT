# -*- coding: utf-8 -*-
import sys
from urllib import FancyURLopener

class MyOpener(FancyURLopener):
    def downPro(self):
        version = '''Mozilla/5.0 (X11; U; Linux i686 (x86_64); zh-CN; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2'''
        print version
        myopener=MyOpener()
        url = 'https://dl2.ankiweb.net/shared/downloadDeck2/855860209?k=Wzg1NTg2MDIwOSwgMjM3OTMsIDE1ODA1MjUxODVd.gxA3C5tqqjvBma6dxmudXOJu2padlYUFJGfaO8Yafc8'  #自己指定文件地址
        page=myopener.open(url)
        saveFile = file('save_file.dpkg','wb+')
        try:
            while True:
                arr = page.read()
                if len(arr) == 0:
                    break
                saveFile.write(arr)
                print arr
        finally:
            page.close()
            saveFile.close()


p=MyOpener()
p.downPro()
sys.exit()






竟然是zsh的问题，直接用bash就好了


wget  https://dl2.ankiweb.net/shared/downloadDeck2/855860209?k=Wzg1NTg2MDIwOSwgMjM3OTMsIDE1ODA1MjUxODVd.gxA3C5tqqjvBma6dxmudXOJu2padlYUFJGfaO8Yafc8 -O /home/greenb/d.dpkg

