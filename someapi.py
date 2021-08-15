import aiohttp
import asyncio
class Images:
    def __init__(self):
        pass
    async def dog():
        return "https://someapi.xyz/dog/image"

class Json:
    def __init__(self):
        pass
    async def dog():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://someapi.xyz/json/dogs") as r:
            
                data = await r.json()
       
        return data["fact"]
    async def quote(amogus=None):
        if amogus==None:
            amogus=="amogus cool"

        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://someapi.xyz/json/quote") as r:
            
                data = await r.json()
        if amogus=="author":
            return data["author"]
            
        else:
            return data["quote"]
            
    async def mocktext(text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://someapi.xyz/mocktext?text={text}") as r:
            
                data = await r.json()
        return data["text"]
class Canvas:
    def __init__(self):
        pass
    async def invert(avatar):
        return f"https://someapi.xyz/invert?avatar={avatar}"

    async def greyscale(avatar):
        return f"https://someapi.xyz/greyscale?avatar={avatar}"

    async def wanted(avatar):
        return f"https://someapi.xyz/wanted?avatar={avatar}"

    async def alert(text):
        return f"https://someapi.xyz/alert?text={text}"

    async def god_temp(text):
        return f"https://someapi.xyz/god_temp?text={text}"

    async def biden(text):
        return f"https://someapi.xyz/biden?text={text}"
        
    async def gay(avatar):
        return f"https://someapi.xyz/rainbow?avatar={avatar}"

    async def billy(text):
        return f"https://someapi.xyz/billy?text={text}"

    async def pacman(text):
        return f"https://someapi.xyz/pacman/text?text={text}"

    async def hitler(avatar):
        return f"https://someapi.xyz/hitler?avatar={avatar}"



