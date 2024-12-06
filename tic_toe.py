import random
import time
l=['head','tail']
while True:
    call=input('playerA head or tail?? ')
    call=call.lower()
    if call=='head' or call=='tail':
        break
    else:
        print('entered wrong input....')
print('the coin is in the air..........and ')
time.sleep(2)
dict1={'playerA':'','playerB':''}
rand_val=random.choice(l)
if call.lower()==rand_val:
    won='playerA'
    print(f'congrats playerA you got {rand_val}...so what you want to select ??? x or 0')
    while True:
        player_inp=input('->')
        player_inp=player_inp.lower()
        if player_inp=='x' or player_inp=='0':
            break
        else:
            print('please enter correct choice')
    dict1['playerA']=player_inp
    if player_inp=='x':
        dict1['playerB']='0'
    else:
        dict1['playerB'] = 'x'
elif call.lower()!=rand_val:
    won='playerB'
    print(f'congrats playerB you got {rand_val}...so what you want to select ??? x or 0')
    while True:
        player_inp=input('->')
        player_inp=player_inp.lower()
        if player_inp=='x' or player_inp=='0':
            break
        else:
            print('please enter correct choice')
    dict1['playerB'] = player_inp
    if player_inp == 'x':
        dict1['playerA'] = '0'
    else:
        dict1['playerA'] = 'x'
mat=[[None,None,None],[None,None,None],[None,None,None]]
def play(toss_won):
    if toss_won=='playerA':
        var='playerA'
    else:
        var='playerB'
    while (None in mat[0]) or (None in mat[1]) or (None in mat[2]):
        while True:
            temp_str = input(f"it's {var}'s turn->").strip()
            temp_str1 = ''
            for temp in temp_str:
                if temp != ' ':
                    temp_str1 += temp
            var_inp = temp_str1
            if not var_inp.isdigit() or len(var_inp) != 2 or int(var_inp[0]) > 2 or int(var_inp[1]) > 2:
                print('you have entered wrong input...')
                continue
            else:
                if var == 'playerA':
                    if mat[int(var_inp[0])][int(var_inp[1])] is not None:
                        print(f'this box is already occupied....try again {var}')
                        continue
                    else:
                        mat[int(var_inp[0])][int(var_inp[1])] = dict1['playerA']
                        break
                else:
                    if mat[int(var_inp[0])][int(var_inp[1])] is not None:
                        print(f'this box is already occupied....try again {var}')
                        continue
                    else:
                        mat[int(var_inp[0])][int(var_inp[1])] = dict1['playerB']
                        break
        print('     |     |  ')
        for x in range(3):
            print(' ', end='')
            for u, y in enumerate(mat[x]):
                if u != 2:
                    if y==None:
                        print(x,u, end=' | ')
                    else:
                        print('',y,'',end=' | ')
                else:
                    if y==None:
                        print(x,u)
                    else:
                        print('',y,'')
            if x != 2:
                print('------------------')
        print('     |     |  ')
        if mat[0][0] == mat[1][0] == mat[2][0]!=None: #top left to bottom left
            if mat[0][0]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[0][0]==mat[1][1]==mat[2][2]!=None: #top left to bottom corner
            if mat[0][0]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[0][0] == mat[0][1] == mat[0][2]!=None: # top left to top right
            if mat[0][0]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[0][1]==mat[1][1]==mat[2][1]!=None: # top middle to bottom middle
            if mat[0][1]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[0][2] == mat[1][1] == mat[2][0]!=None: # top right to bottom left
            if mat[0][2]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[0][2] == mat[1][2] == mat[2][2]!=None: # top right to bottom right
            if mat[0][2]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[1][0] == mat[1][1] == mat[1][2]!=None: # middle left to middle right
            if mat[1][0]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        elif mat[2][0] == mat[2][1] == mat[2][2]!=None: # bottom left to bottom right
            if mat[2][0]=='x':
                for u in dict1.items():
                    if u[1]=='x':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            else:
                for u in dict1.items():
                    if u[1]=='0':
                        print(f"{u[0]} has won the game with symbol {u[1]}")
            return
        else:
            if var=='playerA':
                var='playerB'
            else:
                var='playerA'
    print('its a draw')
    return
play(won)