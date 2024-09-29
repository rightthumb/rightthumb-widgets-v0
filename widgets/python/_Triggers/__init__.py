import _rightThumb._construct as __
import _rightThumb._base3 as _
def expires(path,when):
    # import time
    # print('when:',when)
    _.pr(__.longSpace,r=1)
    # print('______________________expires:',_.timeAgo_past(when[0]))
    return _.mod(path) < _.timeAgo_past(when[0])