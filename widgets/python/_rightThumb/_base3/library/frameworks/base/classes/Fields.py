import _rightThumb._base3 as _
import _rightThumb._construct as __

class Field:
    def __init__(self, project, name, value, appReg, script, maxField):
        self.appReg = appReg
        self.project = project
        self.name = name
        self.trigger = script
        self.maxField = maxField
        self.registerValue(value)
    def setTrigger(self, script):
        self.trigger = script
    def addPadding(self, value, extra, right, center):
        value = self.runTrigger(str(value))
        oValue = value
        addPadding = extra + self.maxField - len(value)
        add = ''
        i = 0
        l = ''
        r = ''
        while not len(value) >= self.maxField + extra:
            i += 1
            if i % 2 == 0:
                l += ' '
            else:
                r += ' '
            value += ' '
            add += ' '
        if right:
            value = add + oValue
        if center:
            value = l + oValue + r
        return value
    def addPaddingSetSpaces(self, value):
        value = self.runTrigger(str(value))
        addPadding = self.maxField - len(value)
        newValue = value
        Zeros = ''
        while not len(newValue) == self.maxField:
            Zeros += ' '
            newValue = Zeros + value
        return newValue
    def addPaddingZeros(self, value):
        value = self.runTrigger(str(value))
        addPadding = self.maxField - len(value)
        newValue = value
        Zeros = ''
        while not len(newValue) == self.maxField:
            Zeros += '0'
            newValue = Zeros + value
        return newValue
    def runTrigger(self, value):
        if type(self.trigger) == bool:
            return value
        return self.trigger(value)
    def registerValue(self, value):
        thisLen = len(self.runTrigger(str(value)))
        if thisLen > self.maxField:
            self.maxField = thisLen
class Fields:
    def __init__(self):
        self.fields = {}
        self.extra = 0
    def lengths(self, project):
        if _.switches.isActive('Long'):
            minLength = False
        else:
            minLength = True
        result = {}
        for record in self.fields[project]:
            if record.project == project:
                if minLength:
                    result[record.name] = 43
                else:
                    result[record.name] = record.maxField
        return result
    def register(self, project='', names='', value='', appReg=False, script=False, maxField=None, p=None, n=None, v=None, m=None, isRegisterDic=False):
        if not p is None:
            project = p
        if not n is None:
            names = n
        if not v is None:
            value = v
        maxField = 0
        if not maxField is None:
            maxField = maxField
        if not m is None:
            maxField = m
        if type(appReg) == bool:
            appReg = __.appReg
        if not project in self.fields:
            self.fields[project] = []
        for name in names.split(','):
            shouldAdd = True
            for i, s in enumerate(self.fields[project]):
                if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and (name == self.fields[project][i].name):
                    shouldAdd = False
            if shouldAdd:
                self.fields[project].append(Field(project, name, value, appReg, script, maxField))
                if maxField and type(value) == int:
                    return self.fields[project][len(self.fields[project]) - 1].addPaddingZeros(value)
                elif maxField and type(value) == str:
                    return self.fields[project][len(self.fields[project]) - 1].addPadding(value)
            else:
                self.registerValue(project, name, value, appReg)
    def registerValue(self, project, name, value, appReg=False):
        if type(appReg) == bool:
            appReg = __.appReg
        result = False
        for i, s in enumerate(self.fields[project]):
            if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and (name == self.fields[project][i].name):
                self.fields[project][i].registerValue(value)
                result = True
        return result
    def padZeros(self, project, name, value, extra=None, appReg=False, space=False):
        if extra is None:
            extra = self.extra
        if type(appReg) == bool:
            appReg = __.appReg
        for i, s in enumerate(self.fields[project]):
            if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and (name == self.fields[project][i].name):
                if space:
                    return self.fields[project][i].addPaddingSetSpaces(value)
                else:
                    return self.fields[project][i].addPaddingZeros(value)
                result = self.fields[project][i].addPaddingZeros(value)
        return result
    def value(self, project, name, value, extra=None, right=False, appReg=False, r=None, center=False):
        result = value
        if not r is None:
            right = r
        if extra is None:
            extra = self.extra
        if type(appReg) == bool:
            appReg = __.appReg
        for i, s in enumerate(self.fields[project]):
            if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and (name == self.fields[project][i].name):
                result = self.fields[project][i].addPadding(value, extra, right, center)
        return result
    def valuez(self, project, name, value, appReg=False):
        if type(appReg) == bool:
            appReg = __.appReg
        for i, s in enumerate(self.fields[project]):
            if self.fields[project][i].appReg == appReg and project == self.fields[project][i].project and (name == self.fields[project][i].name):
                result = self.fields[project][i].addPaddingZeros(value)
        return result
    def asset(self, project, asset, appReg=False):
        self.fields[project] = []
        if type(appReg) == bool:
            appReg = __.appReg
        if type(asset) == dict:
            self.registerDic(project, asset, appReg)
        if type(asset) == list:
            for row in asset:
                if type(row) == dict:
                    self.registerDic(project, row, appReg)
    def registerDic(self, project, asset, appReg=False):
        if type(appReg) == bool:
            appReg = __.appReg
        for name in asset.keys():
            self.register(project, name, asset[name], appReg, isRegisterDic=True)