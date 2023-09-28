#!/usr/bin/env python

# WS server that sends messages every second

import asyncio
import datetime

import websockets


async def time(websocket, path):
    while True:
        await websocket.send(str(datetime.datetime.now()))
        await asyncio.sleep(1)


async def main():
    start_server = websockets.serve(time, "127.0.0.1", "9000")
    print("Running server on 127.0.0.1:9000")
    await start_server


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    server_task = loop.create_task(main())
    loop.run_until_complete(asyncio.gather(server_task, return_exceptions=True))
    loop.run_forever()

    # try:
    #     loop.run_until_complete(asyncio.gather(server_task, return_exceptions=True))
    #     loop.run_forever()
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     # Close the WebSocket server and the event loop gracefully on exit
    #     server_task.cancel()
    #     loop.run_until_complete(asyncio.gather(server_task, return_exceptions=True))
    #     loop.close()
