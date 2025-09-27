import _rightThumb._base3 as _

def dic_key_sort2(table, n=False, ip=False, r=False):
    keys = list(table.keys())
    dic = {}
    theData = []
    if ip:
        _.fields.register('cnt-ip', 'val', 7, m=3)
        for x in keys:
            if not x.count('.') == 3:
                theData.append(x)
            else:
                zZz = []
                for y in x.split('.'):
                    xXx = _.fields.padZeros('cnt-ip', 'val', int(y))
                    zZz.append(xXx)
                theData.append('.'.join(zZz))
        theData.sort()
        if r:
            theData.reverse()
        for x in theData:
            y = ''
            zZz = []
            if not x.count('.') == 3:
                y = x
            elif x.count('.') == 3:
                for y in x.split('.'):
                    zZz.append(str(int(y)))
                y = '.'.join(zZz)
            if y in table:
                dic[y] = table[y]
        return dic
    if not n:
        keys.sort()
        if r:
            keys.reverse()
        for x in keys:
            dic[x] = table[x]
        return dic
    else:
        nKeys = []
        _.fields.register('cnt-n', 'val', 7, m=40)
        for k in keys:
            nKeys.append(_.fields.padZeros('cnt-n', 'val', int(k)))
        nKeys.sort()
        if r:
            nKeys.reverse()
        for x in nKeys:
            dic[str(int(x))] = table[str(int(x))]
        return dic