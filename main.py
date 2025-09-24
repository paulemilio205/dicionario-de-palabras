import discord
from discord.ext import commands
import random

frases = [
    "💡 Nunca es tarde para empezar de nuevo.",
    "🔥 Si puedes soñarlo, puedes lograrlo.",
    "🚀 El éxito es la suma de pequeños esfuerzos repetidos cada día.",
    "🌟 Cree en ti, incluso cuando nadie más lo haga.",
    "💪 Las grandes cosas toman tiempo, sé paciente.",
    "🌈 Cada día es una nueva oportunidad."
]

datos = [
    "Los pulpos tienen tres corazones.",
    "La miel nunca caduca, se han encontrado tarros de miel de miles de años en buen estado.",
    "Las vacas tienen mejores amigas y se estresan cuando se separan.",
    "Un día en Venus dura más que un año en Venus.",
    "Los flamencos nacen grises, se vuelven rosados por su alimentación.",
    "Los tiburones existen desde antes que los árboles."
]

chistes = [
    "¿Por qué el libro de matemáticas se deprimió? Porque tenía demasiados problemas.",
    "¿Qué le dice una impresora a otra? —¿Esa hoja es tuya o es una impresión mía?",
    "¿Cómo se dice pañuelo en japonés? Saka-moko.",
    "¿Por qué la computadora fue al médico? ¡Porque tenía un virus!",
    "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!",
    "Oye ¿tú estudias derecho? No, yo estudio sentado."
]


def flip_coin():
    flip = random.randint(0, 2)
    if flip == 0:
        return "cara"
    else:
        return "cruz"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def cara_o_cruz(ctx):
    await ctx.send(flip_coin())

@bot.command()
async def adios(ctx):
    await ctx.send("Adios que te valla bien",)

@bot.command()
async def chiste(ctx):
    await ctx.send(random.choice(chistes))

@bot.command()
async def dato(ctx):
    await ctx.send(random.choice(datos))

    
@bot.command()
async def frase(ctx):
    await ctx.send(random.choice(frases))




bot.run("your bot here")
