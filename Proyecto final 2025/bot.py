import discord
import asyncio
import time
from discord.ext import commands
from main import clasificador

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)


@bot.event
async def on_ready():
    print(f'Se inició {bot.user}')

@bot.command()
async def subir_imagen(ctx):
    if len(ctx.message.attachments) == 0:
        await ctx.send("No se ha encontrado ninguna imagen adjunta.")
    else:
        # Iterar sobre los archivos adjuntos
        for attachment in ctx.message.attachments:
            if attachment.filename.endswith(('jpg', 'jpeg', 'png')):
                # Guardar la imagen en el sistema de archivos local
                filepath = f"images/{attachment.filename}"
                await attachment.save(filepath)

                # Enviar la URL de la imagen de vuelta al usuario
                await ctx.send(clasificador(f"images/{attachment.filename}"))
                await ctx.send(f"Imagen {attachment.filename} guardada con éxito. Disponible en: {attachment.url}")
            else:
                await ctx.send(f"El archivo {attachment.filename} no es una imagen válida.")
    

@bot.command()
async def co2(ctx):
    await ctx.send(f'Las emisiones de dióxido de carbono (CO2) son gases liberados principalmente por actividades humanas como la quema de combustibles fósiles (carbón, petróleo, gas (para generar electricidad, o fábricas)) y la deforestación, ¡y es por esto que fui creado!, para tomar conciencia de las emisiones de co2 y cambio climatico y aplicar soluciones en nuestro entorno y vida cotidiana.')
    await ctx.send(f'Estas emisiones contribuyen al calentamiento global, atrapando el calor en la atmósfera y causando cambios climáticos. Los efectos son: Afectan nuestro entorno aumentando las temperaturas globales. Fenómenos climáticos extremos, y elevación del nivel del mar. Además, impactan la biodiversidad, la agricultura y la salud humana debido a olas de calor, sequías, y peor calidad del aire. ¡Es por esto que debes aplicar mis consejos en tu espacio de trabajo!')
    time.sleep(2)
    await ctx.send(f'Los principales electrodomesticos que mas emiten dioxido de carbono son: Refrigeradores y congeladores. Cocinas eléctricas o de gas. Computadoras (aunque no contribuyen directamente a las emisiones de co2, contribuyen indirectamente dependiendo si la energia viene de fuentes no renovables).')
    await ctx.send(f'¡Empecemos a analizar tu espacio con <$subir_imagen>!')


@bot.command()
async def hola(ctx):
    await ctx.send(f'Hola, {ctx.author}. Mi nombre es {bot.user}, sere tu encargado de analizar tu espacio de trabajo y como reducir las emisiones de dioxido de carbono y ahorrar energía electrica. Podemos empezar a analizar tu espacio de trabajo con el comando <$subir_imagen> y una imagen adjunta en el mensaje. ¡Conoce más sobre las emisiones de dioxido de carbono con el comando <$co2>!')
    time.sleep(2)
    await ctx.send(f'Este bot esta siendo desarrollado y no puede presentar exactitud, a parte de estar incompleta puesto que se espera añadir más funciones y variedad. Gracias por su comprensión {ctx.author}.')



bot.run("discord token")

