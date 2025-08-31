#!/usr/bin/python3
import asyncio
import json
import websockets
import mss
import base64
import pyautogui
os.environ['DISPLAY'] = ':0'
async def handler(websocket):
	while True:
		try:
			# Listen for commands from the client
			message = await websocket.recv()
			command = json.loads(message)

			if command['type'] == 'control':
				if command['action'] == 'move_mouse':
					pyautogui.moveTo(command['x'], command['y'])
				elif command['action'] == 'click':
					pyautogui.click()
				elif command['action'] == 'type':
					pyautogui.write(command['text'])
			elif command['type'] == 'request_screen':
				with mss.mss() as sct:
					monitor = sct.monitors[1]
					sct_img = sct.grab(monitor)
					bytes_img = mss.tools.to_png(sct_img.rgb, sct_img.size)
					encoded_img = base64.b64encode(bytes_img).decode('utf-8')
					await websocket.send(json.dumps({'type': 'screen', 'image': encoded_img}))
		except websockets.exceptions.ConnectionClosed:
			break

async def main():
	async with websockets.serve(handler, "localhost", 8765):
		await asyncio.Future()  # run forever

if __name__ == "__main__":
	asyncio.run(main())

# pip3 install mss pyautogui websockets
# sudo apt install python3-mss -y
# sudo apt install python3-pyautogui -y
# sudo apt install python3-websockets -y