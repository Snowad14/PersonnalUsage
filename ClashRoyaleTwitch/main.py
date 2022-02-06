import json
import requests
from twitchio.ext import commands
from pymongo import MongoClient

KEY_ACCESS = "YOUR CLASH ROYALE API KEY"
client = MongoClient("YOUR DATABASE CONNECTION")
DB = client["NAME OF DB"]
col = DB["NAME OF COLLECTION"]

def Check(playerid):
    playerid = playerid.replace('#', '%23')
    try:
        r = requests.get(f"https://api.clashroyale.com/v1/players/{playerid}/battlelog",
                         headers={"Accept": "application/json", "authorization": "Bearer " + KEY_ACCESS},
                         params={"limit": 20})
    except:
        return False

    NeededCard = ["Goblins", "Giant", "Bomber", "Skeleton Army", "Tombstone", "Barbarians", "Archers", "Minions"]
    for card in NeededCard:
        try:
            if card not in (json.dumps(r.json())):
                return False
        except:
            return False
    return True

def getTrophy(playerid):
    playerid = playerid.replace('#', '%23')
    r = requests.get(f"https://api.clashroyale.com/v1/players/{playerid}",
                     headers={"Accept": "application/json", "authorization": "Bearer " + KEY_ACCESS},
                     params={"limit": 20})
    data = r.json()
    return data["leagueStatistics"]["currentSeason"]["trophies"]


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token='YOUR TWITCH KEY', prefix='?', initial_channels=['#NAMEOFSTREAMER'])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        

    @commands.command(name='login')
    async def login_command(self, ctx, arg = "default"):

        if arg == "default":
            await ctx.reply(f"Please add an argument")
            return

        arg = arg.replace('@', '')

        if col.count_documents({"ClashRoyale": arg}):
            await ctx.reply(f"This user is already registered!")
            return

        if Check(arg):
            await ctx.reply(f"Account Validate  !")
            col.insert_one({"Twitch": ctx.author.name, "ClashRoyale": str(arg)})
        else:
            await ctx.reply(f"You have not met the conditions!")

    @commands.command(name='get')
    async def get_command(self, ctx, arg = "default"):

        if arg == "default":
            await ctx.reply(f"Please specify a user!")
            return

        if not col.count_documents({"Twitch": arg}):
            await ctx.reply(f"This user is not registered!")
            return

        arg = arg.replace('@', '')
        clashRoyaleData = col.find_one({"Twitch": arg}, {'_id': 0, "ClashRoyale": 1})
        trophy = getTrophy(clashRoyaleData["ClashRoyale"])
        await ctx.reply(f"This user has {str(trophy)} trophy")

bot = Bot()
bot.run()