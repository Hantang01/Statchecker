import requests
import datetime
import math

plusrank = "s"
key = '8b0a23da-b538-443c-a475-2ad10a723b08'

prstg = {'0': 'None ✫',
        '1': 'Iron',
        '2': 'Gold ✫',
        '3': 'Diamond ✫',
        '4': 'Emerald ✫',
        '5': 'Sapphire ✫',
        '6': 'Ruby ✫',
        '7': 'Crystal ✫',
        '8': 'Opal ✫',
        '9': 'Amethyst ✫',
        '10': 'Rainbow ✫',
        '11': 'Iron Prime ✪',
        '12': 'Gold Prime ✪',
        '13': 'Diamond Prime ✪',
        '14': 'Emerald Prime ✪',
        '15': 'Sapphire Prime ✪',
        '16': 'Ruby Prime ✪',
        '17': 'Crystal Prime ✪',
        '18': 'Opal Prime ✪',
        '19': 'Amethyst Prime ✪',
        '20': 'Mirror ✪',
        '21': 'Light ⚝',
        '22': 'Dawn ⚝',
        '23': 'Dusk ⚝',
        '24': 'Air ⚝',
        '25': 'Wind ⚝',
        '26': 'Nebula ⚝ ✫',
        '27': 'Thunder ⚝',
        '28': 'Earth ⚝',
        '29': 'Water ⚝',
        '30': 'Fire ⚝',
        '31': 'NoLifeMF ✫✪⚝'}

