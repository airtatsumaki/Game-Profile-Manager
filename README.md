# Game Profile Manager

The solution to creating multiple profiles or playthroughs of single player games.

As a PC gamer sharing a PC with siblings, I found there are a ton of games out there that do not support profiles or save slots. Super annoying when you have other users on the same device who have started a save. You'd normally find clicking on 'New Game' would pull up prompts like 'All previous progress will be lost when creating a new game. Do you want to continue', sigh!

Originally developed in 2009 for the sole purpose of handling profiles for Need for Speed: Shift. It became apparent this app would need to support any number of games and profiles. So here we are with my first GitHub version to share with the gaming community.

## Installation

Unzip Game Profile Manager to a location of choice. For initial release i would suggestion placing it outside of program files.

Ensure the folder structure is as follows:  
Game Profile Manager  
&nbsp;&nbsp;&nbsp;> img  
&nbsp;&nbsp;&nbsp;> GameProfileManager.exe

![Folder structure](userguide_img/folders.png)  
## Startup

On startup Game Profile Manager will provide a prompt to say you do not have any profiles or games added. This is normal of course. Once you start added profiles and games these will be saved into the 'resources/' folder along with save game files once you start playing.

## Navigation

The top menu bar is where users can navigate to different app features.  

<ul>
<li /><strong>Home</strong> - this is the default page of the app. Here you can select your game and the profile and run the game.
<li /><strong>Profile management</strong> - here is where you can add and delete profiles. Note, deleting a profile will not delete the save games in the 'resources/' folder. You never know when you might need that save again.
<li /><strong>Game management</strong> - here is where you can add and delete games. Note, deleting doesn't uninstall the game. It simply breaks Gampe Profile Managers tie to the game. This will also not delete any saved data ino the 'resources/' folder.
</ul>

![Navigation  bar](userguide_img/navigation.png)

## Adding/ deleting a profile

A profile can be added on the left side of the Profile management screen. You can also delete profiles on the right side of the screen.

![Profile management screen](userguide_img/profile_management.png)

## Adding/ deleting a game

Adding a game is a bit more involved but its worth it. On the left of the game page you will see 3 boxes:

<ul>
<li /><strong>Name</strong> - this will be the name of the game. You can name the games whatever you like it doesn't need to match the actual games name.
<li /><strong>.exe or steam URL 'steam://rungameid/XXXXXX'</strong> - here is where you can add the games .exe path (advised for non-steam games) or add the steam url of the game. More about finding the steam url for a given game below.
<li /><strong>Save location</strong> - this is where the game of your chose is currently storing its saved data. Every game stores it's save data in a different place so you'd need to find out there that is. Google is your friend here but I aim to provide this information on a wiki page for ease of use. It won't list every game, but it will be a start.
</ul>

### Launching a game

On the homepage, choose the profile and game and hit play game. Simple!


## Finding the steam url of a game

Game Profile Manmager supports the use of steam game urls. Steam shortcuts do not contain paths to exact files but instead contain a steam url link. When triggered steam kicks in and launches the game. Lets look at 2 ways to get this url.

<ol>
<li/><strong>Creating a desktop shorcut</strong> - find the steam game of choice in your steam library. Right click and select Manage > Add desktop shortcut. Right click the desktop icon and select Properties.  

![Steam game url from shorcut](userguide_img/steam_shortcut.png)

<li/><strong>Finding the steam game id</strong> - find the steam game of choice in your steam library. Right click and select 'Properties...'. In the app properties window select the UPDATES tab and you will see the app id. When adding this app id to Game Profile Manager you will need to prefix the app id with the full steam url 'steam://rungameid/APP_ID_HERE'.

![Steam app id](userguide_img/steam_appid.png)
</ol>

## Adding an example game (Race Driver: Grid (2008)

Lets run through a worked example of using the app from start to finish with Race Driver: Grid. Although this game supports steam family sharing it does not link save games to the active steam user. So even though multiple steam users can play this game, if on the same device, they will share the same save game data. Not ideal.

### Adding Grid to Game Profile Manager

To go Game Management via the menu bar then enter the following information.  
<ul>
<li />Name: GRID
<li />.exe or steam URL 'steam://rungameid/XXXXXX': steam://rungameid/12750
<li />Save file location: C:\Users\user\Documents\Codemasters\GRID\savegame
</ul>

That's it. Now add a profile (Profile A) and play the game. When a new profile (Profile B) is selected you will notice that Profile B will have their own save files created while Profile A's save files will be backed up into the 'resources/' folder which will be location in the root of the Game Profile Manager folder.

## Dependencies

- [pylnk3](https://github.com/strayge/pylnk)
- [Pillow](https://pillow.readthedocs.io/en/stable/)