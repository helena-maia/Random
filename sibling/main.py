#python 3.6.8
#main that imports package that imports package
#func.py and subpackage are sibling modules from package

import package as pkg

if __name__ == '__main__':
    pkg.func.function(2)
