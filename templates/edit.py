'''
import shutil
import os
os.remove("../static/css")
os.remove("../static/js")
os.remove("../static/fonts")
os.remove("../static/favicon.ico")

shutil.move("D:\\Cryptonomy\\vue\\dist\\js", "D:\\Cryptonomy\\static\\js")
shutil.move("../vue/dist/css", "../static/css")
shutil.move("../vue/dist/fonts", "../static/fonts")
shutil.move("../vue/dist/favicon.ico", "../static/favicon.ico")
shutil.move("../vue/dist/index.html", "/")

'''
# Open a file: file
file = open('index.html',mode='r')

# read all lines at once
all_of_it = file.read()

# close the file
file.close()

all_of_it = all_of_it.replace('/js','static/js')
all_of_it = all_of_it.replace('/css','static/css')
all_of_it = all_of_it.replace('/fonts','static/js')
all_of_it = all_of_it.replace('/favicon.ico','static/favicon.ico')

f = open("index.html", "w")
f.write(all_of_it)
f.close()
