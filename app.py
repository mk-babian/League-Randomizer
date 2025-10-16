from flask import Flask, render_template, request, jsonify
import time

championList = ["Aatrox", "Illaoi", "Qiyana", "Ahri", "Irelia", "Quinn", "Akali", "Ivern", "Rakan", "Akshan", "Janna", "Rammus", "Alistar", "Jarvan IV", "Rek'Sai",
                "Ambessa", "Jax", "Rell", "Amumu", "Jayce", "Renata Glasc", "Anivia", "Jhin", "Renekton", "Annie", "Jinx", "Rengar", "Aphelios", "Kai'Sa", "Riven",
                "Ashe", "Kalista", "Rumble", "Aurelion Sol", "Karma", "Ryze", "Aurora", "Karthus", "Samira", "Azir", "Kassadin", "Sejuani", "Bard", "Katarina",
                "Senna", "Bel'Veth", "Kayle", "Seraphine", "Blitzcrank", "Kayn", "Sett", "Brand", "Kennen", "Shaco", "Braum", "Kha'Zix", "Shen", "Briar",
                "Kindred", "Shyvana", "Caitlyn", "Kled", "Singed", "Camille", "Kog'Maw", "Sion", "Cassiopeia", "K'Sante", "Sivir", "Cho'Gath", "LeBlanc",
                "Skarner", "Corki", "Lee Sin", "Smolder", "Darius", "Leona", "Sona", "Diana", "Lillia", "Soraka", "Dr. Mundo", "Lissandra", "Swain", "Draven",
                "Lucian", "Sylas", "Ekko", "Lulu", "Syndra", "Elise", "Lux", "Tahm Kench", "Evelynn", "Malphite", "Taliyah", "Ezreal", "Malzahar", "Talon",
                "Fiddlesticks", "Maokai", "Taric", "Fiora", "Master Yi", "Teemo", "Fizz", "Milio", "Thresh", "Galio", "Miss Fortune", "Tristana", "Gangplank",
                "Mordekaiser", "Trundle", "Garen", "Morgana", "Tryndamere", "Gnar", "Naafiri", "Twisted Fate", "Gragas", "Nami", "Twitch", "Graves", "Nasus", "Udyr",
                "Gwen", "Nautilus", "Urgot", "Hecarim", "Neeko", "Varus", "Heimerdinger", "Nidalee", "Vayne", "Hwei", "Nilah", "Veigar", "Nocturne", "Vel'Koz",
                "Nunu & Willump", "Vex", "Olaf", "Vi", "Orianna", "Viego", "Ornn", "Viktor", "Pantheon", "Vladimir", "Poppy", "Volibear", "Pyke", "Warwick", "Wukong",
                "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yunara", "Yuumi", "Zac", "Zed", "Zeri", "Ziggs", "Zilean", "Zoe", "Zyra"]

legendaryItems = ["Rabadon's Deathcap", "Infinity Edge", "Bloodthirster", "Trinity Force", "Overlord's Bloodmail", "Mortal Reminder", "Ravenous Hydra", "Titanic Hydra",
                  "Death's Dance", "Stridebreaker", "Zhonya's Hourglass", "Guardian Angel", "Sterak's Gage", "Mercurial Scimitar", "Blade of The Ruined King",
                  "Shadowflame", "Jak'Sho, The Protean", "Lord Dominik's Regards", "Warmog's Armor", "Maw of Malmortius", "Spear of Shojin", "Riftmaker",
                  "Chempunk Chainsword", "Sundered Sky", "Yun Tal Wildarrows", "Black Cleaver", "Experimental Hexplate", "Heartsteel", "Banshee's Veil",
                  "Guinsoo's Rageblade", "Void Staff", "Cryptbloom", "Hullbreaker", "Terminus", "Edge of Night", "Cosmic Drive", "Silvermere Dawn",
                  "Liandry's Torment", "Kraken Slayer", "Immortal Shieldbow", "The Collector", "Serylda's Grudge", "Hubris", "Voltaic Cyclosword",
                  "Kaenic Rookern", "Archangel's Staff", "Manamune", "Lich Bane", "Nashor's Tooth", "Essence Reaver", "Dead Man's Plate", "Iceborn Gauntlet",
                  "Eclipse", "Morellonomicon", "Profane Hydra", "Unending Despair", "Blackfire Torch", "Wit's End", "Youmuu's Ghostblade", "Force of Nature",
                  "Stormsurge", "Hollow Radiance", "Horizon Focus", "Luden's Companion", "Axiom Arc", "Spirit Visage", "Sunfire Aegis", "Statikk Shiv",
                  "Malignance", "Randuin's Omen", "Opportunity", "Phantom Dancer", "Runaan's Hurricane", "Rapid Firecannon", "Hextech Rocketbelt",
                  "Navori Flickerblade", "Abyssal Mask", "Rylai's Crystal Scepter", "Rod of Ages", "Frozen Heart", "Umbral Glaive", "Bloodletter's Curse",
                  "Dawncore", "Serpent's Fang", "Thornmail", "Trailblazer", "Winter's Approach", "Fimbulwinter", "Redemption", "Knight's Vow",
                  "Mikael's Blessing", "Vigilant Wardstone", "Imperial Mandate", "Staff of Flowing Water", "Shurelya's Battlesong", "Zeke's Convergence",
                  "Locket of the Iron Solari", "Ardent Censer", "Moonstone Renewer", "Echoes of Helia", "Mejai's Soulstealer", "Celestial Opposition",
                  "Dream Maker", "Zaz'Zak's Realmspike", "Solstice Sleigh", "Bloodsong"]

bootItems = ["Mercury's Treads", "Plated Steelcaps", "Berserker's Greaves", "Sorcerer's Shoes", "Boots of Swiftness", "Symbiotic Soles", "Synchronized Souls", 
             "Ionian Boots of Lucidity"]

starterItems = ["Doran's Shield", "Doran's Blade", "Cull", "Scorchclaw Pup", "Gustwalker Hatchling", "Mosstomper Seedling", "Doran's Ring", "Tear of the Goddess",
                "World Atlas", "Dark Seal"]

consumableItems = ["Refillable Potion", "Health Potion, Control Ward"]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/button_action')
def button_action():
    mouse_x = int(request.args.get('x', 0))
    seconds = time.time()
    index = (int(seconds) * mouse_x) % len(championList)
    return jsonify({'Champion': championList[index]})

if __name__ == "__main__":
    app.run(debug=True)