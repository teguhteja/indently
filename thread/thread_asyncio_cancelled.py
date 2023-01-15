# SuperFastPython.com
# example of canceling a task and checking its done status
import asyncio
 
# define a coroutine for a task
async def task_coroutine():
    # report a message
    print('executing the task')
    # block for a moment
    await asyncio.sleep(1)
 
# custom coroutine
async def main():
    # create and schedule the task
    task = asyncio.create_task(task_coroutine())
    # check if it is done
    print(f'>task done: {task.done()}')
    # wait a moment
    await asyncio.sleep(0.1)
    # check if it is done
    print(f'>task done: {task.done()}')
    # cancel the task
    task.cancel()
    # wait a moment more
    await asyncio.sleep(0.1)
    # check if it is done
    print(f'>task done: {task.done()}')
 
# start the asyncio program
asyncio.run(main())