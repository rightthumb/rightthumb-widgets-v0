import _rightThumb._base3 as _
import _rightThumb._construct as __

aggregate_trigger_ran = False
def aggregate_trigger():
    global aggregate_trigger_ran
    if aggregate_trigger_ran:
        return None
    if not _.switches.isActive('Aggregate'):
        return None
    script = ' '.join(_.switches.values('Aggregate'))
    __.aggregate.obj.code(script, isSwitch=True)
class AGGREGATE:
    def __init__(self):
        self.records = {}
        self.index = {}
        self.columns = _.dot()
        self.columns.table = {}
        self.columns.group = {}
        self.columns.eof = {}
        self.columns.eot = {}
        self.columns.otherQ = {}
        self.columns.other = {}
        self.switch = _.dot()
        self.switch.label = '--sw--c3p0-r2d2-4life--sw--'
        self.switch.processed = False
        self.functions = _.dot()
        self.functions.index = {}
        self.other = _.dot()
        self.other.index = {}
        self.counter = -1
        self.formating = {}
        self.cache = _.dot()
        self.cache.records = {}
        self.cache.formating = {}
        self.last = '{D346F128-1468-481C-A0C8-FF8C6083EE64}'
        self.lasting = []
    def code(self, script, label=None, isSwitch=False, addSwitch=False, addAll=False):
        if script is None:
            return None
        self.counter += 1
        if isSwitch:
            label = self.switch.label
            if self.switch.processed:
                return self.records[label]
            self.switch.processed = True
        elif label is None:
            label = 'simple-' + str(self.counter)
        self.records[label] = []
        records = _.code(script=script, addString=[['alphaParam', '?']])
        indexes = _.dot()
        indexes.functions = {}
        indexes.table = []
        indexes.group = []
        indexes.eot = []
        indexes.eof = []
        indexes.otherVar = []
        indexes.otherVarQ = []
        indexes.other = []
        for fXn in __.aggregate.fn.order:
            indexes.functions[fXn] = []
        indexes.functions['other'] = []
        for rec in records:
            if rec['status'] and 'function' in rec['l']:
                if rec['txt'] in __.aggregate.fn.order:
                    indexes.functions[rec['txt']].append(rec)
                else:
                    indexes.functions['other'].append(rec)
            elif rec['status'] and 'variable' in rec['l']:
                if not '?' in rec['txt'] or ('?' in rec['txt'] and (not rec['txt'].lower().split('?')[0] + '?' in __.aggregate.prefixes)):
                    indexes.table.append(rec)
                elif rec['txt'].startswith('eot?'):
                    indexes.eot.append(rec)
                elif rec['txt'].startswith('eof?'):
                    indexes.eof.append(rec)
                elif rec['txt'].startswith('eog?'):
                    indexes.group.append(rec)
                elif rec['txt'].startswith('bog?'):
                    indexes.group.append(rec)
                elif rec['txt'].lower().startswith('eoga?'):
                    indexes.group.append(rec)
                elif '?' in rec['txt']:
                    indexes.otherVarQ.append(rec)
                else:
                    indexes.otherVar.append(rec)
            else:
                indexes.other.append(rec)
        tmp_records = []
        for fXn in __.aggregate.fn.order:
            for rec in indexes.functions[fXn]:
                tmp_records.append(rec)
        for rec in indexes.functions['other']:
            tmp_records.append(rec)
        for rec in indexes.table:
            tmp_records.append(rec)
        for rec in indexes.otherVarQ:
            tmp_records.append(rec)
        for rec in indexes.otherVar:
            tmp_records.append(rec)
        for rec in indexes.group:
            tmp_records.append(rec)
        for rec in indexes.eot:
            tmp_records.append(rec)
        for rec in indexes.eof:
            tmp_records.append(rec)
        for rec in indexes.other:
            tmp_records.append(rec)
        for rec in tmp_records:
            self.records[label].append(rec)
        table = {}
        for i, rec in enumerate(self.records[label]):
            table[str(rec['i'])] = str(self.counter) + '-' + str(i)
        for i, rec in enumerate(self.records[label]):
            self.records[label][i]['i'] = str(self.counter) + '-' + str(i)
        for i, rec in enumerate(self.records[label]):
            if str(rec['rent']) in table:
                self.records[label][i]['rent'] = table[str(rec['rent'])]
            if 'args' in rec:
                args = []
                for ar in rec['args']:
                    if str(ar) in table:
                        args.append(table[str(ar)])
                self.records[label][i]['args'] = args
            if 'p' in rec:
                self.records[label][i]['p'] = table[str(rec['p'])]
            if 'val' in rec:
                self.records[label][i]['val'] = table[str(rec['val'])]
        for i, rec in enumerate(self.records[label]):
            self.index[rec['i']] = rec
            if rec['status'] and 'function' in rec['l']:
                self.functions.index[rec['i']] = rec
            elif rec['status'] and 'variable' in rec['l']:
                if not '?' in rec['txt'] or ('?' in rec['txt'] and (not rec['txt'].lower().split('?')[0] + '?' in __.aggregate.prefixes)):
                    self.columns.table[rec['i']] = rec
                elif rec['txt'].startswith('eot?'):
                    self.columns.eot[rec['i']] = rec
                elif rec['txt'].startswith('eof?'):
                    self.columns.eof[rec['i']] = rec
                elif rec['txt'].startswith('eog?'):
                    self.columns.group[rec['i']] = rec
                elif rec['txt'].startswith('bog?'):
                    self.columns.group[rec['i']] = rec
                elif rec['txt'].lower().startswith('eoga?'):
                    self.columns.group[rec['i']] = rec
                elif '?' in rec['txt']:
                    self.columns.otherQ[rec['i']] = rec
                else:
                    self.columns.other[rec['i']] = rec
            else:
                self.other.index[rec['i']] = rec
        self.cache.records[label] = self.records[label]
        self.last = label
        self.lasting = [label]
        if addSwitch or addAll:
            return self.build(label=label, addSwitch=addSwitch, addAll=addAll)
        return self.records[label]
    def build(self, label=None, addSwitch=None, addAll=None, s=None):
        if not s is None:
            addSwitch = s
        if label is None:
            addAll = True
        records = []
        toProcess = []
        if addAll:
            for k in self.records:
                toProcess.append(k)
        elif addSwitch:
            if self.switch.label in self.records:
                toProcess.append(self.switch.label)
            if label in self.records:
                toProcess.append(label)
        self.last = '<?>'.join(toProcess)
        self.lasting = toProcess
        if self.last in self.cache.records:
            return self.cache.records[self.last]
        for lab in toProcess:
            for rec in self.records[lab]:
                records.append(rec)
        indexes = _.dot()
        indexes.functions = {}
        indexes.table = []
        indexes.group = []
        indexes.eot = []
        indexes.eof = []
        indexes.otherVar = []
        indexes.otherVarQ = []
        indexes.other = []
        for fXn in __.aggregate.fn.order:
            indexes.functions[fXn] = []
        indexes.functions['other'] = []
        for rec in records:
            if rec['status'] and 'function' in rec['l']:
                if rec['txt'] in __.aggregate.fn.order:
                    indexes.functions[rec['txt']].append(rec)
                else:
                    indexes.functions['other'].append(rec)
            elif rec['status'] and 'variable' in rec['l']:
                if not '?' in rec['txt'] or ('?' in rec['txt'] and (not rec['txt'].lower().split('?')[0] + '?' in __.aggregate.prefixes)):
                    indexes.table.append(rec)
                elif rec['txt'].startswith('eot?'):
                    indexes.eot.append(rec)
                elif rec['txt'].startswith('eof?'):
                    indexes.eof.append(rec)
                elif rec['txt'].startswith('eog?'):
                    indexes.group.append(rec)
                elif rec['txt'].startswith('bog?'):
                    indexes.group.append(rec)
                elif rec['txt'].lower().startswith('eoga?'):
                    indexes.group.append(rec)
                elif '?' in rec['txt']:
                    indexes.otherVarQ.append(rec)
                else:
                    indexes.otherVar.append(rec)
            else:
                indexes.other.append(rec)
        tmp_records = []
        for fXn in __.aggregate.fn.order:
            for rec in indexes.functions[fXn]:
                tmp_records.append(rec)
        for rec in indexes.functions['other']:
            tmp_records.append(rec)
        for rec in indexes.table:
            tmp_records.append(rec)
        for rec in indexes.otherVarQ:
            tmp_records.append(rec)
        for rec in indexes.otherVar:
            tmp_records.append(rec)
        for rec in indexes.group:
            tmp_records.append(rec)
        for rec in indexes.eot:
            tmp_records.append(rec)
        for rec in indexes.eof:
            tmp_records.append(rec)
        for rec in indexes.other:
            tmp_records.append(rec)
        combine_records = []
        for rec in tmp_records:
            combine_records.append(rec)
        self.cache.records[self.last] = combine_records
        return combine_records
    def formatGen(self, label=None, addSwitch=None, addAll=None, s=None):
        records = self.build(label=label, addSwitch=addSwitch, addAll=addAll, s=s)
        if self.last in self.cache.formating:
            return self.cache.formating[self.last]
        results = []
        for i, rec in enumerate(records):
            if rec['status'] and 'function' in rec['l'] and ('format' == rec['txt']):
                rXy = []
                for arg in rec['args']:
                    rXy.append(self.index[arg]['txt'])
                results.append(rXy)
            if rec['status'] and 'function' in rec['l'] and (rec['txt'] in __.aggregate.fn.format):
                rXy = []
                for arg in rec['args']:
                    rXy.append(self.index[arg]['txt'])
                rXy.append(__.aggregate.fn.format[rec['txt']])
                results.append(rXy)
            if rec['status'] and 'variable' in rec['l']:
                child = self.index[rec['val']]
                if 'function' in child['l'] and child['txt'] in __.aggregate.fn.format:
                    rXy = []
                    if '?' in rec['txt'] and rec['txt'].lower().split('?')[0] + '?' in __.aggregate.group_prefixes:
                        gc = rec['txt'].split('?')[2]
                        rXy.append(gc)
                    else:
                        rXy.append(rec['txt'])
                    rXy.append(__.aggregate.fn.format[child['txt']])
                    results.append(rXy)
        formating = {}
        for rXy in results:
            fields = []
            cmds = {}
            for res in rXy:
                if not res.startswith('?'):
                    fields.append(_.tfc(res))
                elif res.startswith('?') and (not res.startswith('??')) and (not res.startswith('???')):
                    last = res
                    if not res in cmds:
                        cmds[res] = {}
                elif res.startswith('???'):
                    cmds[last][last2][res] = {}
                elif res.startswith('??'):
                    last2 = res
                    cmds[last][res] = {}
            for f in fields:
                if not f in formating:
                    formating[f] = {}
                for c in cmds:
                    if not c in formating[f]:
                        formating[f][c] = {}
                    for p in cmds[c]:
                        if not p in formating[f][c]:
                            formating[f][c][p] = {}
                        for pp in cmds[c]:
                            if not pp in formating[f][c][p]:
                                formating[f][c][p][pp] = {}
        self.cache.formating[self.last] = formating
        pass
        return formating
    def format(self, fields, data, label=None, addSwitch=None, addAll=None, s=None):
        formating = self.formatGen(label=label, addSwitch=addSwitch, addAll=addAll, s=s)
        if not type(fields) is list:
            fields = [fields]
        try:
            for field in fields:
                f = _.tfc(field)
                if f in formating:
                    if '?date1' in formating[f]:
                        return _.friendlyDate(data)
                    if '?date' in formating[f]:
                        return _.friendlyDate2(data)
                    if '?size' in formating[f]:
                        data = str(data).replace(',', '').replace(' ', '')
                        if formating[f]['?size']:
                            fm = list(formating[f]['?size'].keys())[0]
                            return _.reFormatSize(str(data) + fm)
                        return _.formatSize(int(data))
                    if '?bytes' in formating[f]:
                        return _.unFormatSize(data)
                    if '?comma' in formating[f]:
                        return _.addComma(data)
        except Exception as e:
            return data
        return data