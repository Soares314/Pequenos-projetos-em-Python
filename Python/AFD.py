def delta(state, algarism, i):
    if i == len(algarism):
        return state

    if state == 0:
        if algarism[i] == "a":
            state = 1
        elif algarism[i] == "b":
            state = 5
        i = i + 1
        return delta(state, algarism, i)
    
    if state == 1:
        if algarism[i] == "a":
            state = 5
        elif algarism[i] == "b":
            state = 2
        i = i + 1
        return delta(state, algarism, i)
    
    if state == 2:
        if algarism[i] == "a":
            state = 3
        elif algarism[i] == "b":
            state = 4
        i = i + 1
        return delta(state, algarism, i)
    
    if state == 3:
        if algarism[i] == "a":
            state = 6
        elif algarism[i] == "b":
            state = 4
        i = i + 1
        return delta(state, algarism, i)

    if state == 4:
        if algarism[i] == "a":
            state = 3
        elif algarism[i] == "b":
            state = 4
        i = i + 1
        return delta(state, algarism, i)
    
    if state == 5:
        if algarism[i] == "a":
            state = 5
        elif algarism[i] == "b":
            state = 5
        i = i + 1
        return delta(state, algarism, i)
    
    if state == 6:
        if algarism[i] == "a":
            state = 6
        elif algarism[i] == "b":
            state = 4
        i = i + 1
        return delta(state, algarism, i)

def IsFromLanguage(*algarism):
    for x in algarism:
        i = 0
        state = 0 
        if delta(state, x, i) == 3:
            print(f"{x} is from this language\n")
        else:
            print(f"{x} isn't from this language\n")

IsFromLanguage("", "a", "ab", "aba", "baba", "abba", "baab", "abab", "abaaba", "abaababbaba")

