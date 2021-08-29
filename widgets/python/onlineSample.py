#!/usr/bin/python3
name = "Joel"
job = "Programmer"

title = "{} the {}".format(name, job)
print(title)


title = name + " the " + job
print(title)

age = 28
title = "{} the {} of {} years".format(name, job, age)
print(title)


availability = ["Monday", "Wednesday", "Friday", "Saturday"]
result = " - ".join(availability)
print(result)


capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
}
print(capitals)

data = {"name": "John Smith", "hometown": {"name": "New York", "id": 123}}
print(data)

print(data['name'])
print(data['hometown'])
print(data['hometown']['id'])
print(data['hometown']['name'])


