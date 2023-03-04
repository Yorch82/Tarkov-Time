import json, os, discord, requests
from discord.ext import commands

time_url = "https://tarkov-time.adam.id.au/api?type=plain"

class Crear_Respuesta():
    def __init__(self, title, content):
        self.title = title
        self.content = content

        self.respuesta = discord.Embed(
            title = self.title,
            description = self.content,
            colour = int("DC75FF", 16)
        )
    @property
    def enviar(self):
        return self.respuesta

def main():
    if os.path.exists('config.json'):
        with open('config.json') as f:
            config_data = json.load(f)
    else:
        template = {'prefix': '!', 'token': ""}
        with open('config.json', 'w') as f:
            json.dump(template, f)

    t = requests.session()
        
    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix = '!', intents = intents, description = "Tarkov Time")
    # Comandos
    @bot.command(name="time", description="Tiempo actual Tarkov")
    async def time(ctx):
        time = t.get(time_url)
        respuesta = Crear_Respuesta("El tiempo actual en Tarkov es: ", time.text)
        await ctx.reply(embed = respuesta.enviar)
        
    # Eventos
    bot.run(os.environ["DISCORD_TOKEN"])

if __name__ == "__main__":
    main()
