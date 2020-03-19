# -*- coding: utf-8 -*-

old = open(u'Normal text',"r")
new_file = open(u'New text' , 'w')
Old = old.read()
new = Old.replace(",", ",бля,")
new_file.write(new)
new_file.close()
old.close()



print("---------------------------------------------------")
print("|                Текст редактирован                |")
print("---------------------------------------------------")
