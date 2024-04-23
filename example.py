import asyncio
import websockets

async def connect_to_websocket(uri):
    async with websockets.connect(uri) as websocket:
        # while True:
            await websocket.send(uri)
            message = await websocket.recv()
            print(f"Receieved message : {message}")


            
async def main():
    websocket_uris = [
        "ws://localhost:8765/1",
        "ws://localhost:8765/2",
    ]
    tasks = [connect_to_websocket(uri) for uri in websocket_uris]
    await asyncio.gather(*tasks)
    
asyncio.run(main())

    