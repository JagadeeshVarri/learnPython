# When character are consecutive in a string , it is possible to shorten the character string by replacing the character with a certain rule. For example, in the case of the character string YYYYY, if it is expressed as # 5 Y, it is compressed by one character.

def restore_original_str(a1):
    result = ""
    ind = 0
    end = len(a1)
    while ind < end:
        if a1[ind] == "#":
            result += a1[ind + 2] * int(a1[ind + 1])
            ind += 3
        else:
            result += a1[ind]
            ind += 1
    return result
print("Original text:","XY#6Z1#4023")
print(restore_original_str("XY#6Z1#4023"))
print("Original text:","#39+1=1#30")
print(restore_original_str("#39+1=1#30"))
