import _rightThumb._base3 as _
import _rightThumb._construct as __
import _rightThumb._profileVariables as _profile

import importlib
class regImp:
    def __init__(self, focus=None, app=None, argvProcessForce=False, dirty=False, a=None, i=None):
        if focus == 0:
            focus = None
        DEFAULTS = {'file-open': {'Clean': 1}}
        if not '__' and '.' in focus or app is None:
            return __.imp(focus)
        if not a is None:
            app = a
        if not i is None:
            app = i
        if app is None:
            _.err('class regImp', 'expected: _.regImp(__.appReg,app)  or _.regImp(focus(),app)')
        if focus is None:
            focus = __.appReg
        _.regImps[focus] = {}
        self.app = app
        self.parent = focus
        self.imp = importlib.import_module(app)
        self.focus = self.imp.focus(parentApp=focus)
        self.focusPop = focus
        self.saveLog = True
        try:
            self.imp.registerSwitches(argvProcessForce=False)
        except Exception as e:
            self.imp.sw()
        _.appInfo[self.imp.focus(focus)] = _.appInfo[self.imp.focus()]
        _.appData[self.imp.focus(focus)] = _.appData[self.imp.focus()]
        __.constructRegistration(_.appInfo[self.imp.focus(focus)]['file'], self.imp.focus(focus))
        _.regImps[focus] = {}
        _.regImps[focus][app] = self.imp
        __.appReg = self.focusPop
        if dirty and (not self.focus == '__init___-___init__'):
            self.imp.appDBA = self.focus
        if app in DEFAULTS:
            for sw in DEFAULTS[app]:
                if type(DEFAULTS[app][sw]) == str:
                    self.switch(sw, DEFAULTS[app][sw])
                elif DEFAULTS[app][sw]:
                    self.switch(sw)
                else:
                    self.switch(sw, delete=True)
    def provideImport(self):
        return self.imp
    def listFunctions(self):
        self.functions
        for func in self.functions:
            _.print_(func['name'], func['args'])
    def pipe(self, data=[], xfer=False, clear=True, appReg=False):
        if type(data) == bool:
            return _.appData[self.focus]['pipe']
        if type(appReg) == bool:
            appReg = self.focusPop
        if not len(data):
            if xfer:
                data = _.appData[appReg]['pipe']
                if clear:
                    _.appData[appReg]['pipe'] = []
        _.appData[self.focus]['pipe'] = data
        try:
            _.appData[self.focus]['data']['table']['received']
            profile = _profile.records.audit('pipe', data, appReg=[appReg, self.focus])
            _.appData[appReg]['data']['table']['sent'].append(profile)
            _.appData[self.focus]['data']['table']['received'].append(profile)
        except Exception as e:
            pass
    def switch(self, names=[], value=None, appReg=False, dump=False, delete=False, d=False):
        if type(appReg) == bool:
            appReg = self.focusPop
        if dump:
            _.switches.dumpSwitches()
        else:
            for name in names.split(','):
                vl = value
                if name == 'Password' or name == 'Key':
                    vl = '*******'
                if not value is None:
                    try:
                        _.appData[self.focus]['data']['field']['received']
                        profile = _profile.records.audit(name, vl, appReg=[appReg, self.focus])
                        _.appData[appReg]['data']['field']['sent'].append(profile)
                        _.appData[self.focus]['data']['field']['received'].append(profile)
                    except Exception as e:
                        pass
                __.appReg = self.focus
                if delete or d:
                    _.switches.fieldSet(name, 'active', False)
                else:
                    _.switches.fieldSet(name, 'active', True)
                    if not value is None:
                        if type(value) == list:
                            _.switches.fieldSet(name, 'values', value)
                            _.switches.fieldSet(name, 'value', ','.join(value))
                        else:
                            _.switches.fieldSet(name, 'value', value)
                            _.switches.fieldSet(name, 'values', [value])
            pass
        __.appReg = self.focusPop
    def deleteSwitch(self, name):
        __.appReg = self.focus
        _.switches.fieldSet(name, 'active', False)
        __.appReg = self.focusPop
    def kwargs(self, *args, **kwargs):
        focusPop = True
        if 'focusPop' in kwargs:
            focusPop = kwargs['focusPop']
            del kwargs['focusPop']
        __.appReg = self.focus
        self.imp.appDBA = self.focus
        if args and kwargs:
            result = self.imp.action(*args, **kwargs)
        elif args:
            result = self.imp.action(*args)
        elif kwargs:
            result = self.imp.action(**kwargs)
        else:
            result = self.imp.action()
        if focusPop:
            __.appReg = self.focusPop
        return result
    def action(self, arg='c766f06b', focusPop=True):
        __.appReg = self.focus
        self.imp.appDBA = self.focus
        if not arg == 'c766f06b':
            result = self.imp.action(arg)
        else:
            result = self.imp.action()
        if focusPop:
            __.appReg = self.focusPop
        return result
    def do(self, *args, **kwargs):
        focusPop = True
        args = list(args)
        if len(args) == 1 and args[0] == 'action':
            return self.action()
        func = args.pop(0)
        _kwargs = {}
        for k in kwargs:
            if k == 'focusPop':
                focusPop = kwargs[k]
            else:
                _kwargs[k] = kwargs[k]
        __.appReg = self.focus
        if 'function' in str(type(func)):
            return func()
        elif type(func) == str:
            theFunction = eval('self.imp.' + func)
        else:
            theFunction = func
        result = 'theFunction' + _.fak(args, kwargs)
        if focusPop:
            __.appReg = self.focusPop
        return result
    def execute(self, func, arg=False, nofocus=False):
        global threads
        theFunc = eval('self.imp.' + func)
        shouldRun = True
        if not nofocus and type(arg) == bool:
            args = [self.focus]
        elif not nofocus and (not type(arg) == bool):
            args = [arg, self.focus]
        if nofocus and type(arg) == bool:
            shouldRun = False
            theID = threads.add('execute', theFunc, loaded=True)
        elif nofocus and (not type(arg) == bool):
            args = [arg]
        if shouldRun:
            theID = threads.add('execute', theFunc, args, loaded=True)
        return theID