# try:
#     print(0/0)
# except Exception as e:
#     print(e)
# finally:
#     print("done")
def add(a,b):
    if b==0:
        raise Exception(" B is zero")
    return a+b
try:
    print(add(1,0))
except Exception as e:
    print(e)
finally:
    print("Done")