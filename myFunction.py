def hello():
    print("hello Dianna")
    print("how are you ?")
hello()

def hello1(name):
    print(f"hello {name}")
    print("how are you ?")
hello1('Marc')

def command(cmd):
    import os
    os.system(cmd)
command('ls')