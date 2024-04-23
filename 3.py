import asyncio
import websockets
import json

class WebSocketAdapter:
    def __init__(self, uri):
        self.uri = uri
        self.websocket = None
    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.uri)
            await self.on_connect()
            await self.receive_messages()
        except Exception as e:
            await self.on_error(e)
    async def disconnect(self):
        await self.websocket.close()
    async def send_message(self, message):
        await self.websocket.send(json.dumps(message))
    async def receive_messages(self):
        while True:
            try:
                message = await self.websocket.recv()
                await self.on_message((message))
                print(f"Client received message {message}")
                # await self.send_message("Message from client")
            except websockets.exceptions.ConnectionClosed:
                await self.on_close()
                break
            except Exception as e:
                await self.on_error(e)
    async def on_connect(self):
        print("Connected to WebSocket server.")
    async def on_message(self, message):
        print("Received message from server:", message)
    async def on_error(self, error):
        print("WebSocket error:", error)
    async def on_close(self):
        print("WebSocket connection closed.")
# # Example usage:
# async def main():
#     uri = "ws://localhost:8765/conversations/1"
#     websocket_adapter = WebSocketAdapter(uri)
#     await websocket_adapter.connect()

# # Run the event loop
# asyncio.get_event_loop().run_until_complete(main())

async def main(url):
    websocket_adapter = WebSocketAdapter(url)
    await websocket_adapter.connect()
    # await websocket_adapter.send_message("Message from client")
    print("======================================")

async def test():
    urls = [
        "ws://localhost:8765/conversations/1",
        "ws://localhost:8765/conversations/2",
        "ws://localhost:8765/conversations/3",
        "ws://localhost:8765/conversations/4",
        "ws://localhost:8765/conversations/5",
        "ws://localhost:8765/conversations/6",
        "ws://localhost:8765/conversations/7",
        "ws://localhost:8765/conversations/8",
        "ws://localhost:8765/conversations/9",
        "ws://localhost:8765/conversations/10",
        "ws://localhost:8765/conversations/11",
        "ws://localhost:8765/conversations/12",
        "ws://localhost:8765/conversations/13",
        "ws://localhost:8765/conversations/14",
        "ws://localhost:8765/conversations/15",
        "ws://localhost:8765/conversations/16",
        "ws://localhost:8765/conversations/17",
        "ws://localhost:8765/conversations/18",
        "ws://localhost:8765/conversations/19",
        "ws://localhost:8765/conversations/20",
    ]
    tasks = [main(url) for url in urls]
    await asyncio.gather(*tasks)
# Run the event loop
asyncio.get_event_loop().run_until_complete(test())