# PumpkinHero
An open source rhythm game in Python

The game has a halloween theme and is designed to be used with a Makey Makey,
however you can just use the arrow keys if you prefer.

To run the game (from terminal but in an x-window session)
---------------
1. Clone the game by typing 'git clone https://github.con/filtoid/PumpkinHero
2. cd 'PumpkinHero'
3. python main.py

Troubleshooting
---------------
If you get an error along the lines of pygame not installed (should be installed on a Raspberry Pi by default) then you should try runnning either:

```pip install pygame```
or
```sudo apt-get install python-pygame```

Then rerun the instructions above

Rules
-----
You need to hit the button corresponding with the lane for each character as the leading edge (lower edge) of the graphic crosses into the yellow or green areas. If you hit the key in the yellow area you get 1 point and if you hit it in the green area you get 2 points.

To start a game press 's'

The characters and corresponding keys are as follows:

| Key      | Character | Position |
|----------|-----------|----------|
|Left      | Witch     | 1st      |
|Up        | Zombie    | 2nd      |
|Down      | Monster   | 3rd      |
|Right     | Skeleton  | 4th      |


Makey Makey
-----------
This game is designed to work with a Makey Makey. The Makey Makey works by mapping miscellaneous hardware to the arrow keys. This means that you can turn pumpkins into buttons corresponding to the swim lanes of the game (hence the name).

Support
-------
Curently this code only supports Linux and Windows. ~~It may work on Windows~~ It does work on Windows (with Pygame installed) but Pygame does not get keydown events in MacOS by default. Some clever trickery is needed to achieve this. If you can figure out how to get the keys to work on MacOS then please feel free to update the docs and send a pull request - it would be very gratefully received :)
