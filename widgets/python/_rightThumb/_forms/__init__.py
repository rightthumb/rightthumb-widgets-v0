# from _rightThumb._forms import genForm
# epyi forms -childe forms

import _rightThumb._construct as __;appDBA=__.clearFocus(__name__,__file__);__.appReg=appDBA;import _rightThumb._base3 as _;
def focus(parentApp='', childApp='', reg=True): global appDBA; f = __.appName(appDBA, parentApp, childApp); return f if reg else f
fieldSet=_.l.vars(focus(),__name__,__file__,appDBA);_.load();_v=__.imp('_rightThumb._vars');

def sw():
	pass
_._default_settings_()

_.appInfo[focus()] = {
	'file': '_rightThumb._forms',
	'description': 'Form builder',
	'categories': [
						'DEFAULT',
				],
	'examples': [
						_.hp('genForm(FormDict)'),
						_.linePrint(label='simple',p=0),
						'',
	],
	'columns': [
	],
	'aliases': [],
	'notes': [],
}

_.appInfo[focus()] = _.appInfoContinuity(__.thisApp( __file__ ),_.appInfo[focus()])
_.appData[focus()] = _.appDataContinuity()
def appRegDics(): return { 'appInfo': _.appInfo[focus()], 'appData': _.appData[focus()] }

def triggers():
	_._default_triggers_()
