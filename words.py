from utils import element_wait,word_wait,char_wait
from utils import dot,tire

# 0 is dot
# 1 is tire

chars_characheristics={
    "A":(0,1),
    "B":(1,0,0,0),
    "C":(1,0,1,0),
    "D":(1,0,0),
    "E":(0,),
    "F":(0,0,1,0),
    "G":(1,1,0),
    "H":(0,0,0,0),
    "I":(0,0),
    "J":(0,1,1,1),
    "K":(1,0,1),
    "L":(0,1,0,0),
    "M":(1,1),
    "N":(1,0),
    "O":(1,1,1),
    "P":(0,1,1,0),
    "Q":(1,1,0,1),
    "R":(0,1,0),
    "S":(0,0,0),
    "T":(1),
    "U":(0,0,1),
    "V":(0,0,0,1),
    "W":(0,1,1),
    "X":(1,0,0,1),
    "Y":(1,0,1,1),
    "Z":(1,1,0,0),
    "0":(1,1,1,1,1),
    "1":(0,1,1,1,1),
    "2":(0,0,1,1,1),
    "3":(0,0,0,1,1),
    "4":(0,0,0,0,1),
    "5":(0,0,0,0,0),
    "6":(1,0,0,0,0),
    "7":(1,1,0,0,0),
    "8":(1,1,1,0,0),
    "9":(1,1,1,1,0)
}




def build_char(char):

    char=chars_characheristics.get(char,None)

    if char:
        func_sequence=[]

        for index,code in enumerate(char):
            if code==1:
                func_sequence.append(tire)
            if code==0:
                func_sequence.append(dot)

            if index+1<len(char):
                func_sequence.append(element_wait)

        return func_sequence

def build_word(word):

    chars=[]

    chars.append(char_wait)

    for char in word:
        if char in ("_"," "):
            chars.append(word_wait)
            continue
        char_factory_result=build_char(char)
        chars.extend(char_factory_result)
        chars.append(char_wait)
    chars.append(word_wait)

    return chars