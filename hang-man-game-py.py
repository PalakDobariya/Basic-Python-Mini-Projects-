# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random
from collections import Counter

someWords='''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon'''

someWords= someWords.split(' ')

#randomly choose a secret word from our " someWords" LIST
word=random.choice(someWords)

if __name__=='__main__':
    print('Guess the word ! hint:word is a name of a fruit')
    
    for i in word:
        #for printing the empty spaces for letters of the word
        print('_',end=' ')
    print()
    
    playing=True
    #list for storing the letters gussed by the player
    letterGuessed = ''
    chances=len(word)+2
    correct=0
    flag=0
    try:
        while(chances!=0)and flag==0:
            #flag is updated when the word is correctly gussed
            print()
            chances -=1
            
            try:
                guess=str(input("enter a letter to guess:"))
            except:
                print("enter only a letter!")
                continue
            #Validation of the guess
            if not guess.isalpha():
                print("enter only a letter")
                continue
            elif len(guess)>1:
                print("enter only a single letter")
                continue
            elif guess in letterGuessed:
                print("you have already guessed that letter")
                continue
            
            #if letter is guessed correctly
            if guess in word:
                k=word.count(guess)# k stores the number of times
                for _ in range(k):
                    letterGuessed +=guess# the guess letter is added as many times as it occurs
                    
            #print the word
            for char in word:
                if char in letterGuessed and(Counter(letterGuessed)!=Counter(word)):
                    print(char, end=' ')
                    correct +=1
                #if user has guessed all the letter
                elif (Counter(letterGuessed)==Counter(word)):
                #Once the correct word is gussed fully.
                #the game ends, even if chances remain
                    print ("the word is :",end=' ')
                    print(word)
                    flag=1
                    print('Congratulations, you won!')
                    break# to break out of the for loop
                    break# to break out of the while loop
                else:
                    print('_',end=' ')
                    
        #if user has used allof his chances
        if chances <=0 and (Counter(letterGuessed)!=Counter(word)):
            print()
            print('you lost! try again..')
            print('the word was {}'.format(word))
    except KeyboardInterrupt:
        print()
        print('Bye! try again')
        exit()
          