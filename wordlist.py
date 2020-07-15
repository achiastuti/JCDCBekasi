word = "secret"

#creates an variable with an empty value
guesses = ''

#determine the number of turns
turns = 10

#check if the turns are more than zero
while turns > 0:         
    failed = 0                 
    for char in word:      
        if char in guesses:
            print (char),    
        else:
            print ("_" )
            failed += 1    
    if failed == 0:        
        print ("You won")  
        break              
    # ask the user go guess a character
    guess = input("guess a character:") 
    guesses += guess                    
    # if the guess is not found in the secret word
    if guess not in word:  
        turns -= 1        
        print ("Wrong")
    # how many turns are left
        print ("You have"), + turns, 'more guesses' 
    # if the turns are equal to zero
        if turns == 0:           
        # print "You Lose"
            print ("You Lose")



