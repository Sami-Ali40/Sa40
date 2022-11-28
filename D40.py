         os.system('rm -rf Sami.so Sami32.so')
 except:
     pass
 os.system('rm -rf Sami_64.so Sami32.so')
 os.system('rm -rf Sami.so Sami32.so')
 os.system('git pull')

 bit = platform.architecture()[0]
