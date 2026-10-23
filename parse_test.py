def parse_expression(text, pattern):
    val = False
    for i,word in enumerate(pattern):
        if word == text[i]:
            val = True 
        else:
            return False
    return val

if __name__ == "__main__":
    t1 = input().split(' ')
    t2 = input().split(' ')

    print(parse_expression(t1, t2))
    print(t2, t1)