def _local_(do): exec(do)
_.l.conf('clean-pipe',True); _.l.sw.register( triggers, sw );
########################################################################################
#n)--> start




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
import re
class NameSpace: pass
_ns = NameSpace()
_ns.form_data = {}
_ns.formReg = {}
_ns.errors = []
shutdown_event = threading.Event()
class Server(SimpleHTTPRequestHandler):

	def _set_headers(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.end_headers()

	def _set_headersJSON(self):
		self.send_response(200)
		self.send_header('Content-type', 'application/json; charset=utf-8')
		self.end_headers()

	def do_GET(self):
		self._set_headers()
		html_content = self.generate_html_form()
		self.wfile.write(html_content.encode('utf-8'))

	def generate_html_form(self):
		if 'title' in _ns.config:
			title = _ns.config['title']
		else:
			title = 'Dynamic Form'
		description = title
		if 'description' in _ns.config:
			description = _ns.config['description']
		form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>{description}</h1><form method="post">'
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
				validation = field.get("validation", {})
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
				elif field_type == "checkbox":
					for option in options:
						checked = 'checked' if option in value else ''
						form_html += f"<input type='checkbox' name='{label}' value='{option}' {checked}>{option}<br>"

			form_html += "<br>"
		form_html += "<input type='submit' name='action' value='Submit'> &nbsp;&nbsp; <input type='submit' name='action' value='Cancel'></form></body></html>"
		return form_html

	def do_POST(self):
		content_length = int(self.headers['Content-Length'])
		post_data = self.rfile.read(content_length).decode('utf-8')
		# form_data = parse_qs(post_data)
		# form_data = {k: v[0] if v else '' for k, v in form_data.items()}
		form_data = parse_qs(post_data)
		for k, v in form_data.items():
			# Handle checkboxes: Multiple values for the same field name
			if isinstance(v, list) and len(v) > 1:
				form_data[k] = v
			else:
				form_data[k] = v[0] if v else ''

		# _.pr(line=1)
		# _.pv(form_data)
		# _.pr(line=1)

		all_fields = {}
		for section, fields in self.server.form_structure.items():
			if section == "Config":
				continue
			for field in fields:
				label = field.get("label")
				all_fields[label] = ''
		for k in all_fields:
			if not k in form_data:
				form_data[k] = ''
		_ns.form_data = form_data

		action = form_data.get('action')
		
		if 'title' in _ns.config:
			title = _ns.config['title']
		else:
			title = 'Dynamic Form'
		description = title
		if 'description' in _ns.config:
			description = _ns.config['description']
		description = description.strip()
		title = title.strip()
		description += ': Results'
		result = 'Validation Error'


		if action == 'Cancel':
			# Handle the cancel action
			self._set_headers()
			form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>Form was cancelled</h1><div class="centered"><h2 style="color:red">Form was cancelled</h2></div></body></html>'
			self.wfile.write(form_html.encode('utf-8'))
			shutdown_event.set()
			threading.Thread(target=self.server.shutdown).start()
			return
		


		errors = []
		for k in _ns.formReg:
			if not k == 'Config':
				for fld in _ns.formReg[k]:
					if 'validation' in fld:
						validation = fld['validation']
					else:
						validation = None
					if fld['label'] in form_data and validation:
						validationResult = validate_field(fld,form_data[fld['label']])
						if type(validationResult) == str:
							errors.append(validationResult)
		if len(errors):
			result = '<ul>'
			for error in errors:
				result += f'<li>{error}</li>'
			result += '</ul>'
			form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>{description}</h1><div class="centered"><h2 style="color:red">Validation Error</h2>{result}</div></body></html>'
			self._set_headers()
			self.wfile.write(form_html.encode('utf-8'))
			_ns.errors = errors
		self.server.form_data = form_data  # Update the server's form_data
		if not _ns.errors:
			result = json.dumps(form_data, indent=4)
			form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>{description}</h1><div class="centered"><pre>{result}</pre></div></body></html>'
			self._set_headers()
			self.wfile.write(form_html.encode('utf-8'))
		shutdown_event.set()
		threading.Thread(target=self.server.shutdown).start()


	# def generate_html_form(self):
	# 	if 'title' in _ns.config:
	# 		title = _ns.config['title']
	# 	else:
	# 		title = 'Dynamic Form'
	# 	description = title
	# 	if 'description' in _ns.config:
	# 		description = _ns.config['description']
	# 	form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>{description}</h1><form method="post">'
	# 	for section, fields in self.server.form_structure.items():
	# 		if section == "Config":
	# 			continue
	# 		form_html += f"<h2>{section}</h2>"
	# 		for field in fields:
	# 			label = field.get("label")
	# 			field_type = field.get("type")
	# 			options = field.get("options", [])
	# 			value = field.get("value", "")
	# 			field_config = field.get("config", {})
	# 			validation = field.get("validation", {})
	# 			width = field_config.get("width", self.server.form_structure.get("Config", {}).get("field", {}).get("width", 20))
	# 			form_html += f"<label>{label}</label><br>"
	# 			if field_type == "text":
	# 				form_html += f"<input type='text' name='{label}' value='{value}' size='{width}'><br>"
	# 			elif field_type == "password":
	# 				form_html += f"<input type='password' name='{label}' value='{value}' size='{width}'><br>"
	# 			elif field_type == "text_area":
	# 				form_html += f"<textarea name='{label}' rows='5' cols='{width}'>{value}</textarea><br>"
	# 			elif field_type == "radio":
	# 				for option in options:
	# 					checked = 'checked' if option == value else ''
	# 					form_html += f"<input type='radio' name='{label}' value='{option}' {checked}>{option}<br>"
	# 			elif field_type == "dropdown":
	# 				form_html += f"<select name='{label}'>"
	# 				for option in options:
	# 					selected = 'selected' if option == value else ''
	# 					form_html += f"<option value='{option}' {selected}>{option}</option>"
	# 				form_html += "</select><br>"
	# 		form_html += "<br>"
	# 	form_html += "<input type='submit' value='Submit'><input type='submit' value='Cancel'></form></body></html>"
	# 	return form_html

	# def do_POST(self):
	# 	content_length = int(self.headers['Content-Length'])
	# 	post_data = self.rfile.read(content_length).decode('utf-8')
	# 	form_data = parse_qs(post_data)
	# 	form_data = {k: v[0] if v else '' for k, v in form_data.items()}
	# 	all_fields = {}
	# 	for section, fields in self.server.form_structure.items():
	# 		if section == "Config":
	# 			continue
	# 		for field in fields:
	# 			label = field.get("label")
	# 			all_fields[label] = ''
	# 	for k in all_fields:
	# 		if not k in form_data:
	# 			form_data[k] = ''
	# 	_ns.form_data = all_fields
	# 	if 'title' in _ns.config:
	# 		title = _ns.config['title']
	# 	else:
	# 		title = 'Dynamic Form'
	# 	description = title
	# 	if 'description' in _ns.config:
	# 		description = _ns.config['description']
	# 	description = description.strip()
	# 	title = title.strip()
	# 	description += ': Results'
	# 	result = 'Validation Error'
	# 	errors = []
	# 	for k in _ns.formReg:
	# 		if not k == 'Config':
	# 			for fld in _ns.formReg[k]:
	# 				if 'validation' in fld:
	# 					validation = fld['validation']
	# 				else:
	# 					validation = None
	# 				if fld['label'] in form_data and validation:
	# 					validationResult = validate_field(fld,form_data[fld['label']])
	# 					if type(validationResult) == str:
	# 						errors.append(validationResult)
	# 	if len(errors):
	# 		result = '<ul>'
	# 		for error in errors:
	# 			result += f'<li>{error}</li>'
	# 		result += '</ul>'
	# 		form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>{description}</h1><div class="centered"><h2 style="color:red">Validation Error</h2>{result}</div></body></html>'
	# 		self._set_headers()
	# 		self.wfile.write(form_html.encode('utf-8'))
	# 		_ns.errors = errors
	# 	self.server.form_data = form_data  # Update the server's form_data
	# 	if not _ns.errors:
	# 		result = json.dumps(form_data, indent=4)
	# 		form_html = f'<html><head><title>{title}</title><link rel="stylesheet" href="https://a.sds.sh/?f=css/noForm.css&v=1.0"></head><body><h1>{description}</h1><div class="centered"><pre>{result}</pre></div></body></html>'
	# 		self._set_headers()
	# 		self.wfile.write(form_html.encode('utf-8'))
	# 	shutdown_event.set()
	# 	threading.Thread(target=self.server.shutdown).start()



def integrity(form_structure):
	if not 'Config' in form_structure:
		form_structure['Config'] = {}
	return form_structure



class FormManager:
	def __init__(self, form_structure):
		form_structure = integrity(form_structure)
		_ns.formReg = form_structure
		self.form_structure = form_structure
		self.index = {}
		for k in self.form_structure:
			if not k == 'Config':
				for fld in self.form_structure[k]:
					self.index[fld['label']] = fld
					

		self.form_data = {}
		self.config = self.form_structure.get("Config", {})
		_ns.config = self.config
		self.use_tkinter = self.detect_gui()
		if self.use_tkinter:
			if self.config.get("html", False):
				self.start_webserver()
				self.form_data = _ns.form_data
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

	def exit_tkinter(self):
		self.root.destroy()
		_.isExit(__file__)

	def create_tkinter_form(self):
		self.root = tk.Tk()
		self.root.title("Dynamic Form")
		# self.root.geometry("800x850")
		self.root.geometry('')
		row = 0
		for section, fields in self.form_structure.items():
			if section == "Config":
				continue
			ttk.Label(self.root, text=section, font=("Arial", 14, "bold")).grid(row=row, column=0, columnspan=2, pady=10)
			row += 1
			for field in fields:
				if field.get("type") == "checkbox":
					# _.pr('checkboxes', field,c='yellow')
					row += 4
				self.create_tkinter_field(field, row)
				row += 1
		ttk.Button(self.root, text="Submit", command=self.submit_tkinter_form).grid(row=row+len(fields), column=0, columnspan=2, pady=20)
		ttk.Button(self.root, text="Cancel", command=self.exit_tkinter).grid(row=row+len(fields), column=1, columnspan=2, pady=20)
		self.root.mainloop()


	def create_tkinter_field(self, field, row):
		label = field.get("label")
		field_type = field.get("type")
		options = field.get("options", [])
		value = field.get("value", "")
		col_span = field.get("col_span", 2)
		field_config = field.get("config", {})
		validation = field.get("validation", {})
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
		elif field_type == "checkbox":
			# Create a LabelFrame to contain the checkboxes
			checkbox_frame = ttk.LabelFrame(self.root, text=label, style=style_name)
			checkbox_frame.grid(row=row, column=1, columnspan=2, sticky=tk.W, padx=20, pady=5, ipadx=5, ipady=5)

			# Track the row within the LabelFrame
			checkbox_row = 0
			var = {}
			for option in options:
				option_var = tk.BooleanVar(value=option in value)
				var[option] = option_var
				cb_widget = ttk.Checkbutton(checkbox_frame, text=option, variable=option_var)
				cb_widget.grid(row=checkbox_row, column=0, sticky=tk.W, padx=5, pady=2)
				checkbox_row += 1

			# Store the variables in the form data dictionary
			self.form_data[label] = var
			row += 1  # Increment the main row counter after the LabelFrame


			# Store the variables in the form data dictionary
			self.form_data[label] = var



		self.form_data[label] = var
		

	def Field(self, label):
		if label in self.index:
			return self.index[label]
		return {}

	def submit_tkinter_form(self):
		data = {}
		for label, var in self.form_data.items():
			if isinstance(var, tk.Text):
				data[label] = var.get("1.0", tk.END).strip()
			elif isinstance(var, dict):  # Check for checkbox vars
				selected_options = [option for option, option_var in var.items() if option_var.get()]
				data[label] = selected_options
			else:
				data[label] = var.get()
		self.form_data = data  # Update form_data with submitted data
		_ns.form_data = data
		self.root.destroy()
		_ns.errors = []
		for field in self.form_data:
			fld = self.Field(field)
			self.validate_field(fld, self.form_data[field])


	# def submit_tkinter_form(self):
	# 	data = {}
	# 	for label, var in self.form_data.items():
	# 		if isinstance(var, tk.Text):
	# 			data[label] = var.get("1.0", tk.END).strip()
	# 		else:
	# 			data[label] = var.get()
	# 	self.form_data = data  # Update form_data with submitted data
	# 	_ns.form_data = data
	# 	self.root.destroy()
	# 	_ns.errors=[]
	# 	for field in self.form_data:
	# 		fld = self.Field(field)
	# 		self.validate_field(fld,self.form_data[field])

	def create_terminal_form(self):
		for section, fields in self.form_structure.items():
			if section == "Config":
				continue
			_.pr(line=1,c='green')
			_.pr(f"\n :: {section}",c='yellow')
			_.pr()
			for field in fields:
				self.create_terminal_field(field)


	def create_terminal_field(self, field):
		label = field.get("label")
		field_type = field.get("type")
		options = field.get("options", [])
		value = field.get("value", "")
		validation = field.get("validation", {})

		if field_type == "text":
			while True:
				user_input = input(f"{label} [{value}]: ") or value
				if self.validate_field(field, user_input, True):
					self.form_data[label] = user_input
					break
		elif field_type == "password":
			while True:
				user_input = getpass.getpass(f"{label}: ") or value
				if self.validate_field(field, user_input, True):
					self.form_data[label] = user_input
					break
		elif field_type == "text_area":
			while True:
				print(f"{label} [{value}]: (press Enter twice to finish)")
				lines = []
				while True:
					line = input()
					if line:
						lines.append(line)
					else:
						break
				user_input = "\n".join(lines) or value
				if self.validate_field(field, user_input, True):
					self.form_data[label] = user_input
					break
		elif field_type == "radio":
			while True:
				print(f"{label}:")
				for i, option in enumerate(options, 1):
					print(f"  {i}. {option}")
				try:
					choice = int(input("Choose an option: ")) - 1
					user_input = options[choice]
				except:
					user_input = value
				if self.validate_field(field, user_input, True):
					self.form_data[label] = user_input
					break
				_.pr()
				_.pr()
		elif field_type == "dropdown":
			while True:
				print(f"{label}:")
				for i, option in enumerate(options, 1):
					print(f"  {i}. {option}")
				try:
					choice = int(input("Choose an option: ")) - 1
					user_input = options[choice]
				except:
					user_input = value

				if self.validate_field(field, user_input, True):
					self.form_data[label] = user_input
					break
		elif field_type == "checkbox":
			selected_options = []
			print(f"{label}: (press Enter without input to finish)")
			for option in options:
				user_input = input(f"Include {option}? (y/N): ").strip().lower()
				if user_input == 'y':
					selected_options.append(option)
			self.form_data[label] = selected_options




	# def create_terminal_field(self, field):
	# 	label = field.get("label")
	# 	field_type = field.get("type")
	# 	options = field.get("options", [])
	# 	value = field.get("value", "")
	# 	validation = field.get("validation", {})
	# 	if field_type == "text":
	# 		while True:
	# 			user_input = input(f"{label} [{value}]: ") or value
	# 			if self.validate_field(field,user_input,True):
	# 				self.form_data[label] = user_input
	# 				break
	# 	elif field_type == "password":
	# 		while True:
	# 			user_input = getpass.getpass(f"{label}: ") or value
	# 			if self.validate_field(field,user_input,True):
	# 				self.form_data[label] = user_input
	# 				break
	# 	elif field_type == "text_area":
	# 		while True:
	# 			print(f"{label} [{value}]: (press Enter twice to finish)")
	# 			lines = []
	# 			while True:
	# 				line = input()
	# 				if line:
	# 					lines.append(line)
	# 				else:
	# 					break
	# 			user_input = "\n".join(lines) or value
	# 			if self.validate_field(field, user_input,True):
	# 				self.form_data[label] = user_input
	# 				break
	# 	elif field_type == "radio":
	# 		while True:
	# 			print(f"{label}:")
	# 			for i, option in enumerate(options, 1):
	# 				print(f"  {i}. {option}")
	# 			try:
	# 				choice = int(input("Choose an option: ")) - 1
	# 				user_input = options[choice]
	# 			except:
	# 				user_input = value
	# 			if self.validate_field(field,user_input,True):
	# 				self.form_data[label] = user_input
	# 				break
	# 			_.pr()
	# 			_.pr()
	# 	elif field_type == "dropdown":
	# 		while True:
	# 			print(f"{label}:")
	# 			for i, option in enumerate(options, 1):
	# 				print(f"  {i}. {option}")
	# 			try:
	# 				choice = int(input("Choose an option: ")) - 1
	# 				user_input = options[choice]
	# 			except:
	# 				user_input = value
				
	# 			if self.validate_field(field,user_input,True):
	# 				self.form_data[label] = user_input
	# 				break

	def finalValue(self,field,value):
		if not value:
			value = field['value']
		return value

	def validate_field(self,fld,value,check=False):
		updateFields(fld,value)
		label = fld['label']
		value = value
		if not 'validation' in fld:
			return True
		validation = fld['validation']
		Type = fld['type']
		if validation.get("required") and not value:
			if not check:
				_ns.errors.append(label+ ' is Required')
			return False
		if "required" in validation and validation["required"]:
			if not value:
				if not check:
					_ns.errors.append(label+ ' is Required')
				return False
		if "length" in validation:
			min_length = validation["length"].get("min", 0)
			max_length = validation["length"].get("max", float("inf"))
			if not (min_length <= len(value) <= max_length):
				if not Type == 'checkbox':
					if len(value) < min_length:
						if not check:
							_ns.errors.append(label+ ' is Short')
						return False
					if len(value) > max_length:
						if not check:
							_ns.errors.append(label+ ' is Long')
						return False
				if Type == 'checkbox':
					if len(value) < min_length:
						if not check:
							_ns.errors.append(label+ ' not enough options selected')
						return False
					if len(value) > max_length:
						if not check:
							_ns.errors.append(label+ ' too many options selected')
						return False
		if "regex" in validation:
			if not re.match(validation["regex"], value):
				if not check:
					_ns.errors.append(label+ ' has invalid pattern')
				return False
		if "url" in validation:
			post = postURL(validation['url'], {'value':value})
			if post == '0':
				return False
		return True

	def validate_field_old(self, value, validation):
		if validation.get("required") and not value:
			_.e("Validation error","This field is required.")
			return False
		if "required" in validation and validation["required"]:
			if not value:
				_.e("Validation error","This field is required.")
		if "length" in validation:
			min_length = validation["length"].get("min", 0)
			max_length = validation["length"].get("max", float("inf"))
			if not (min_length <= len(value) <= max_length):
				_.e("Validation error",f"Length must be between {min_length} and {max_length} characters.")
				return False
		if "regex" in validation:
			if not re.match(validation["regex"], value):
				_.e("Validation error","Invalid format.")
				return False
		return True

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

def validate_field(fld,value):
	updateFields(fld,value)
	label = fld['label']
	value = value
	validation = fld['validation']
	Type = fld['type']
	if validation.get("required") and not value:
		return label+ ' is Required'
	if "required" in validation and validation["required"]:
		if not value:
			return label+ ' is Required'
	if "length" in validation:
		min_length = validation["length"].get("min", 0)
		max_length = validation["length"].get("max", float("inf"))
		if not (min_length <= len(value) <= max_length):
			if not Type == 'checkbox':
				if len(value) < min_length:
					return label+ ' is Short'
				if len(value) > max_length:
					return label+ ' is Long'
			if Type == 'checkbox':
				if len(value) < min_length:
					return label+ ' not enough options selected'
				if len(value) > max_length:
					return label+ ' too many options selected'
	if "regex" in validation:
		if not re.match(validation["regex"], value):
			return label+ ' has invalid pattern'
	return True

def updateFields(field,value):
	formReg = {}
	for k in _ns.formReg:
		if k == 'Config':
			formReg[k] = _ns.formReg[k]
		if not k == 'Config':
			formReg[k] = []
			for fld in _ns.formReg[k]:
				if fld['label'] == field['label']:
					fld['value'] = value
				formReg[k].append(fld)
	_ns.formReg = formReg
import time



def encodeURL(string):
	import urllib.parse
	encoded_string = urllib.parse.quote(string)
	return encoded_string

def postURL(url, form_data=None, headers=None, browser_agent=None):
	if not type(url) == str:
		url = url[0]+encodeURL(url[1])
	import requests
	if form_data is None:
		form_data = {}
	if headers is None:
		headers = {}
	if browser_agent:
		headers['User-Agent'] = browser_agent
	response = requests.post(url, data=form_data, headers=headers)
	try:
		return response.json()
	except ValueError:
		return response.text


def submit(record,form_structure):
	if 'post' in form_structure:
		url = form_structure['post']
		form = {}
		form['structure'] = form_structure
		form['record'] = record
		postURL(form, record)
		_.pr('Uploaded',c='green')
	if 'save' in form_structure:
		_.saveTable2(form_structure['save'], record)
		_.pr('Saved',c='green')

	if 'table' in form_structure:
		_.saveTable(form_structure['save'], record)
		_.pr('Saved to Tables Folder',c='green')


def genForm(form_structure):
	if type(form_structure) == str:
		form_structure = json.loads(form_structure)
	
	if type(form_structure) == list:
		config = {}
		for i,form in enumerate(form_structure):
			if 'Config' in form: config = form['Config']
			if not 'Config' in form:
				form_structure[i]['Config'] = config
				
	if not type(form_structure) == list:
		forms = [form_structure]
	for form in forms:
		form = integrity(form)
		if 'getRecord' in form: form = postURL(form['getRecord'], form)
		try:
			myForm = FormManager(form)
		except KeyboardInterrupt:
			_.e("\n\nThe form was cancelled")
			sys.exit()
		record = myForm.record()
		if not _ns.errors:
			try: json.dumps(record, indent=4)
			except: _.e('Form exited'); sys.exit()
			submit(record,form)
			return record
		if _ns.errors:
			_.pr('Validation Errors:',c='red')
			if not 'html' in _ns.formReg['Config']:
				for error in _ns.errors:
					_.pr('\t',error,c='cyan')
			if not 'html' in _ns.formReg['Config']:
				time.sleep(3)
			else:
				time.sleep(5)
			
			_ns.errors=[]
			return genForm(_ns.formReg)



# epyi forms -childe forms





