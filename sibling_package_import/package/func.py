import importlib

#import subpackage
if __package__ is None: #func.py called as main
    import subpackage as sub_pkg 
else: #func.py called from import
    sub_pkg =  importlib.import_module(__package__+".subpackage") #__package__ contains the parent package

def function(a):
    sub_pkg.subfunction(a)

if __name__ == "__main__":
    function(10)
