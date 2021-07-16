### Game Profile Manager

The solution to creating multiple profiles or playthroughs of single player games.

As a PC gamer sharing a PC with siblings, I found there are a ton of games out there that do not support profiles or save slots. Super annoying when you have other users on the same device who have started a save. You'd normally find clicking on 'New Game' would pull up prompts like 'All previous progress will be lost when creating a new game. Do you want to continue', sigh!

Originally developed in 2009 for the sole purpose of the app handling profiles for Need for Speed: Shift. It became apparent this app would need to support any number of games and any number of profiles. So here we are with my first GitHub version to share with the gaming community.

### Installation

Unzip Game Profile Manager to a location of choice. For initial release i would suggestion placing it outside of program files.

Ensure the folder structure is as follows
Game Profile Manager    > img
                        > GameProfileManager.exe

![Folder structure](userguide_img/folders.png)

### Startup

On startup Game Profile Manager will provide a prompt

### Dependencies

- [pylnk3](https://github.com/strayge/pylnk)
- [Pillow](https://pillow.readthedocs.io/en/stable/)