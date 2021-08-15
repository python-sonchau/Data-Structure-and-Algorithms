def is_unique(input_str):
    d = dict()
    input = ''.join(input_str.lower())
    
    for i in input:
        if i not in d:
            d[i] = 1
        else:
            return False
    
    return True

def is_unique_2(input_str):
    return len(set(input_str)) == len(input_str)

print(is_unique('abCDefGh'))
print(is_unique('nonunique'))