

def toBINARY(interger):
    bIN = "0000000000000000"
    bIN_len = len(bIN)

    if(interger < 0):
        bIN = "1" + bIN[1:bIN_len+1]

    interger = abs(interger)

    print(len(bIN))
    for i in range(bIN_len-1):
        power = 2**((bIN_len-2)-i)
        mods = interger//power    
        if(mods == 1):
            if(power%interger != 0):
                interger = interger - power%interger
            else:
                interger = 0

        bIN = bIN[0:i+1] + str(mods) + bIN[i+2:bIN_len+1] 
        
    return bIN




print(toBINARY(-600))