def word_count(txt):
    num = len(txt.split())
    return num

def char_count(txt):
    letters = txt.lower()
    counted ={}
    for letter in letters:
        if letter in counted:
            counted[letter] +=1
        else:
            counted[letter] =1 
    return counted
def sort_count(dick):
    def sort_on(items):
        return items["num"]

    templist =[]
    tmp2=[]
    for dic in dick:
        if dic.isalpha():
            templist.append({"char" : dic,"num":dick[dic]})
    templist.sort(reverse=True,key=sort_on)

   
    return templist