异步
asyncio. 这是一个仅仅使用单线程, 就能达到多线程/进程的效果的工具

官网介绍：https://docs.python.org/3/library/asyncio.html

Asyncio 库是 Python 的原装库, 但是是在 Python 3 的时候提出来的, Python 2 和 Python 3.3- 是没有的. 
而且 Python 3.5 之后, 和 Python 3.4 前在语法上还是有些不同, 比如 “await” 和 “yield” 的使用, 
在 3.5+ 版本中, asyncio 有两样语法非常重要, async, await. 弄懂了它们是如何协同工作的, 我们就完全能发挥出这个库的功能了

#普通方式
import time
def job(t):
    print('Start job ', t)
    time.sleep(t)               # wait for "t" seconds
    print('Job ', t, ' takes ', t, ' s')
    
def main():
    [job(t) for t in range(1, 3)]
      
t1 = time.time()
main()
print("NO async total time : ", time.time() - t1)


#异步方式
import asyncio
async def job(t):
    print('Start job ', t)
    await asyncio.sleep(t)          # wait for "t" seconds, it will look for another job while await
    print('Job ', t, ' takes ', t, ' s')
    
async def main(loop):
    tasks = [loop.create_task(job(t)) for t in range(1, 3)]     # just create, not run job
    await asyncio.wait(tasks)                                   # run jobs and wait for all tasks done

t1 = time.time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
# loop.close()                          # Ipython notebook gives error if close loop
print("Async total time : ", time.time() - t1)


