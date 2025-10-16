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