import os

#print(os.environ)

s = str(os.environ['c_line1']) + "\n" + str(os.environ['c_line2']) + "\n\t" + str(os.environ['c_line3'])

f = open("config.py", "w")
f.write(s)
