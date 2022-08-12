import inspect
import os

a = inspect.getfile(inspect.currentframe())

if os.path.isdir(a):
    print("asdasd")
elif os.path.isfile(a):
    print("qwe")

print (a)