from nekofun.model import ResultNeko, RandomNeko
import sys
from nekofun import utils
import random
import requests
from typing import Dict
from nekofun.error import HTTPException

class Get:
  """
  동기 클라이언트 클래스입니다.
  """
  def __init__(self):
    pass

  def request(self, tag : str) -> Dict[str, str]:
    URL = utils.BASE + tag
    response = requests.get(URL)
    rescode = response.status_code
    if(rescode == 200):
      result = response.json()
      result['data'] = result.pop('image')
      return result
    else:
      raise HTTPException(f"Error Code : {rescode}")
    
  def kiss(self) -> ResultNeko:
    """Kissing images"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def lick(self) -> ResultNeko:
    """Lick"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def hug(self) -> ResultNeko:
    """안아줘요"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def baka(self) -> ResultNeko:
    """바...바보!!"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def poke(self) -> ResultNeko:
    """푹푹푹푹"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def cry(self) -> ResultNeko:
    """울지마, 넌 머지않아 예쁜 꽃이 될 테니까"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def smug(self) -> ResultNeko:
    """What to put here?"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def slap(self) -> ResultNeko:
    """아야!!"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def tickle(self) -> ResultNeko:
    """간질간질"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def pat(self) -> ResultNeko:
    """쓰담쓰담"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def laugh(self) -> ResultNeko:
    """웃자"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def feed(self) -> ResultNeko:
    """배고파요"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def cuddle(self) -> ResultNeko:
    """안아줘ㅇ...아니 이거 맞나"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)


  #NSFW
  def _4k(self) -> ResultNeko:
    """NSFW : 실사"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def blowjob(self) -> ResultNeko:
    """NSFW : 펠라"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def boobs(self) -> ResultNeko:
    """NSFW : 가슴"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)
    
  def cum(self) -> ResultNeko:
    """NSFW : 질내사정"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)
    
  def feet(self) -> ResultNeko:
    """NSFW : 발"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def hentai(self) -> ResultNeko:
    """NSFW : 랜덤 hentai"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def wallpapers(self) -> ResultNeko:
    """99% SFW(건전)"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def spank(self) -> ResultNeko:
    """NSFW : 찰싹찰싹"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def gasm(self) -> ResultNeko:
    """NSFW : 아헤가오"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def lesbian(self) -> ResultNeko:
    """NSFW : 레즈비언"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def lewd(self) -> ResultNeko:
    """NSFW : **WARNING** 적은 확률로 로리/쇼타가 나올수 있음"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)

  def pussy(self) -> ResultNeko:
    """NSFW : 우리집에 고양이 보러 올래?"""
    result = self.request(tag = str(sys._getframe().f_code.co_name))
    return ResultNeko(data = result)


  # ETC
  def random(self) -> RandomNeko:
    """SFW, NSFW 포함"""
    tag = random.choice(utils.all_tag)
    result = self.request(tag)
    result['tag'] = tag
    return RandomNeko(data = result)

  def random_sfw(self) -> RandomNeko:
    """랜덤 SFW"""
    tag = random.choice(utils.sfw_tag)
    result = self.request(tag)
    result['tag'] = tag
    return RandomNeko(data = result)

  def random_nsfw(self) -> RandomNeko:
    """랜덤 NSFW"""
    tag = random.choice(utils.nsfw_tag)
    result = self.request(tag)
    result['tag'] = tag
    return RandomNeko(data = result)    
