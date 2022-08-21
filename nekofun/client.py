from nekofun.http import NekoFunRequest
from nekofun.model import ResultNeko, RandomNeko
import sys
from nekofun import utils
import random

class Get(NekoFunRequest):
  """
  `NekoFunRequest`를 감싸는 비동기 클라이언트 클래스입니다.
  """
  def __init__(self):
    pass

  async def kiss(self) -> ResultNeko:
    """Kissing images"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def lick(self) -> ResultNeko:
    """Lick"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def hug(self) -> ResultNeko:
    """안아줘요"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def baka(self) -> ResultNeko:
    """바...바보!!"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def poke(self) -> ResultNeko:
    """푹푹푹푹"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def cry(self) -> ResultNeko:
    """울지마, 넌 머지않아 예쁜 꽃이 될 테니까"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def smug(self) -> ResultNeko:
    """What to put here?"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def slap(self) -> ResultNeko:
    """아야!!"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def tickle(self) -> ResultNeko:
    """간질간질"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def pat(self) -> ResultNeko:
    """쓰담쓰담"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def laugh(self) -> ResultNeko:
    """웃자"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def feed(self) -> ResultNeko:
    """배고파요"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def cuddle(self) -> ResultNeko:
    """안아줘ㅇ...아니 이거 맞나"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)


  #NSFW
  async def _4k(self) -> ResultNeko:
    """NSFW : 실사"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def blowjob(self) -> ResultNeko:
    """NSFW : 펠라"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def boobs(self) -> ResultNeko:
    """NSFW : 가슴"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)
    
  async def cum(self) -> ResultNeko:
    """NSFW : 질내사정"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)
    
  async def feet(self) -> ResultNeko:
    """NSFW : 발"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def hentai(self) -> ResultNeko:
    """NSFW : 랜덤 hentai"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def wallpapers(self) -> ResultNeko:
    """99% SFW(건전)"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def spank(self) -> ResultNeko:
    """NSFW : 찰싹찰싹"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def gasm(self) -> ResultNeko:
    """NSFW : 아헤가오"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def lesbian(self) -> ResultNeko:
    """NSFW : 레즈비언"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def lewd(self) -> ResultNeko:
    """NSFW : **WARNING** 적은 확률로 로리/쇼타가 나올수 있음"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  async def pussy(self) -> ResultNeko:
    """NSFW : 우리집에 고양이 보러 올래?"""
    result = await self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)


  # ETC
  async def random(self) -> RandomNeko:
    """SFW, NSFW 포함"""
    tag = random.choice(utils.all_tag)
    result = await self.request(tag)
    result['tag'] = tag
    return RandomNeko(data = result)

  async def random_sfw(self) -> RandomNeko:
    """랜덤 SFW"""
    tag = random.choice(utils.sfw_tag)
    result = await self.request(tag)
    result['tag'] = tag
    return RandomNeko(data = result)

  async def random_nsfw(self) -> RandomNeko:
    """랜덤 NSFW"""
    tag = random.choice(utils.nsfw_tag)
    result = await self.request(tag)
    result['tag'] = tag
    return RandomNeko(data = result)    
