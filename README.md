# schwarbot
Dean DiPaolo, Logan Marks, Ray Mele
CIS 1051 Spring 2023

Schwarbot is a Discord Bot that sends Kyle Schwarber's stats on command

Intial Project: 
Send out a Tweet every time Phillies’ outfielder Kyle Schwarber hits a homerun.
Twitter API policy changed and we were unaware the free version was not available to us, so we switched to Discord.
Also, we could not get our code to run continuously to automatically send a message when Kyle records a homerun, so we switched it to send his stats on demand.

Data Source:
Phillies website has Schwarber's 2023 and career stats (https://www.mlb.com/player/kyle-schwarber-656941?season=2023&team=143)

Google Sheet was used to extract the data table from the Phillies’ website using Import HTML function.
GSpread was installed from pip to refresh and pull data from the Google Sheet.
Source: https://docs.gspread.org/en/v5.7.1/#installation

Use Discord Developer Portal to make “Schwarbot”
Give it the required permissions to send and receive messages

Link to Video Presentation: 
