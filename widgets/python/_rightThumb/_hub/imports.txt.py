from inspect import currentframe, getframeinfo

frameinfo = getframeinfo(currentframe())

print(frameinfo.filename, frameinfo.lineno)