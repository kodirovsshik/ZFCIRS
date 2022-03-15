from os import getcwd
from os.path import join
import glob

filepaths = (glob.glob(f'{getcwd()}\\*\\*.txt'))

zfc_path = join(getcwd(), 'ЗФЦИРС.txt')
open(zfc_path, 'w').write('')

zfc = open(zfc_path, 'a', encoding="utf8")
for filepath in filepaths:
    print(filepath[filepath.rindex('\\')+1::])
    zfc.write(open(filepath, 'r', encoding="utf8").read() + '\n\n')
