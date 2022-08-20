# Nekofun
일러스트 크롤링 라이브러리(동기, 비동기 지원)
## How to use
### Install
```
pip install nekofun
```

### Example
#### [async]
```py
from nekofun import client
import asyncio

async def main():
  # 클래스를 정의해줍니다.
  get = client.Get()
  result = await get.cry() # 우는 그림(or gif)를 가져옵니다.
  result = result.content # 링크형태로 반환합니다.
  print(result)
  
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
```
#### [sync]
```py
from nekofun import sync

sync = sync.Get() # 클래스를 정의해줍니다.
result = sync.cry() # 우는 그림(or gif)를 가져옵니다.
print(result.content) # 링크형태로 반환하여 출력합니다.
```
