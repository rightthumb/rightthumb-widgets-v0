#!/usr/bin/python3
import asyncio
import tkinter as tk
from PIL import Image, ImageTk
import websockets
import json
import base64
import io

class RemoteDesktopClient:
	def __init__(self, root):
		self.root = root
		self.root.title("Remote Desktop")
		self.canvas = tk.Canvas(root, width=800, height=600)
		self.canvas.pack()

		# Event bindings
		self.canvas.bind("<Motion>", self.mouse_move)
		self.canvas.bind("<Button-1>", self.mouse_click)
		self.root.bind("<Key>", self.key_press)

		# WebSocket connection
		self.websocket = None

	async def connect(self, uri):
		async with websockets.connect(uri) as websocket:
			self.websocket = websocket
			await self.request_screen()
			await self.receive()

	async def request_screen(self):
		if self.websocket:
			await self.websocket.send(json.dumps({'type': 'request_screen'}))

	async def receive(self):
		while True:
			response = await self.websocket.recv()
			data = json.loads(response)
			if data['type'] == 'screen':
				self.update_screen(data['image'])

	def update_screen(self, image_data):
		image_bytes = base64.b64decode(image_data)
		image = Image.open(io.BytesIO(image_bytes))
		photo = ImageTk.PhotoImage(image)
		
		self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
		self.canvas.image = photo  # Keep a reference!

	def mouse_move(self, event):
		print(f"Mouse moved to {event.x}, {event.y}")

	def mouse_click(self, event):
		print("Mouse clicked")

	def key_press(self, event):
		print(f"Key pressed: {event.char}")

def main():
	root = tk.Tk()
	client = RemoteDesktopClient(root)

	async def run_client():
		await client.connect("ws://localhost:8765")
		root.mainloop()

	asyncio.run(run_client())

if __name__ == "__main__":
	main()

# pip3 install websockets Pillow
