import aiohttp
from typing import Dict
from nekofun import utils
from nekofun.error import HTTPException

class NekoFunRequest:
  def __init__(self) -> None:
    pass

  async def request(self, tag : str) -> Dict[str, str]:
    URL = utils.BASE + tag
    async with aiohttp.ClientSession() as session:
      async with session.get(URL) as response:
        rescode = response.status
        if(rescode==200):
          result = await response.json()
          result['data'] = result.pop('image')
          return result
        else:
          raise HTTPException(f"Error Code : {rescode}")
