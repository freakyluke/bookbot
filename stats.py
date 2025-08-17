def word_count(txt):
    num = len(txt.split())
    return num

def char_count(txt):
    letters = txt.lower()
    counted ={}
    num=0
    for letter in letters:
        if letter in counted:
            counted[letter] +=1
        else:
            counted[letter] =1 
    return counted
def sort_count(dick):
    def sort_on(items):
        return items["num"]

    temp =[]
    tmp2=[]
    for dic in dick:
        if dic.isalpha():
            temp.append({"char" : dic,"num":dick[dic]})
    temp.sort(reverse=True,key=sort_on)

   
    return temp