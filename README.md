# Practice-Project

## Project Summary
WIP Text Adventure Game. The game is a Murder Mystery where you and a detective have to solve a murder case at the local circus. The game uses the Renpy engine which is incredibly versitile and very in depth. The main language used for the Project was Python.
Currently the Project is very unfinished in terms of it's story and what not. However I was able to include a good number of mechanics such as:
- Custom Player Name
- Music that loops
- Smooth Character Movement
- A Menu for Multiple Paths
- Text "Blips" (Currently Commented Out as they act a little weird)

## Technical Summary
For the project the main thing that I used was the Renpy Documentation that was on there website:
- https://www.renpy.org/doc/html/

However, there were a few things that had caused a lot of issues. The main thing that was such a struggle was getting the text blips to work. As a matter of fact they still *kind* of don't work. The reason why they work the way that they are intended to was because that feature was removed in a later version of the program so I had to try and cobble together a makeshift version using what I could with the information Online.

Another issue that I encountered was organization. Being a murder mystery game the same is some what open in terms of progression. and organizing everything in one file began to become a very huge hassle. However after doing a little bit of research I learned that the game does just check for the script.rpy file but all rpy files. This made organization a lot easier as it meant that I could add the testimony script in a seprate file from the investigation script.

## How I Did it
The basics of just getting a character is really simple. It starts off with defining a character and there sprite/sprites as a letter value. You are also able to give there name a custom color in the gui with a hex value
```
define d = Character("Detective", color="#c70039")

d "I am a detective"
```

While defining preset characters is relatively simple the act of adding a player character with custom name is a little more awkward.