while True:
    WantedUsername = input("Who's stats would you like to check: ")
    try:
        MojangRequestlink = str("https://api.mojang.com/users/profiles/minecraft/" + WantedUsername)
        MojangApi = requests.get(MojangRequestlink).json()
        WantedPlayerUUID = MojangApi["id"]
        
    except:
        validPlayer = False
        print("Invalid player")
        break

    try:
        EndpointLink = ("http://api.hypixel.net/player?key=" + key + "&uuid=" + WantedPlayerUUID)
        HypixelData = requests.get(EndpointLink).json()

    except:
        print("Invalid/Malformed API key")
        break
        
    def Generalstats(HypixelData):
        plusrank = "test"
        try:
            karma = HypixelData["player"]['karma']
            karma = "{:,}".format(karma)
        except:
            karma = "0"
        
        try:
            discord = HypixelData["player"]["socialMedia"]["links"]["DISCORD"]
            forum = HypixelData["player"]["socialMedia"]["links"]["HYPIXEL"]
            youtube = HypixelData["player"]["socialMedia"]["links"]["YOUTUBE"]
            twitch = HypixelData["player"]["socialMedia"]["links"]["TWITCH"]
            twitter = HypixelData["player"]["socialMedia"]["links"]["TWITTER"]
        except:
            pass
        
        try:
            rank = HypixelData["player"]["newPackageRank"]
            
            try:
                plusrank = HypixelData["player"]["monthlyPackageRank"]
            except:
                pass
            
            if rank == "VIP":
                rank = "VIP"
            elif rank == "VIP_PLUS":
                rank = "VIP+"
            elif rank == "MVP":
                rank = "MVP"
            elif plusrank == "SUPERSTAR":
                rank = "MVP++"
            elif rank == "MVP_PLUS":
                rank = "MVP+"
            
            elif rank == "NONE":
                raise KeyError
            


        except KeyError:
            
            rank = "No rank"
            
        
        try:
            level = int(HypixelData["player"]["networkExp"])
            level = 1 + (-8750. + (8750**2 + 5000*level)**.5) / 2500
            level = round(level,2)
        except:
            level = "0"
        
        try:
            achievement = HypixelData["player"]["achievementPoints"]
        except:
            achievement = "0"
        
        try:
            firstLogin_unix_time = HypixelData["player"]["firstLogin"]
            firstLogin_unix_time = str(firstLogin_unix_time)[0:10]
            date_time = datetime.datetime.fromtimestamp(int(firstLogin_unix_time))
            date_time = date_time.strftime('%Y-%m-%d %H:%M:%S:%M')
        except:
            pass
        try:
            try:
                lastLogout = int(HypixelData["player"]["lastLogout"])
            except:
                pass
            try:
                lastLogin = int(HypixelData["player"]["lastLogin"])
            except:
                pass
            if lastLogin > lastLogout:
                OnlineStatus = "Online"
            if lastLogout > lastLogin:
                OnlineStatus = "Offline"
        except:
            OnlineStatus = "(login/logout api disabled)"
            
        try:
            lastLogin_unix_time = HypixelData["player"]["lastLogin"]
            lastLogin_unix_time = str(lastLogin_unix_time)[0:10]
            lidate_time = datetime.datetime.fromtimestamp(int(lastLogin_unix_time))
            lidate_time = lidate_time.strftime('%Y-%m-%d %H:%M:%S:%M')
        except:
            lidate_time = "(last login api disabled)"
            
        try:
            prefix = HypixelData["player"]["prefix"]
            rank = prefix
        except:
            pass
        
        
        try:
            guildlink = ("https://api.hypixel.net/findGuild?key=" + key + "&byUuid=" + WantedPlayerUUID)
            guildIDData = requests.get(guildlink).json()
            guildID = guildIDData["guild"]
            guildinfo = ("https://api.hypixel.net/guild?key=" + key + "&id=" + guildID)
            guildData = requests.get(guildinfo).json()
            guild = guildData["guild"]["name"]
        except:
            guild = "(No guild)"
        print("------------------------------+General+------------------------------")
        print("Karma: " + karma)
        print("Rank: " + rank)
        print("Level: " + str(level))
        print("Achievement Points: " + str(achievement))
        print("---+Social Media+---")
        try:
            print("Discord: " + discord)
            print("Forum: " + forum)
            print("Twitch: " + twitch)
            print("Twitter: " + twitter)
            print("Youtube: " + youtube)
            
        except:
            pass
        print("---+Calender+---")
        print("First Login: " + date_time)
        print("Last Login: " + lidate_time)
        print("Player is in the : " + guild + " guild")
        print("Online Status: " +OnlineStatus)
        
    def BedwarsStats(HypixelData):
        try:
            level = int(HypixelData["player"]["stats"]["Bedwars"]["Experience"])
            level = (level/(7000+96*5000))*100
            lprstg = level/100
            lprstg = int(round(lprstg,0))
            lprstg = math.trunc(lprstg)
            x = str(lprstg)
            if level > 3100:
                x = '31'
            level = str(round(level,2))
        except:
            level = '0'
            lprstg = '0'
        
            
        try:
            kills = int(HypixelData["player"]["stats"]["Bedwars"]["kills_bedwars"])
            deaths = int(HypixelData["player"]["stats"]["Bedwars"]["deaths_bedwars"])
                
            
            KDR = kills/deaths
            KDR = str(round(KDR,2))
            kills = str(kills)
        except:
            kills = "0"
            KDR = "0"
            
        try:
            bedkills = int(HypixelData["player"]["stats"]["Bedwars"]["beds_broken_bedwars"])
            beddeaths = int(HypixelData["player"]["stats"]["Bedwars"]["beds_lost_bedwars"])
            
            
            BKDR = bedkills/beddeaths
            BKDR = str(round(BKDR,2))
            bedkills = str(bedkills)
        except:
            bedkills = "0"
            BKDR = "0"
            
        try:
            fkills = int(HypixelData["player"]["stats"]["Bedwars"]["final_kills_bedwars"])
            fdeaths = int(HypixelData["player"]["stats"]["Bedwars"]["final_deaths_bedwars"])
                    
                
            FKDR = fkills/fdeaths
            FKDR = str(round(FKDR,2))
            fkills = str(fkills)
        except:
            fkills = "0"
            FKDR = "0"
        
    
        print("------------------------------+Bedwars+------------------------------")
        print("Level: " + level + " | Prestige: " + prstg[x])

        print("Kills: " + kills + " | KDR: " + KDR)
        print("Bed kills: " + bedkills + " | BKDR: " + BKDR)
        print("Final Kills: " + fkills + " | FKDR: " + FKDR)
    def SkywarsStats(HypixelData):
        try:
            level = HypixelData["player"]["stats"]["SkyWars"]["levelFormatted"]
            level = re.sub('§0|§1|§2|§3|§4|§5|§6|§7|§8|§9|§a|§b|§c|§d|§e|§k|§m|§o|§l|§n|§r|§f', '', level)
        except:
            level = '0'
        
        try:
            kills = HypixelData["player"]["stats"]["SkyWars"]["kills"]
            deaths = HypixelData["player"]["stats"]["SkyWars"]["deaths"]
            KDR = int(kills)/int(deaths)
            KDR = str(round(KDR,2))
            kills = str(kills)
        except:
            KDR = '0'
            kills = '0'
        
        try:
            wins = HypixelData["player"]["stats"]["SkyWars"]["wins"]
            losses = HypixelData["player"]["stats"]["SkyWars"]["losses"]
            WLR = int(wins)/int(losses)
            WLR = str(round(WLR,2))
            wins = str(wins)
        except:
            wins = '0'
            WLR = '0'
        
        try:
            assists = str(HypixelData["player"]["stats"]["SkyWars"]["assists"])
        except:
            assists = '0'
            
        print("------------------------------+Skywars+------------------------------")
        print("Level: " + level)
        print("Kills: " + kills + " | KDR: " + KDR)
        print("Wins: " + wins + " | KDR: " + WLR)
        print("Assists: " + assists)
        
    def DuelsStats(HypixelData):
        try:
            kills = HypixelData["player"]["stats"]["Duels"]["kills"]
            deaths = HypixelData["player"]["stats"]["Duels"]["deaths"]
            KDR = int(kills)/int(deaths)
            KDR = str(round(KDR,2))
            kills = str(kills)
        except:
            KDR = '0'
            kills = '0'
        
        try:
            wins = HypixelData["player"]["stats"]["Duels"]["wins"]
            losses = HypixelData["player"]["stats"]["Duels"]["losses"]
            WLR = int(wins)/int(losses)
            WLR = str(round(WLR,2))
            wins = str(wins)
        except:
            wins = '0'
            WLR = '0'
        
        print("------------------------------+Duels+------------------------------")
        print("Kills: " + kills + " | KDR: " + KDR)
        print("Wins: " + wins + " | KDR: " + WLR)
        
    Generalstats(HypixelData)
    BedwarsStats(HypixelData)
    SkywarsStats(HypixelData)
    DuelsStats(HypixelData)


    
    

    


