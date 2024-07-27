import tkinter as tk
from tkinter import ttk, messagebox
import getpass
import platform
import psutil
from datetime import datetime
import os
import json
import subprocess
import http.server
from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import webbrowser
from urllib.parse import parse_qs, urlparse
import threading
from socketserver import ThreadingMixIn
import random
import sys
from cgi import parse_header, parse_multipart

import _rightThumb._construct as __

__.form_data = {}
shutdown_event = threading.Event()

class Server(SimpleHTTPRequestHandler):
	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		html_content = self.generate_html_form()
		self.wfile.write(html_content.encode('utf-8'))

	def generate_html_form(self):
		form_html = "<html><body><h1>Dynamic Form</h1><form method='post'>"
		for section, fields in self.server.form_structure.items():
			if section == "Config":
				continue
			form_html += f"<h2>{section}</h2>"
			for field in fields:
				label = field.get("label")
				field_type = field.get("type")
				options = field.get("options", [])
				value = field.get("value", "")
				field_config = field.get("config", {})
				width = field_config.get("width", self.server.form_structure.get("Config", {}).get("field", {}).get("width", 20))

				form_html += f"<label>{label}</label><br>"
				if field_type == "text":
					form_html += f"<input type='text' name='{label}' value='{value}' size='{width}'><br>"
				elif field_type == "password":
					form_html += f"<input type='password' name='{label}' value='{value}' size='{width}'><br>"
				elif field_type == "text_area":
					form_html += f"<textarea name='{label}' rows='5' cols='{width}'>{value}</textarea><br>"
				elif field_type == "radio":
					for option in options:
						checked = 'checked' if option == value else ''
						form_html += f"<input type='radio' name='{label}' value='{option}' {checked}>{option}<br>"
				elif field_type == "dropdown":
					form_html += f"<select name='{label}'>"
					for option in options:
						selected = 'selected' if option == value else ''
						form_html += f"<option value='{option}' {selected}>{option}</option>"
					form_html += "</select><br>"

			form_html += "<br>"
		form_html += "<input type='submit' value='Submit'></form></body></html>"
		return form_html

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length).decode('utf-8')
		form_data = parse_qs(post_data)
		form_data = {k: v[0] for k, v in form_data.items()}
		self.server.form_data = form_data  # Update the server's form_data
		self._set_headers()
		self.wfile.write(json.dumps(form_data, indent=4).encode('utf-8'))
		__.form_data = form_data
		# print("Form Submitted: ", json.dumps(form_data, indent=4))
		# self.server_close()
		shutdown_event.set()
		threading.Thread(target=self.server.shutdown).start()

		
		# sys.exit()

