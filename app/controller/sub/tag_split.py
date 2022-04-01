def tag_split(text):
    index=-1
    text_temp=text
    tag=[]

    while True:
        index=text_temp.find('##')
        text_temp=text_temp.replace('##','#')
        if(index==-1):
            break
    
    while True:
        index=text_temp.find('#',index+2)
        text_temp = text_temp[:index]+' '+text_temp[index:]
        if(index==-1):
            break

    text_temp=text_temp.replace('  ',' ').split(' ')

    for i in text_temp:
        if(i.find('#')!=-1):
            if(len(i)!=1):
                tag.append(i)
                
    return tag
