# Hangman

Hangman is a Python terminal game, wich runs in the Code Institute mock terminal on Heroku.

Users can try to defeat the computer by identifying all of the letters in a word or predicting the word that the computer chooses at random.
Users have just six attempts before getting "hanged" and losing all of their progress.

[Please find attached here the live version of my project.] (https://level-game.herokuapp.com/)

# How to play
Users can try to defeat the computer by identifying all of the letters in a word or predicting the word that the computer chooses at random.
Users have six attempts before getting "hanged" and losing all of their progress.
If the user correctly guesses a letter in the word, it  will be displayed on the terminal on the line in the right word position.
In case the user loses and he cannot guess the word before finishing the six rounds a game over message will appear. 


# Features

* After user input his name, he will be presented to the rules. 
* Random secret words will be masked by the signal "_". 
* The player can only guess 1 letter at the time.

   ![ScreenShot](/assets/images/game01.png)

* Plays against the computer
* User will notificed when he got a right or wrong answer guess.
* Accept user input

    ![ScreenShot](/assets/images/game02.png)



   ![ScreenShot](/assets/images/game03.png)

* The secret word will only be revealed at the end of the game.

## Future features
  * Different levels.
  * Option to add multiplayers.


# Testing

* I manually evaluated this project by: * Running the code through a PEP8 linter and verifying there were no     errors.

* Given Invalid inputs including strings where numbers are allowed, out of bounds inputs, and the same input again.

* Tested on my own terminal as well as the Heroku terminal at the Code Institute.

# Bugs

* At first I added the list of words in the run.py but to make the code more organised I created newords.txt file. 

*  The game was only with one end-game message with no secret word revealed. I have added the option for the user see what is the secret word and also added one more funtion for game over message in order to be more clear about the result.

* I also had some Misuse Expressions issues. which causes errors and did not allow it to execute the code correctly.


## No bugs remaining.

# Validator testing
  * PEP8 
    * No errors were returned from [PEP8online](http://pep8online.com/)


# Deployment
  * Steps for deployment
    * Fork or clone this repository
    * Create a new Heroku app
    * Set the buildbacks to Python and NodeJS in that order
    * Link the Heroku app to repository
    * Click on Deploy

# Credits
  * Code Institute for the deployment terminal
  * [ Youtube ] Creating A Simple Hangman Game in Python (https://www.youtube.com/watch?v=5x6iAKdJB6U).

  ## Acknowledgements
I would like to thank **Slack Community** for their assistance with minor coding issues and **Beatriz Amorim** who tested my game and gave me excellent feedback based on her milestone submission.

  

