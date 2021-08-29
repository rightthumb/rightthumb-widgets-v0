#!/usr/bin/python3
import uuid
string = str(uuid.uuid4())
string = uuid.uuid4().hex
string = uuid.uuid4()
string = str(string)
string = '{' + string.upper() + '}'

print(string)