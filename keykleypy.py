import configparser
from os.path import abspath as wd
import keyboard
from pixpile import *
import asyncio

async def drawButton(keyName='', posX=0, posY=0, style={}, spanXForced=1):
    spanX = int(style['spanX'])
    spanY = int(style['spanY'])

    colorText = style['colorText']
    colorFg = style['colorFg'] if not keyboard.is_pressed(keyName) else style['colorFgPressed']
    colorBg = style['colorBg']

    symbolFg = style['symbolFg']
    symbolBg = style['symbolBg']
    
    print(drawRectangle(symbolBg, colorBg, 0, 0+posX+(spanX*posX), 0+posY+(spanY*posY), (spanX if spanXForced==1 else spanX*spanXForced+spanXForced-1), spanY))
    print(drawRectangle(symbolFg, colorFg, 0, 1+posX+(spanX*posX), 1+posY+(spanY*posY), (spanX-2 if spanXForced==1 else spanX*spanXForced-3+spanXForced), spanY-2))
    print(f"{moveCursor(3+posX+(spanX*posX), 3+posY+(spanY*posY))}{colorIt(keyName, colorText, colorFg)}")

async def main():
    config = configparser.ConfigParser()
    config.read(f'{wd("")}/kleypy_config.ini')
    style = config['style']
    print(CLR, end='')
    while True:
        tasks = [
            asyncio.create_task(drawButton('1'   , 0, 0, style)), asyncio.create_task(drawButton('2'    , 1, 0, style)), asyncio.create_task(drawButton('3'    , 2, 0, style)), asyncio.create_task(drawButton('4', 3, 0, style)), asyncio.create_task(drawButton('5', 4, 0, style)),
            asyncio.create_task(drawButton('q'   , 0, 1, style)), asyncio.create_task(drawButton('w'    , 1, 1, style)), asyncio.create_task(drawButton('e'    , 2, 1, style)), asyncio.create_task(drawButton('r', 3, 1, style)),
            asyncio.create_task(drawButton('a'   , 0, 2, style)), asyncio.create_task(drawButton('s'    , 1, 2, style)), asyncio.create_task(drawButton('d'    , 2, 2, style)), asyncio.create_task(drawButton('f', 3, 2, style)), asyncio.create_task(drawButton('g', 4, 2, style)),
            asyncio.create_task(drawButton('ctrl', 0, 3, style)), asyncio.create_task(drawButton('shift', 1, 3, style)), asyncio.create_task(drawButton('space', 2, 3, style, spanXForced=3))
        ]
        await tasks[0]

if __name__ == "__main__":
    asyncio.run(main())
