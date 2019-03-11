from random import choice
ud = {'1':'Rock','2':'Paper','3':'Scissor'}

def RPS():
    print ("""Select ur choice:
(1) for Rock
(2) for Paper
(3) for Scissor
(.) to Quit\n""")
    pr = 'Enter Choice: ' 
    while True:
        userip = input(pr)
        if userip == '.':
            break
        x = ud[userip]
        y = choice(['Rock','Paper','Scissor'])
        print ('Your Choice is:',x)
        print ('Computer has chosen:',y)
        if x == y:
            print ('Game is DRAW',end='\n\n')
        elif (x == 'Rock' and y == 'Scissor')\
             or (x == 'Scissor' and y == 'Paper')\
             or (x == 'Paper' and y == 'Rock'):
            print ('Congratulations!, You Win!!',end='\n\n')
        else:
            print ('OOPs!, You Lose!!',end='\n\n')
            
    print ('Bye Bye')

if __name__ == '__main__':
    RPS()
  