class FormManager:
	def __init__(self, form_structure):
		self.form_structure = form_structure
		self.form_data = {}
		self.config = self.form_structure.get("Config", {})
		self.use_tkinter = self.detect_gui()
		if self.use_tkinter:
			if self.config.get("html", False):
				self.start_webserver()
				self.form_data = __.form_data
			else:
				self.create_tkinter_form()
		else:
			self.create_terminal_form()

	def detect_gui(self):
		try:
			root = tk.Tk()
			root.withdraw()
			root.update()
			root.destroy()
			return True
		except:
			return False

	def apply_style(self, widget, field_config=None):
		style = ttk.Style()
		style_name = "Custom.TLabel"

		config = self.form_structure.get("Config", {})
		field_config = field_config or {}

		font_config = field_config.get("font", config.get("font", {}))
		color_config = field_config.get("color", config.get("color", {}))

		font_type = font_config.get("type", "Arial")
		font_size = font_config.get("size", 12)
		style.configure(style_name, font=(font_type, font_size))

		if "text" in color_config:
			style.configure(style_name, foreground=color_config["text"])
		if "bg" in color_config:
			style.configure(style_name, background=color_config["bg"])

		return style_name

	def create_tkinter_form(self):
		self.root = tk.Tk()
		self.root.title("Dynamic Form")
		self.root.geometry("800x800")

		row = 0
		for section, fields in self.form_structure.items():
			if section == "Config":
				continue
			ttk.Label(self.root, text=section, font=("Arial", 14, "bold")).grid(row=row, column=0, columnspan=2, pady=10)
			row += 1
			for field in fields:
				self.create_tkinter_field(field, row)
				row += 1
		ttk.Button(self.root, text="Submit", command=self.submit_tkinter_form).grid(row=row+len(fields), column=0, columnspan=2, pady=20)
		self.root.mainloop()

	def create_tkinter_field(self, field, row):
		label = field.get("label")
		field_type = field.get("type")
		options = field.get("options", [])
		value = field.get("value", "")
		col_span = field.get("col_span", 2)
		field_config = field.get("config", {})
		width = field_config.get("width", self.config.get("field", {}).get("width", 20))
		var = None

		style_name = self.apply_style(None, field_config)
		
		if field_type == "text":
			var = tk.StringVar(value=value)
			label_widget = ttk.Label(self.root, text=label, style=style_name)
			label_widget.grid(row=row, column=0, sticky=tk.E)
			entry_widget = ttk.Entry(self.root, textvariable=var, width=width)
			entry_widget.grid(row=row, column=1, columnspan=col_span, pady=5, padx=10)
		elif field_type == "password":
			var = tk.StringVar(value=value)
			label_widget = ttk.Label(self.root, text=label, style=style_name)
			label_widget.grid(row=row, column=0, sticky=tk.E)
			entry_widget = ttk.Entry(self.root, textvariable=var, show='*', width=width)
			entry_widget.grid(row=row, column=1, columnspan=col_span, pady=5, padx=10)
		elif field_type == "text_area":
			var = tk.Text(self.root, height=5, width=width, wrap="word", font=("Arial", 12))
			label_widget = ttk.Label(self.root, text=label, style=style_name)
			label_widget.grid(row=row, column=0, sticky=tk.NE)
			var.grid(row=row, column=1, columnspan=col_span, pady=5, padx=10)
			var.insert("1.0", value)
		elif field_type == "radio":
			var = tk.StringVar(value=value)
			label_widget = ttk.Label(self.root, text=label, style=style_name)
			label_widget.grid(row=row, column=0, sticky=tk.E)
			for option in options:
				rb_widget = ttk.Radiobutton(self.root, text=option, variable=var, value=option)
				rb_widget.grid(row=row, column=1, sticky=tk.W)
				row += 1
		elif field_type == "dropdown":
			var = tk.StringVar(value=value)
			label_widget = ttk.Label(self.root, text=label, style=style_name)
			label_widget.grid(row=row, column=0, sticky=tk.E)
			combobox_widget = ttk.Combobox(self.root, textvariable=var, values=options, width=width)
			combobox_widget.grid(row=row, column=1, columnspan=col_span, pady=5, padx=10)
		
		self.form_data[label] = var

	def submit_tkinter_form(self):
		data = {}
		for label, var in self.form_data.items():
			if isinstance(var, tk.Text):
				data[label] = var.get("1.0", tk.END).strip()
			else:
				data[label] = var.get()
		# print(json.dumps(data, indent=4))
		self.form_data = data  # Update form_data with submitted data
		self.root.destroy()

	def create_terminal_form(self):
		for section, fields in self.form_structure.items():
			if section == "Config":
				continue
			print(f"\n{section}")
			for field in fields:
				self.create_terminal_field(field)
		# print(json.dumps(self.form_data, indent=4))

	def create_terminal_field(self, field):
		label = field.get("label")
		field_type = field.get("type")
		options = field.get("options", [])
		value = field.get("value", "")

		if field_type == "text":
			self.form_data[label] = input(f"{label} [{value}]: ") or value
		elif field_type == "password":
			self.form_data[label] = getpass.getpass(f"{label}: ")
		elif field_type == "text_area":
			print(f"{label} [{value}]: (press Enter twice to finish)")
			lines = []
			while True:
				line = input()
				if line:
					lines.append(line)
				else:
					break
			self.form_data[label] = "\n".join(lines) or value
		elif field_type == "radio":
			print(f"{label}:")
			for i, option in enumerate(options, 1):
				print(f"  {i}. {option}")
			choice = int(input("Choose an option: ")) - 1
			self.form_data[label] = options[choice]
		elif field_type == "dropdown":
			print(f"{label}:")
			for i, option in enumerate(options, 1):
				print(f"  {i}. {option}")
			choice = int(input("Choose an option: ")) - 1
			self.form_data[label] = options[choice]

	def record(self):
		return self.form_data

	def start_webserver(self):
		host = "localhost"
		port = random.randint(8000, 8999)
		server_address = (host, port)
		httpd = HTTPServer(server_address, Server)
		httpd.form_structure = self.form_structure  # Attach form structure to the server

		print(f"Serving at http://{host}:{port}")
		webbrowser.open(f'http://{host}:{port}')
		
		try:
			httpd.serve_forever()
		except KeyboardInterrupt:
			pass
		
		httpd.server_close()
		print("Server stopped.")

