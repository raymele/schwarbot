#Schwarbot
#Spring 2023
#Dean DiPaolo, Logan Marks, Ray Mele



# Schwarber Stuff

import gspread

gc = gspread.service_account("credentials.json") #credentials.json in same folder as this program

def schwarbombDataImport():
    #from https://docs.gspread.org/en/v5.7.1/#installation
    # Open a sheet from a spreadsheet in one go
    wks = gc.open("Test Schwarbomb data v1").sheet1  #in raymond.mele@gmail.com googledrive shared with google api 
    #clears cell B7 so data can be updated
    wks.update('B7',0)
    # Updates google sheet with current data from savant stat site
    #wks.update('A1',[['=IMPORTHTML("https://baseballsavant.mlb.com/savant-player/kyle-schwarber-656941?stats=statcast-r-hitting-mlb","table",1)']])
    wks.update('B7',5)
    #=IMPORTHTML("https://baseballsavant.mlb.com/savant-player/kyle-schwarber-656941?stats=statcast-r-hitting-mlb","table",1)

def howManySchwarberABs():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    numberOfABsSeason = stats.acell('B2').value
    numberOfABsTotal = stats.acell('B3').value
    return "There have been " + numberOfABsSeason, " Schwarber at bats this season, and ", numberOfABsTotal, " total."
               
def howManySchwarberRs():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    numberOfRsSeason = stats.acell('C2').value
    numberOfRsTotal = stats.acell('C3').value
    return "There have been " + numberOfRsSeason, " Schwarber runs this season, and ", numberOfRsTotal, " total."

def howManySchwarbombs():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    numberOfSchwarbombsSeason = stats.acell('E2').value
    numberOfSchwarbombsTotal = stats.acell('E3').value
    return "There have been " + numberOfSchwarbombsSeason + " Schwarbombs this season and ", numberOfSchwarbombsTotal, " total."

def howManySchwarberHits():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    numberOfHitsSeason = stats.acell('D2').value
    numberOfHitsTotal = stats.acell('D3').value
    return "There have been " + numberOfHitsSeason + " Schwarber hits this season, and ", numberOfHitsTotal, " total."

def howManySchwarberRBIs():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    numberOfRBIsSeason = stats.acell('F2').value
    numberOfRBIsTotal = stats.acell('F3').value
    return "There have been " + numberOfRBIsSeason + " Schwarber RBIS this season, and ", numberOfRBIsTotal, " total."

def howManySchwarberSBs():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    numberOfSBsSeason = stats.acell('G2').value
    numberOfSBsTotal = stats.acell('G3').value
    return "There have been " + numberOfSBsSeason + " Schwarber stolen bases this season, and ", numberOfSBsTotal, " total."

def SchwarberAVG():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    avgSeason = stats.acell('H2').value
    avgTotal = stats.acell('H3').value
    return "Schwarber has a batting average of " + avgSeason + " this season, and ", avgTotal, " total."

def SchwarberOBP():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    obpSeason = stats.acell('I2').value
    obpTotal = stats.acell('I3').value
    return "Schwarber has an on-base percentage of " + obpSeason + " this season, and ", obpTotal, " total."

def SchwarberOPS():
    schwarbombDataImport()
    stats = gc.open("Test Schwarbomb data v1").sheet1
    opsSeason = stats.acell('J2').value
    opsTotal = stats.acell('J3').value
    return "Schwarber has an OPS of " + opsSeason + " this season, and ", opsTotal, " total."


# Discord Stuff
# https://realpython.com/how-to-make-a-discord-bot-python/

import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    print('Received message: {0.content}'.format(message))
    if message.author == client.user:
        return
    # !hr !hits !abs !runs !rbis !sbs !avg !obp !ops
    if message.content.startswith('!hello'):
        await message.channel.send('Hello, I show Kyle Schwarber\'s stats on command. You can ask me for hr, hits, abs, runs, rbis, sbs, avg, obp, or ops by putting a ! in front of the stat you want.')
    if message.content.startswith('!hr'):
        print('Responding to ', message, 'command')
        await message.channel.send(howManySchwarbombs())
    if message.content.startswith('!hits'):
        print('Responding to ', message, 'command')
        await message.channel.send(howManySchwarberHits())
    if message.content.startswith('!abs'):
        print('Responding to ', message, 'command')
        await message.channel.send(howManySchwarberABs())
    if message.content.startswith('!runs'):
        print('Responding to ', message, 'command')
        await message.channel.send(howManySchwarberRs())
    if message.content.startswith('!rbis'):
        print('Responding to ', message, 'command')
        await message.channel.send(howManySchwarberRBIs())
    if message.content.startswith('!sbs'):
        print('Responding to ', message, 'command')
        await message.channel.send(howManySchwarberSBs())
    if message.content.startswith('!avg'):
        print('Responding to ', message, 'command')
        await message.channel.send(SchwarberAVG())
    if message.content.startswith('!obp'):
        print('Responding to ', message, 'command')
        await message.channel.send(SchwarberOBP())
    if message.content.startswith('!ops'):
        print('Responding to ', message, 'command')
        await message.channel.send(SchwarberOPS())

