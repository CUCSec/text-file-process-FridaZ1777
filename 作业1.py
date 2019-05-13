result=0
with open('C:/Users/20213/Documents/CS1.2/Python/git/text-file-process-FridaZ1777/log_files/201811113024.log',encoding='utf8') as t:
    for line in t:
        s1=line.split('：')
        s2=s1[2].split(',')
        if s2[0]=='201811113024':
            result+=1
print(result)