# Function to get drive information
def get_drive_info():
	def get_drive_serial(drive_letter):
		import subprocess
		import re
		result = subprocess.run(['vol', drive_letter], stdout=subprocess.PIPE, text=True, shell=True)
		match = re.search(r"Volume Serial Number is ([\w-]+)", result.stdout)
		if match:
			return match.group(1)
		else:
			return None

	def get_drive_model(drive_letter):
		import wmi
		c = wmi.WMI()
		logical_disk = c.Win32_LogicalDisk(DeviceID=drive_letter)[0]
		partition = c.query(f"ASSOCIATORS OF {{Win32_LogicalDisk.DeviceID='{drive_letter}'}} WHERE AssocClass=Win32_LogicalDiskToPartition")[0]
		disk_drive = c.query(f"ASSOCIATORS OF {{Win32_DiskPartition.DeviceID='{partition.DeviceID}'}} WHERE AssocClass=Win32_DiskDriveToDiskPartition")[0]
		return disk_drive.Model

	import socket
	import time
	if platform.system() == "Windows":
		import win32api
	cwd = os.getcwd()
	if platform.system() == "Windows":
		drive = os.path.splitdrive(cwd)[0]
	else:
		drive = os.path.realpath(cwd).split('/')[1]
		drive = '/' + drive

	drive_info = psutil.disk_usage(drive)
	capacity = drive_info.total
	used = drive_info.used
	free = drive_info.free
	model = "N/A"
	serial = "N/A"
	if platform.system() == "Windows":
		model = get_drive_model(drive)
		serial = get_drive_serial(drive)
	else:
		try:
			result = subprocess.run(['lsblk', '-o', 'NAME,SERIAL,MODEL'], stdout=subprocess.PIPE, text=True)
			output = result.stdout.strip().split('\n')
			for line in output[1:]:
				parts = line.split()
				if drive in parts[0]:
					serial = parts[1]
					model = parts[2] if len(parts) > 2 else "N/A"
					break
		except Exception as e:
			serial = "N/A"
			model = "N/A"
	
	pc_name = socket.gethostname()
	epoch_time = int(time.time())
	info = {
		"model": model,
		"serial": serial,
		"capacity": capacity,
		"used": used,
		"free": free,
		"drive_letter_or_mount_info": drive,
		"epoch": epoch_time,
		"pc": pc_name
	}
	return info

