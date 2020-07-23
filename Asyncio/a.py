# import time

# def hello():
#     time.sleep(1)

# def run():
#     for i in range(5):
#         hello()
#         print('Hello World:%s' % time.time())  # 任何伟大的代码都是从Hello World 开始的！

# if __name__ == '__main__':
#     run()

import time
import asyncio


async def hello():
    asyncio.sleep(1)
    print('Hello World:%s' % time.time())


def run():
    for i in range(6):
        loop.run_until_complete(hello())


if __name__ == '__main__':
    loop = asyncio.get_running_loop()
    run()