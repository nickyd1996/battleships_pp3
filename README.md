# Hangman

Hangman is a classic and popular online word guessing game that can be enjoyed by players of all ages. The game begins with the user having the option to read the rules or create a username and select a difficulty level, ranging from easy to hard.

Once the game has started, the user is prompted to guess a letter, and if they are correct, a message will indicate the correct letter placement, and the gallows and previously guessed letters will be displayed. However, if the user guesses incorrectly, they will receive an incorrect message and the gallows will be updated with a penalty, moving them one step closer to losing the game.

Overall, Hangman is a fun and challenging game that requires both guessing skills and vocabulary knowledge, making it a great way to test your abilities and have fun at the same time.

![Home Screen](/readme_images/home_screen.PNG)

[View Hangman live project here](https://hangmans-noose.herokuapp.com/)
- - -

## Table of Contents
### [How to play](#how-to-play-1)
### [Logic Flowchart](#logic-flowchart-1)
### [User Experience (UX)](#user-experience-ux-1)
* [User Stories](#user-stories)
### [Features](#features-1)
* [Existing Features](#existing-features)
### [Features Left to Implement](#features-left-to-implement-1)
### [Design](#design-1)
### [Technologies Used](#technologies-used-1)
### [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used-1)
### [Testing](#testing-1)
### [Manual Testing](#manual-testing-1)
### [Input validation testing](#input-validation-testing-1)
### [Fixed Bugs](#fixed-bugs-1)
### [Deployment](#deployment-1)
* [Deployment to Heroku](#deployment-to-heroku)
* [Forking the GitHub Repository](#forking-the-github-repository)
* [Local Clone](#local-clone)
### [Credits](#credits-1)
* [Code](#code)
* [Content](#content)
### [Acknowledgements](#acknowledgements-1)
---

## How to Play

In this implementation of Hangman, you will play against the computer. 
You will be prompted to choose a difficulty level (easy, medium, or hard), and the computer will randomly select a word from a list of words corresponding to that level. 
You will then have to guess the letters in the chosen word before the hangman is complete.

## Logic flowchart

![Flowchart](/readme_images/hangman_flowchart.PNG)

## User Experience (UX)

Hangman is a classic word guessing game that provides a simple yet entertaining user experience. The user is presented with a blank series of dashes that represent the letters of a mystery word. They have to guess the letters in the word, one at a time. With each correct guess, the letter is revealed in the corresponding position(s). However, with each incorrect guess, a part of a hangman's body is drawn. The user can guess until they either correctly guess the entire word or the hangman is fully drawn, resulting in a loss. The game is easy to learn and provides a good balance of challenge and reward. It is also a great way to improve vocabulary and spelling skills while having fun.

### User Stories

* First-time visitor goals
    * Understand how the game works. Clear instructions and what the objective of the game is.
    * Play the game. Once the user understands the game, they will likely want to play it.
    * Enjoy the experience. The hangman game should be engaging and fun for the user.

* Returning visitor goals
    * Continue playing. The returning visitor may have enjoyed playing the game and wants to play again.
    * Share with friends. Inviting friends to give the game a try.
    * Exploring new features, if there is any.

* Frequent user goals
    * Improving their speed and accuracy in guessing words.
    * Increasing the difficulty level of the game to challenge themselves.
    * Sharing the game with others or inviting friends to play.
    * Exploring new features, if there is any.

---

## Features

* Word selection. The game randomly selects a word from one of the three available predefined lists of words.
* Difficulty settings. The game offers three difficulty settings, easy, medium and hard.
* Visual interface. Appealing interface that is easy to navigate and understand.
* Letter input. User can input their guess letter by letter to guess the hidden word.
* Incorrect guess tracking. Visually drawing a part of the hangman figure.
* Win or loss detection. Detect when the player has either successfully guessed the entire word or made too many incorrect guesses and lost the game.
* Play again at the end of the game.

### Existing Features

* Intro screen
    * Displays logo and a welcome message.

![Intro Screen](/readme_images/intro.PNG)

* Rules
    * User can choose to display rules or skip them using "y" or "n".

![Rules](/readme_images/rules.PNG)

* Enter a username

![Username](/readme_images/username.PNG)

* Introduction message and difficulty setting

![Difficulty Setting](/readme_images/difficulty_setting.PNG)

* Promp user to make a guess

![Guess a letter](/readme_images/guess_a_letter.PNG)

* Correct Guess
    * If letter is guessed, "Correct" message displays green.

![Correct guess](/readme_images/correct_guess.PNG)

* Incorrect Guess
    * If letter is not guessed, "Incorrect" message displays red.

![Incorrect guess](/readme_images/incorrect_guess.PNG)

* User guesses the word correctly
    * Message that confirms hangman is beaten.

![Won game](/readme_images/win.PNG)

* User is out of guesses
    * Message that confirms a lost game.

![Lose](/readme_images/lose.PNG)

* Play again

![Play again](/readme_images/play_again.PNG)

## Features Left to Implement

* Additional words might be available.
* Different word topics
* Scoring system
* Two player option

---

## Design

* Colors
    * dark-orange
    * orange-red
    * red
    * green

* Flowchart
    * [Draw.io](http://draw.io/)

---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Codeanywhere](https://app.codeanywhere.com/)
    * To write the code.
* [Git](https://git-scm.com/)
    * for version control.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku](https://www.heroku.com/)
    * To deploy the project.
* [CI Python Linter](https://pep8ci.herokuapp.com/)
    * Check code for any issues.

## Testing 

CI Python Linter was used to test run.py, colors.py and hangman_art_words.py

<details>
<summary> run.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/run_linter_check.PNG)
</details>

<details>
<summary> colors.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/colors_linter_check.PNG)
</details>

<details>
<summary> hangman_art_words.py CI Python Linter check
</summary>

![run.py linter check](/readme_images/hangman_art_words_linter_check.PNG)
</details>

## Manual Testing

The game was manually tested extensively using codeanywhere terminal, and once the website was deployed on Heroku it was manually tested again, during the creation of the code to the end. Testing of rules display, input validation,  correct and incorrect answers and finally win or lose display and play again feature.



| Feature | Expected Result | Steps Taken | Actual Result |
| ------- | -------------- | ----------- | ------------- |
| Intro Screen   | To display welcome message | None | As Expected |
| Display Rules | To display rules  | Input "1" to display, input "2" to start game or "3" to quit | As Expected |
| Start Game | choose option "1" to load the game start page | Choose a number | As Expected |
| Quit game   | Quit the game | Input option "3" | As Expected |
| Guess a number   | Prompts user to guess a number | Input a number guess | As Expected |
| You missed  | To display an x on the board if you didnt hit the ship | Guessed a wrong coordinate | As Expected |
| You Hit | You hit their ship - show an H on the board where you hit the ship | Guessed the right coordinate | As Expected |
| Guessed Already   | To display a message saying to redo guess as they have already guessed this number | Invalid input | As Expected |
| Guess within the board  | To display a message saying to enter a value between 1 and 4 | Input a valid number  | As Expected | 
| Win   | To display win message | Win the game in less than 5 tries | As Expected | 
| Lose   | To display lose message | Fail to guess the positioning in 5 tries | As Expected | 
| Play Again   | To display play again | Choose "y" for yes and "n" to end the game | As Expected |

## Input validation testing

* Display rules
    * Option to start game or choose to view rules.

![Rules validation](/assets/images/rule-page.png)

* Choosing a number
    * Cannot continue without a valid number
    * must choose within the numbers 0-4

![Within the board validation](/assets/images/within-the-board-validation.png)

* Guess a number
    * Cannot continue with empty input
    * Must be an integer

![Integer validation](/assets/images/valid-integer-validation.png)

* Restart game?
    * Must be "y" or "n"

![Play again validation](/assets/images/restart-game.png)

## Fixed Bugs

* There was a bug that stopped from showing the computers plays on the board, this was identified by playing the game and watching the two boards.
* There was abug in that google sheets error message would come up after playing the game too fast. This bus was fixed by limiting the player to only 5 tries and the warning message did not come up again. 
* The bugs were identified by playing the game multiple times to ensure all bugs would be seen.

## Deployment

### Deploying to Heroku

To deploy with Heroku, Code Institute Python Essentials Template was used so the python code can be viewed in a terminal in a browser
1. Log in to Heroku or create a new account
2. On the main page click "New" and select "Create new app"
3. Choose your unique app name and select your region
4. Click "Create app"
5. On the next page find "settings" and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" key and value "8000", click "Add"
7. Scroll down, locate "Buildpack" and click "Add", select "Python"
8. Repeat step 7. only this time add "Node.js", make sure "Python" is first
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository and link them together
11. Scroll down and select either "Enable Automatic Deploys" or "Manual Deploy"
12. Deployed site [Battleships](https://battleshipspp3-28-c593d68c5099.herokuapp.com/)

### Forking the GitHub Repository

By forking the repository, we make a copy of the original repository on our GitHub account to view and change without affecting the original repository by using these steps:

1. Log in to GitHub and locate [GitHub Repository Battleships](https://github.com/nickyd1996/battleships_pp3)
2. At the top of the Repository(under the main navigation) locate "Fork" button.
3. Now you should have a copy of the original repository in your GitHub account.

### Local Clone

1. Log in to GitHub and locate [GitHub Repository Battleships](https://github.com/nickyd1996/battleships_pp3)
2. Under the repository name click "Clone or download"
3. Click on the code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone` and then paste The URL copied in the step 3.
7. Press Enter and your local clone will be created.

## Credits

### Code

* I gained understanding of python through code institute lessons.

### Content

* Battleships game
* All content was written by the developer.

## Acknowledgements

 * My mentor Mitko Bachvarov provided helpful feedback.