if __name__ == "__main__":
	drive_info = get_drive_info()
	form_structure = {
		"Config": {
			# "html": True,
			"column": {"width": 2},
			"font": {"type": "Arial", "size": 12},
			"color": {"text": "black", "bg": "white"},
			"field": {"width": 40}
		},
		"Drive Information": [
			{"label": "Model", "type": "text", "value": drive_info.get("model", "")},
			{"label": "Serial", "type": "text", "value": drive_info.get("serial", "")},
			{"label": "Capacity", "type": "text", "value": drive_info.get("capacity", "")},
			{"label": "Used", "type": "text", "value": drive_info.get("used", "")},
			{"label": "Free", "type": "text", "value": drive_info.get("free", "")},
			{"label": "Drive Letter or Mount Info", "type": "text", "value": drive_info.get("drive_letter_or_mount_info", "")},
			{"label": "Epoch", "type": "text", "value": drive_info.get("epoch", "")},
			{"label": "PC", "type": "text", "value": drive_info.get("pc", "")}
		],
		"User Input": [
			{"label": "Label", "type": "text", "value": ""},
			{"label": "Priority", "type": "text", "value": "", "config": {"width": 20}},
			{"label": "Owner", "type": "text", "value": ""},
			{"label": "Notes", "type": "text_area", "value": "", "config": {"width": 60}},
			{"label": "Descriptors", "type": "text_area", "value": ""},
			{"label": "Drive Type", "type": "radio", "options": ["internal", "external", "thumb", "button", "network"], "value": ""}
		]
	}
	try:
		myForm = FormManager(form_structure)
	except KeyboardInterrupt:
		import sys
		print("\n\nThe form was cancelled")
		sys.exit()
	record = myForm.record()
	print(json.dumps(record, indent=4))


