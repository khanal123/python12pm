from os.path import dirname,basename,join,isfile
import glob
allFiles=glob.glob(join(dirname(__file__),'*.py'))
# for file in allFiles:
#     print(basename(file))
# names='sophia'
# print(names[:-2])
__all__=[basename(file)[:-3] for file in allFiles if isfile(file) and not file.endswith('__init__.py')]
# print("Hello lib")
# __all__=['database','users']