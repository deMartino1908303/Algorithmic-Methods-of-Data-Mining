def minion_game(st):
    # your code goes here
    st_ln=len(st)
    kv_scr=0
    st_scr=0
    
    for val in range(st_ln):
        
        if str(st[val]) == 'A':
            kv_scr += st_ln - val
        elif str(st[val]) == 'E':
            kv_scr += st_ln - val
        elif str(st[val]) == 'I':
            kv_scr += st_ln - val
        elif str(st[val]) == 'O':
            kv_scr += st_ln - val
        elif str(st[val]) == 'U':
            kv_scr += st_ln - val
        else:
            st_scr += st_ln -val
            
    if kv_scr > st_scr :
        print ("Kevin", kv_scr)
    elif kv_scr < st_scr:
        print ("Stuart", st_scr)
    else:
        print ("Draw")