example_form_structures = [
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Personal Information Form with Example Values": [
            {"label": "First Name", "type": "text", "value": "John"},
            {"label": "Last Name", "type": "text", "value": "Doe"},
            {"label": "Email", "type": "text", "value": "john.doe@example.com"},
            {"label": "Password", "type": "password", "value": "password123"},
            {"label": "Gender", "type": "radio", "options": ["Male", "Female", "Other"], "value": "Male"}
        ],
        "Address Form with Example Values": [
            {"label": "Street", "type": "text", "value": "123 Main St"},
            {"label": "City", "type": "text", "value": "Anytown"},
            {"label": "State", "type": "text", "value": "CA"},
            {"label": "Zip Code", "type": "text", "value": "90210"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Job Application Form with Example Values": [
            {"label": "Position Applied For", "type": "text", "value": "Software Engineer"},
            {"label": "First Name", "type": "text", "value": "Jane"},
            {"label": "Last Name", "type": "text", "value": "Smith"},
            {"label": "Email", "type": "text", "value": "jane.smith@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-1234"}
        ],
        "Work Experience Form with Example Values": [
            {"label": "Company", "type": "text", "value": "Tech Corp"},
            {"label": "Position", "type": "text", "value": "Developer"},
            {"label": "Start Date", "type": "text", "value": "01/01/2020"},
            {"label": "End Date", "type": "text", "value": "Present"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Event Registration Form with Example Values": [
            {"label": "Event Name", "type": "text", "value": "Annual Conference"},
            {"label": "First Name", "type": "text", "value": "Alice"},
            {"label": "Last Name", "type": "text", "value": "Johnson"},
            {"label": "Email", "type": "text", "value": "alice.johnson@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-5678"}
        ],
        "Attendance Preferences Form with Example Values": [
            {"label": "Attendance Mode", "type": "radio", "options": ["In-person", "Virtual"], "value": "In-person"},
            {"label": "Meal Preference", "type": "dropdown", "options": ["Vegetarian", "Non-Vegetarian", "Vegan"], "value": "Vegetarian"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Survey Form with Example Values": [
            {"label": "Age Group", "type": "dropdown", "options": ["<18", "18-25", "26-35", "36-45", "46-60", "60+"], "value": "26-35"},
            {"label": "Favorite Color", "type": "text", "value": "Blue"},
            {"label": "Feedback", "type": "text_area", "value": "Great service!"}
        ],
        "Rating Form with Example Values": [
            {"label": "Satisfaction Level", "type": "radio", "options": ["Very Satisfied", "Satisfied", "Neutral", "Dissatisfied", "Very Dissatisfied"], "value": "Satisfied"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Product Order Form with Example Values": [
            {"label": "Product Name", "type": "text", "value": "Widget"},
            {"label": "Quantity", "type": "text", "value": "10"},
            {"label": "Price per Unit", "type": "text", "value": "9.99"}
        ],
        "Shipping Information Form with Example Values": [
            {"label": "Recipient Name", "type": "text", "value": "Bob Brown"},
            {"label": "Street Address", "type": "text", "value": "456 Elm St"},
            {"label": "City", "type": "text", "value": "Othertown"},
            {"label": "State", "type": "text", "value": "TX"},
            {"label": "Zip Code", "type": "text", "value": "75001"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Contact Us Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Charlie Davis"},
            {"label": "Email", "type": "text", "value": "charlie.davis@example.com"},
            {"label": "Subject", "type": "text", "value": "Inquiry"},
            {"label": "Message", "type": "text_area", "value": "I would like more information about your services."}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Feedback Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Daniel Evans"},
            {"label": "Email", "type": "text", "value": "daniel.evans@example.com"},
            {"label": "Comments", "type": "text_area", "value": "I really enjoyed using your product."},
            {"label": "Rating", "type": "radio", "options": ["1", "2", "3", "4", "5"], "value": "5"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Newsletter Signup Form with Example Values": [
            {"label": "First Name", "type": "text", "value": "Emily"},
            {"label": "Last Name", "type": "text", "value": "Foster"},
            {"label": "Email", "type": "text", "value": "emily.foster@example.com"},
            {"label": "Preferences", "type": "checkbox", "options": ["Daily Updates", "Weekly Summary", "Monthly Newsletter"], "value": "Weekly Summary"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Customer Support Ticket Form with Example Values": [
            {"label": "Name", "type": "text", "value": "George Harris"},
            {"label": "Email", "type": "text", "value": "george.harris@example.com"},
            {"label": "Issue Type", "type": "dropdown", "options": ["Technical", "Billing", "General"], "value": "Technical"},
            {"label": "Description", "type": "text_area", "value": "I am experiencing a technical issue with your software."}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Reservation Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Helen Johnson"},
            {"label": "Email", "type": "text", "value": "helen.johnson@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-7890"},
            {"label": "Reservation Date", "type": "text", "value": "2024-12-25"},
            {"label": "Number of Guests", "type": "text", "value": "4"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Conference Registration Form with Example Values": [
            {"label": "Conference Name", "type": "text", "value": "Tech Innovators Conference"},
            {"label": "First Name", "type": "text", "value": "Ian Kelly"},
            {"label": "Last Name", "type": "text", "value": "Kelly"},
            {"label": "Email", "type": "text", "value": "ian.kelly@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-1234"},
            {"label": "Job Title", "type": "text", "value": "CTO"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Loan Application Form with Example Values": [
            {"label": "Applicant Name", "type": "text", "value": "Jack Lee"},
            {"label": "Email", "type": "text", "value": "jack.lee@example.com"},
            {"label": "Loan Amount", "type": "text", "value": "100000"},
            {"label": "Loan Purpose", "type": "text", "value": "Home Renovation"},
            {"label": "Annual Income", "type": "text", "value": "75000"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Membership Application Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Karen Martinez"},
            {"label": "Email", "type": "text", "value": "karen.martinez@example.com"},
            {"label": "Membership Type", "type": "dropdown", "options": ["Basic", "Premium", "VIP"], "value": "Premium"},
            {"label": "Payment Method", "type": "dropdown", "options": ["Credit Card", "PayPal", "Bank Transfer"], "value": "Credit Card"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Appointment Booking Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Larry Nelson"},
            {"label": "Email", "type": "text", "value": "larry.nelson@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-3456"},
            {"label": "Preferred Date", "type": "text", "value": "2024-07-30"},
            {"label": "Preferred Time", "type": "text", "value": "10:00 AM"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Volunteer Signup Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Maria O'Connor"},
            {"label": "Email", "type": "text", "value": "maria.oconnor@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-6789"},
            {"label": "Availability", "type": "text_area", "value": "Weekends and evenings"},
            {"label": "Skills", "type": "text_area", "value": "Event planning, fundraising"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Travel Booking Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Nathan Parker"},
            {"label": "Email", "type": "text", "value": "nathan.parker@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-4321"},
            {"label": "Destination", "type": "text", "value": "Paris, France"},
            {"label": "Travel Dates", "type": "text", "value": "2024-08-01 to 2024-08-15"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Event Feedback Form with Example Values": [
            {"label": "Name", "type": "text", "value": "Olivia Quinn"},
            {"label": "Email", "type": "text", "value": "olivia.quinn@example.com"},
            {"label": "Event Attended", "type": "text", "value": "Annual Tech Summit"},
            {"label": "Feedback", "type": "text_area", "value": "The event was very informative and well-organized."},
            {"label": "Rating", "type": "radio", "options": ["1", "2", "3", "4", "5"], "value": "4"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Class Registration Form with Example Values": [
            {"label": "Class Name", "type": "text", "value": "Introduction to Python"},
            {"label": "Student Name", "type": "text", "value": "Paul Roberts"},
            {"label": "Email", "type": "text", "value": "paul.roberts@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-9876"},
            {"label": "Preferred Time Slot", "type": "dropdown", "options": ["Morning", "Afternoon", "Evening"], "value": "Morning"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Medical History Form with Example Values": [
            {"label": "Patient Name", "type": "text", "value": "Rachel Scott"},
            {"label": "Email", "type": "text", "value": "rachel.scott@example.com"},
            {"label": "Phone Number", "type": "text", "value": "555-6543"},
            {"label": "Date of Birth", "type": "text", "value": "1980-05-15"},
            {"label": "Known Allergies", "type": "text_area", "value": "Peanuts, Penicillin"},
            {"label": "Current Medications", "type": "text_area", "value": "Metformin, Lisinopril"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40}
        },
        "Research Survey Form with Example Values": [
            {"label": "Participant Name", "type": "text", "value": "Steven Turner"},
            {"label": "Email", "type": "text", "value": "steven.turner@example.com"},
            {"label": "Age Group", "type": "dropdown", "options": ["<18", "18-25", "26-35", "36-45", "46-60", "60+"], "value": "36-45"},
            {"label": "Survey Questions", "type": "text_area", "value": "What is your primary source of news?"},
            {"label": "Additional Comments", "type": "text_area", "value": "I prefer online news sources over print media."}
        ]
    }
]

example_form_structures = [
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a JavaScript file."
        },
        "JavaScript File Notes Form": [
            {"label": "File Name", "type": "text", "value": "main.js"},
            {"label": "File Path", "type": "text", "value": "/path/to/main.js"},
            {"label": "Description", "type": "text_area", "value": "This file contains the main logic for the application."},
            {"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Integrated with backend API."},
            {"label": "Bug Notes", "type": "text_area", "value": "Fixed issue with async function."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
            {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a CSS file."
        },
        "CSS File Notes Form": [
            {"label": "File Name", "type": "text", "value": "styles.css"},
            {"label": "File Path", "type": "text", "value": "/path/to/styles.css"},
            {"label": "Description", "type": "text_area", "value": "This file contains the styling for the application."},
            {"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Styled the main layout."},
            {"label": "Bug Notes", "type": "text_area", "value": "Fixed issue with responsive design."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
            {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a PHP file."
        },
        "PHP File Notes Form": [
            {"label": "File Name", "type": "text", "value": "index.php"},
            {"label": "File Path", "type": "text", "value": "/path/to/index.php"},
            {"label": "Description", "type": "text_area", "value": "This file handles the main backend logic for the application."},
            {"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Connected with MySQL database."},
            {"label": "Bug Notes", "type": "text_area", "value": "Fixed SQL injection vulnerability."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
            {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a documentation file."
        },
        "Documentation File Notes Form": [
            {"label": "File Name", "type": "text", "value": "README.md"},
            {"label": "File Path", "type": "text", "value": "/path/to/README.md"},
            {"label": "Description", "type": "text_area", "value": "This file contains the documentation for the project."},
            {"label": "Revision Notes", "type": "text_area", "value": "Updated with installation instructions."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Added API documentation."},
            {"label": "Bug Notes", "type": "text_area", "value": "Corrected typos in usage examples."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
            {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a specified URL."
        },
        "URL Notes Form": [
            {"label": "URL", "type": "text", "value": "https://example.com"},
            {"label": "Description", "type": "text_area", "value": "This URL points to the main website of the project."},
            {"label": "Revision Notes", "type": "text_area", "value": "Updated website layout."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Integrated with new API."},
            {"label": "Bug Notes", "type": "text_area", "value": "Fixed broken links."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a Python file."
        },
        "Python File Notes Form": [
            {"label": "File Name", "type": "text", "value": "script.py"},
            {"label": "File Path", "type": "text", "value": "/path/to/script.py"},
            {"label": "Description", "type": "text_area", "value": "This file contains the main script logic for the application."},
            {"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Integrated with data processing module."},
            {"label": "Bug Notes", "type": "text_area", "value": "Fixed issue with data parsing."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
            {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
        ]
    },
    {
        "Config": {
            "html": True,
            "column": {"width": 2},
            "font": {"type": "Arial", "size": 12},
            "color": {"text": "black", "bg": "white"},
            "field": {"width": 40},
            "description": "Form for taking notes on a SQL file."
        },
        "SQL File Notes Form": [
            {"label": "File Name", "type": "text", "value": "database.sql"},
            {"label": "File Path", "type": "text", "value": "/path/to/database.sql"},
            {"label": "Description", "type": "text_area", "value": "This file contains the SQL script for database setup."},
            {"label": "Revision Notes", "type": "text_area", "value": "Added new tables."},
            {"label": "Implementation Notes", "type": "text_area", "value": "Optimized queries for performance."},
            {"label": "Bug Notes", "type": "text_area", "value": "Fixed syntax errors in SQL script."},
            {"label": "Project Notes", "type": "text_area", "value": "Part of the main project."},
            {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
        ]
    }
]
example_form_structure_with_checkboxes = {
    "Config": {
        "html": True,
        "column": {"width": 2},
        "font": {"type": "Arial", "size": 12},
        "color": {"text": "black", "bg": "white"},
        "field": {"width": 40},
        "description": "Form for taking notes on a project with multiple tags using checkboxes."
    },
    "Project Notes Form": [
        {"label": "Project Name", "type": "text", "value": "Example Project"},
        {"label": "Project Path", "type": "text", "value": "/path/to/project"},
        {"label": "Description", "type": "text_area", "value": "This project is an example to demonstrate checkboxes."},
        {"label": "Tags", "type": "checkbox", "options": ["frontend", "backend", "database", "testing", "deployment"], "values": ["frontend", "testing"]},
        {"label": "Revision Notes", "type": "text_area", "value": "Initial version created."},
        {"label": "Implementation Notes", "type": "text_area", "value": "Set up project structure and initial configurations."},
        {"label": "Bug Notes", "type": "text_area", "value": "Fixed initial setup issues."},
        {"label": "Related URL", "type": "text", "value": "https://example.com/documentation"}
    ]
}


