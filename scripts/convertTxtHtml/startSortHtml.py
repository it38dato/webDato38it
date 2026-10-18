#tag - теги html
#file - переменная файла
#fileread - считывание файла
#replacetags - замена тегов
#addtags - добавление тега p в файле
#tags=["<p>","</p>","<br>","&nbsp;&nbsp;&nbsp;"]
tags=["&lt;", "&gt;", "<br>", "&nbsp;&nbsp;", "<strong>Task:</strong>", "<strong>Decision:</strong>", "<strong>Source:</strong>"]
#print(tags[2])
with open("input.txt", encoding="utf8") as file:
    fileread = file.read()
    #print(fileread)
replacetags=fileread.replace("<", tags[0]).replace(">",tags[1]).replace("\n", tags[2]).replace("    ", tags[3]).replace("Task:", tags[4]).replace("Decision:", tags[5]).replace("Source:", tags[6])
#print(replacetags)
addtags = "<p>"+replacetags+"</p>"
with open("output.txt", "w", encoding="utf8") as file:
    file.write(addtags+"\n")
