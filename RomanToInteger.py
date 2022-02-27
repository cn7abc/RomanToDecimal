# Converting a roman numeral formatted number to base ten integer.
# Jacob Rogers
# 2-27-2022



def romanToInt(s : str) -> int:
        
    romanDict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'Z' : 0}
        
    stringLength = len(s)
#   Add a ternimating character that means zero to every string so we can always check forwards for subtraction cases, even at the end of the string.
    s = s + 'Z'
    total = 0
    i = 0
        
    while i < stringLength:
            
        if s[i] == 'I':
            if s[i+1] == 'V':
                total = total + 4
                i += 2
                continue
            elif s[i+1] == 'X':
                total = total + 9
                i += 2
                continue
            else:
                total = total + romanDict.get(s[i])
                i += 1
                
        elif s[i] == 'V':
            total = total + romanDict.get(s[i])
            i += 1
                
        elif s[i] == 'X':
            if s[i+1] == 'L':
                total = total + 40
                i += 2
                continue
            elif s[i+1] == 'C':
                total = total + 90
                i += 2
                continue
            else:
                total = total + romanDict.get(s[i])
                i += 1
                    
        elif s[i] == 'L':
            total = total + romanDict.get(s[i])
            i += 1
            
        elif s[i] == 'C':
            if s[i+1] == 'D':
                total = total + 400
                i += 2
                continue
            elif s[i+1] == 'M':
                total = total + 900
                i += 2
                continue
            else:
                total = total + romanDict.get(s[i])
                i += 1
                    
        elif s[i] == 'D':
            total = total + romanDict.get(s[i])
            i += 1
                
        elif s[i] == 'M':
            total = total + romanDict.get(s[i])
            i += 1
                
    return total

go = True

while go:
    
    print("Roman Numeral to base ten, Roma Victa.")
    s = input('Enter a Roman Numeral IN ALL CAPS to see its base ten number: ')

    print(romanToInt(s))

    i = input('press q to quit, or anykey and then enter to continue. ')
    if i == 'q':
        go = False

