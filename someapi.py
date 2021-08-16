import aiohttp
import asyncio
from outdated import warn_if_outdated

warn_if_outdated('someapi_wrapper', '0.4')
class Images:
    def __init__(self):
        pass
    async def dog():
        return "https://someapi.xyz/image/dog"

class Json:
    def __init__(self):
        pass
    async def dog():
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://someapi.xyz/json/dogs") as r:
            
                data = await r.json()
       
        return data["fact"]
    async def quote(amogus=None):
        try:
            if amogus==None:
                amogus=="amogus cool"

            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://someapi.xyz/json/quote") as r:
                
                    data = await r.json()
            if amogus=="author":
                return data["author"]
                
            else:
                return data["quote"]
        except:
            return "Website may be down or you used the function wrongly"
                
    async def mocktext(text):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://someapi.xyz/mocktext?text={text}") as r:
            
                data = await r.json()
        return data["text"]
    async def chatbot(text,apikey):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://someapi.xyz/premuim/chatbot?code={apikey}&text={text}") as r:
            
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
