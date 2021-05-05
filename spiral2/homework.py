def spiralize(number,start=7):
    number*=number
    inc=2
    return_value=7
    while start<number:
        for i in range(4):
            start+=inc
            return_value+=start
        inc+=2
    return return_value
print ( spiralize(804))
