#set my global variables to use throughout the program
rules_dict = {
    #Rock beats Scissors, Lizard
    "Rock": ("Scissors", "Lizard"), 
    #Paper beats Spock, Rock
    "Paper": ("Spock", "Rock"), 
    #Scissors beats Paper, Lizard
    "Scissors": ("Paper", "Lizard"), 
    #Lizard beats Spock, Paper
    "Lizard": ("Spock", "Paper"), 
    #Spock beats Scissors, Rock
    "Spock": ("Scissors", "Rock")
}


#make the function to get what each player's choice defeats
def defeats(your_choice):
    #get the tuple for the winning options given user input
    your_choice_defeats = rules_dict.get(your_choice)
    return your_choice_defeats

#make the function to determine the outcome of the battle
def battle(player_choices):
    #cycle thru getting each player's choice

    #get the items that the player's choice defeats

    #check the tuple against the remaining player's choices

    #remember which players were defeated!

    return 'This function is still a work in progress'

#create a main function to run and test at the command line
def main():
    #make the game flexible for multiple players
    players_int = int(input('How many players are in the game? '))

    #get each players choice, so long as it is a valid choice
    player_choices = []
    x = 1
    #loop thru the total number of players to get their choices
    while x <= players_int:
        your_choice = ''
        #hold the input if the user input doesn't match the dictionary keys
        while not your_choice in rules_dict:
            your_choice = input('Player ' + str(x) + ' what do you throw? Rock, Paper, Scissors, Lizard, Spock? ')
            player_choices.append(your_choice)
        
        #print the options that the user's choice defeats
        for items in defeats(your_choice):
            print('Player ' + str(x) + ' your choice defeats: ' + items)
        
        #iterate to the next player
        x += 1
        
    #print the list of all the user choices
    print(player_choices)


#shield for running at the terminal with command-line input
if __name__ == "__main__":
    main()