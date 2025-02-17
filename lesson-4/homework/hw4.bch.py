import random
run='yes'
while run.lower() in ['yes','run','start','s','y','1','r','ok']:
    c=0
    p=0
    while p<5 and c<5:
        computer_choice=random.choice(['rock','paper','scissors'])
        player_choice=str(input('Choose one of these options! Rock, paper, or scissors? '))
        if player_choice.lower() not in ['rock','paper','scissors']:
            print('Wrong command! Enter your choice correctly!')
        else:
            if computer_choice==player_choice:
                print(f'It\'s tie!')
            elif computer_choice=='rock':
                if player_choice=='paper':
                    p+=1
                else:
                    c+=1
            elif computer_choice=='paper':
                if player_choice=='rock':
                    c+=1
                else:
                    p+=1
            else:
                if player_choice=='rock':
                    p+=1
                else:
                    c+=1
            print(f'computer {c}; you {p}')
            print(f'Computer choice was {computer_choice}')
    if c==5:
        print('The winner is computer')
    else:
        print('The winner is you')
    run=str(input('Do you want to play again? '))

        
 