from os import getcwd
from os.path import join
import glob

filepaths = (glob.glob(f'{getcwd()}\\*\\*.txt'))

zfc_path = join(getcwd(), 'ЗФЦИРС.txt')
open(zfc_path, 'w').write('')

zfc = open(zfc_path, 'a', encoding="utf8")
for filepath in filepaths:
    print(filepath[filepath.rindex('\\')+1::])
<<<<<<< HEAD
    zfc.write(open(filepath, 'r', encoding="utf8").read() + '\n\n')
=======
    zfc.write(open(filepath, 'r', encoding="utf8").read() + '\n\n')
>>>>>>> 29ccdede57383eddf2af130b5f5cde12d3068444
