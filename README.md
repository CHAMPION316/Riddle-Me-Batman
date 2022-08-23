# Riddle Me Batman
![Riddle Me Batman](wireframes/images/responsive.jpg)

# Goal for this Project
The goal of this project is to solve the riddles set forth by The Riddler. These riddles will be associated with other superheroes/villains from the DC Universe. The player will get to choose letters from the whole english alphabet in order to spell out the hero/villain that he/she thinks The Riddler is referring to. (You) the user are Batman and your job is to save Robin who is currently kidnapped. The player will have 6 chances at spelling out these names otherwise The Riddler will hang Robin.

# Table of Contents
* [UX](#ux "UX")

## User Goals
* Read rules
* Type in a user name
* View High Scores
* Exit the Game

## User Stories
* As a user, I want to be able create a user name 
* As a user, I want to read the rules
* As a user, I want to skip through game instructions if required
* As a user, I want to know the outcome of the game

## User Requirements and Expectations

### Requirements
* Single page layout
* Feedback on performance
* Clear instruction as to when the game starts and finishes
* Validation of user inputs
* Feedback to the user on their input to the game

### Expectations
* I expect to know that it is my game based on a username
* I expect to know when the game starts and finishes
* I expect to have the option of reading the rules or not
* I expect not to be able to make any typing errors
* I expect feedback on performance

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## How to Play

* Will play like the standard paper and pencil game of hangman
    * 1 Player Game
    * Words will be randomized
    * Lives will be deducted for incorrect guesses
* User will be given a riddle to solve the word
    * The player creates a username
    * Words care completely randomized
    * The user decides what letters they choose
* Player will be given 6 chances to figure out the word
* If player can't figure out the word they lose the game
* If player figures out the word the move on to the next word

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

## Design Choices
### Fonts

The terminal that was provided by Code Institute to complete this project, used a standard monospace font. Which is the font I decided to keep using.

### Colours

The colour scheme I have chosen is based on what The Riddler uses as his colors in the comics [Riddler Costume](https://www.gamelivestory.com/images/article/batman-8-times-riddler-acted-like-a-hero-in-the-comics-main.webp "Riddler Custome Colors"). Which was a bright [lime green](wireframes/images/color_contrast_green.png) and [electric purple](wireframes/images/color_contrast_purple.png). I used [Coolors](https://coolors.co/ "Coolors") to create the colors myself instead of generating them randomly since I already knew what I wanted. [contrast checker](https://webaim.org/resources/contrastchecker/ "contract checker") was used to contrast the colors as my background choice with a black foreground text. Only the electric purple didn't pass in one catergory. Regardless I won't have text over these colors since they will only be the background colors and not run in the termimal.

[Colour Scheme](wireframes/images/coolors_scheme.png)

### Images

No images were used for this game, however, to have the title stand out, I used [patorjk.com](http://patorjk.com/software/taag/#p=display&h=1&f=Big&t=Riddle%20Me%20Batman%0A) with the font set to *Calvin S* to create giant text that would appear as though it's an image on the home terminal.

\
&nbsp;

![Riddle Me Batman](wireframes/images/riddle-font.jpg)


### Structure
The structure of this project has been mapped out using [App Diagrams](https://app.diagrams.net/ "app diagrams"), all the shapes were chosen by me to diagram the flow of the project.

\
&nbsp;
![Begining of game flow](wireframes/structure-images/flow-key.jpg)
\
&nbsp;


I created 3 choice inputs for the start of the game.

1. Start Game
2. High Scores
3. Exit

From ther the logic can be followed with the flow chart structure below. 

\
&nbsp;
![Flow chart part 1](wireframes/structure-images/riddle-flow-chart-pt1.jpg)
![Flow chart part 2](wireframes/structure-images/riddle-flow-chart-pt2.jpg)
\
&nbsp;

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Wireframes

The game will be built using a pre-built template that Code Institute has provided. This template already scales down for different screen sizes. For this reason I kept my wireframes simple.

* [Mobile Wireframe](wireframes/wireframe-images/mobile.png "Mobile")

* [Tablet Wireframe](wireframes/wireframe-images/tablet.png "Tablet")

* [Desktop Wireframe](wireframes/wireframe-images/desktop.png "Desktop")

\
&nbsp;
[Back to Top](#table-of-contents)
\
&nbsp;

# Features

## Existing Features

Image of the home screen when the player runs the program. The user will be greeted with the 3 input options.
    * Play Game
    * High Scores
    * Exit

\
&nbsp;

![Home Screen](wireframes/images/home-image.jpg)

\
&nbsp;

* The next image is of the game itself which is that of the old school hangman game but with the twist that it's Robin you have to save from being hung. The user with have to guess letters 1 by 1 in order to solve the word. When the user makes a guess whether correct or wong a * asterisk will fill the place of the letters gussed so the user knows not to choose that letter again. However in this game that is still a possibility in which the user will get a string that let's them know they already guessed that letter and still waste an attempt. 

\
&nbsp;

![Play Game](wireframes/images/play-image.jpg)

\
&nbsp;

* The score image list the top 5 players who were able to guess the most DC characters ever. If a user surpasses the score of of anyone of the top 5 players they will be added to the top 5 list and remove those that have the lowest score.

\
&nbsp;

![Scores](wireframes/images/score-image.jpg)

\
&nbsp;

* The username input field appears at the bottom underneath the game letters. From there the player will create a username that will allow them to play the game and have the chance to have their name recorded into the top 5 list if they are good enough.

\
&nbsp;

![Username](wireframes/images/username-image.jpg)

\
&nbsp;

* Guess the letters screen allows the player to guess what letters belong in the word.

\
&nbsp;

![Guess](wireframes/images/guess-image.jpg)

\
&nbsp;

* Guessing incorrectly results in the following image within the game.

\
&nbsp;

![Guess Wrong](wireframes/images/guess-wrong.jpg)

\
&nbsp;

* Guessing correctly results in the following image within the game.

\
&nbsp;

![Guess Correct](wireframes/images/guess-correct.jpg)

\
&nbsp;

* A repeated guess results in the following image.

\
&nbsp;

![Repeat Guess](wireframes/images/repeat-guess.jpg)

\
&nbsp;

* Winning the game results in the following image with the 2 options to play again or not by using the following inputs.
    * 'Y' for Yes
    * 'N' for No

\
&nbsp;

![Win](wireframes/images/win-image.jpg)

\
&nbsp;

* Losing the game results in the following image with the 2 options to play again or not by using the following inputs.
    * 'Y' for Yes
    * 'N' for No

\
&nbsp;

![Lose](wireframes/images/lose-image.jpg)

\
&nbsp;

* Google spreadsheets works with the data being sent to it by the game.
    * Username
    * Score

\
&nbsp;

![Data](wireframes/images/data-image.jpg)

\
&nbsp;

## Features to be Implemented

1. Riddle array that attaches at the bottom of the game letters box
1. Sound effects for guessing the correct letter and wrong letter