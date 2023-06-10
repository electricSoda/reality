# Reality
v0.1.0 beta

Reality monitors your computer usage and separates it into categories so you can see how much time you actually spend on specific things.


#### Features so far
- Pie chart display
- Hover over pie chart to see time spent

That's it! Hopefully you can see the reality of how bad (or good) you spend your time on your computer.

#### Tracked.json
This is a json file that stores which windows to track. The key is the executable name (without the .exe), and the value is a dictionary, formatted like so: 
`"Name of category": "Regex corresponding to the current window title"`

#### Installation (windows only)
pyinstaller --onefile --windowed --add-data "favicon.png;." --icon=favicon.ico main.py
> **Warning**
> make sure to have the file, `tracked.json` in the same directory as the .exe, or else the program won't work

