import myFunction
myFunction.command('ls')


import myFunction as m
m.command('pwd')


from myFunction import command,hello
command('ls')
hello()

from os import system,mkdir
system('clear')