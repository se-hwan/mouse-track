# Description
Lightweight Python script to track mouse position and clicks in Windows built from scratch.

Wanted to practice more Python, and given my time spent in Valorant, League, and Osu, thought it would be interesting to see how that might look visually.

# Dependencies
- pywin32
- numpy
- matplotlib

Each can be installed with ```pip install [dependency]``` from ```cmd.exe``` in Windows.

# Installation
1. Download and install Python 3.7.x from here: https://www.python.org/downloads/windows/
2. Ensure that Python is added to the PATH during the installation window.
3. In the Windows search bar, type ```cmd.exe``` and launch the command prompt.
4. type ```py --version``` to confirm Python was installed correctly.
5. Install each of the dependencies above with ```pip install```.
6. Run ```main.py``` to begin recording. Press ```Enter``` key inside terminal window to finish recording. 
7. Modify savefile names or code by editing ```.py``` files in IDLE (right click, edit with)

# Results
Valorant:
![Valorant mouse map](/images/valorant.png)
Osu:
![Osu mouse map](/images/osu.png)
League:
![League mouse map](/images/league.png)

# Future Updates
- Make plots more visually appealing
- Analyze mouse position/click data for heatmaps, variances, etc.
- Compare data over time --> correlation with skill? 
- Scrape tracking data from streamers/professional games? 
