#coding=utf-8                    #设置编码格式以支持中文注释


char_ = {
'H':('1       1',
     '1       1',
     '1-------1',
     '1       1',
     '1       1'),
'Y':(' \     / ',
     '  \   /  ',
     '   \ /   ',
     '    1    ',
     '    1    '),}
input_word = raw_input("please input any amount and array of \"H\" and \"Y\":")             #可以是Hy的任意组合 
import re
reg1=re.compile("(?=H)")
reg2=re.compile("(?=Y)")
length1=len(reg1.findall(input_word ))
length2=len(reg2.findall(input_word ))


for i in range(5):              #逐行扫描，共五行  
    for z in range(int(length1)+int(length2)):    #逐个字母扫描 
        for j in input_word[z]:   
            print char_ [j][i], #加逗号表示不换行，同行显示每个字母的同一行	
    print ""  			#通过在行末打印空白字符实现换行 