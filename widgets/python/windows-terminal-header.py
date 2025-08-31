#!/usr/bin/python3
from random import choice
import os
import platform

if 'win' in platform.system().lower(): isWin=True
else:  isWin=False

if isWin: user = os.environ['USERNAME']
else: user = os.environ['USER']

if isWin: host = os.environ['COMPUTERNAME']
else: host = socket.gethostname()

import base64
emoji_encoded = b'8J+nu/Cfp6rwn5KA8J+mhvCfponwn6WT8J+mhPCfpoDwn5aV8J+No/CfjaTwn42l8J+NofCfpYPwn6We8J+QlfCfkb7wn5CJ8J+Qk/CfkIvwn5CM8J+QovCfkb3wn5G/8J+lkfCfkKHwn5CX8J+SkPCfj7nwn46o8J+QlPCfkJvwn46v8J+Mr/Cfk7fwn5u28J+llfCfjZLwn4248J+Ns/CfkLLwn46j8J+Qn/CfpoXwn5GA8J+QuPCfpJ7wn5Kq8J+SvvCfkbvwn5CK8J+NlPCfjK3wn42A8J+Vk/Cfporwn42f8J+lnfCflpXwn5CS8J+lnvCfkLzwn5OO8J+Qp/Cfkqnwn42V8J+NjfCfpo/wn42X8J+MiPCfkLPwn6aR8J+agPCfmYjwn5mK8J+ZifCfjK7wn6WS8J+QhfCfkK/wn42J8J+avfCfjYXwn5GF8J+OqfCfjbfwn5C18J+QkvCfpo3wn6an8J+QtvCfkJXwn6au8J+QleKAjfCfprrwn5Cp8J+QuvCfporwn6ad8J+QsfCfkIjwn5CI4oCN4qyb8J+mgfCfkK/wn5CF8J+QhvCfkLTwn5CO8J+mhPCfppPwn6aM8J+mrPCfkK7wn5CC8J+Qg/CfkITwn5C38J+QlvCfkJfwn5C98J+Qj/CfkJHwn5CQ8J+QqvCfkKvwn6aZ8J+mkvCfkJjwn6aj8J+mj/Cfppvwn5Ct8J+QgfCfkIDwn5C58J+QsPCfkIfwn5C/8J+mq/CfppTwn6aH8J+Qu/CfkLvigI3inYTvuI/wn5Co8J+QvPCfpqXwn6am8J+mqPCfppjwn6ah8J+QvvCfpoPwn5CU8J+Qk/CfkKPwn5Ck8J+QpfCfkKbwn5Cn8J+VivCfpoXwn6aG8J+movCfponwn6ak8J+qtvCfpqnwn6aa8J+mnPCfkLjwn5CK8J+QovCfpo7wn5CN8J+QsvCfkInwn6aV8J+mlvCfkLPwn5CL8J+QrPCfpq3wn5Cf8J+QoPCfkKHwn6aI8J+QmfCfkJrwn5CM8J+mi/CfkJvwn5Cc8J+QnfCfqrLwn5Ce8J+ml/CfqrPwn5W38J+VuPCfpoLwn6af8J+qsPCfqrHwn6ag8J+SkPCfjLjwn5Ku8J+qt/Cfj7Xwn4y58J+lgPCfjLrwn4y78J+MvPCfjLfwn4yx8J+qtPCfjLLwn4yz8J+MtPCfjLXwn4y+8J+Mv+KYmPCfjYDwn42B8J+NgvCfjYPwn42H8J+NiPCfjYnwn42K8J+Ni/CfjYzwn42N8J+lrfCfjY7wn42P8J+NkPCfjZHwn42S8J+Nk/Cfq5Dwn6Wd8J+NhfCfq5Lwn6Wl8J+lkfCfjYbwn6WU8J+llfCfjL3wn4y28J+rkfCfpZLwn6Ws8J+lpvCfp4Twn6eF8J+NhPCfpZzwn4yw8J+NnvCfpZDwn6WW8J+rk/Cfpajwn6Wv8J+lnvCfp4fwn6eA8J+NlvCfjZfwn6Wp8J+lk/CfjZTwn42f8J+NlfCfjK3wn6Wq8J+MrvCfjK/wn6uU8J+lmfCfp4bwn6Wa8J+Ns/CfpZjwn42y8J+rlfCfpaPwn6WX8J+Nv/Cfp4jwn6eC8J+lq/CfjbHwn42Y8J+NmfCfjZrwn42b8J+NnPCfjZ3wn42g8J+NovCfjaPwn42k8J+NpfCfpa7wn42h8J+ln/CfpaDwn6Wh8J+mgPCfpp7wn6aQ8J+mkfCfpqrwn42m8J+Np/Cfjajwn42p8J+NqvCfjoLwn42w8J+ngfCfpafwn42r8J+NrPCfja3wn42u8J+Nr/Cfjbzwn6Wb4piV8J+rlvCfjbXwn4228J+NvvCfjbfwn4248J+NufCfjbrwn4278J+lgvCfpYPwn6Wk8J+ni/Cfp4Pwn6eJ8J+nivCfpaLwn4298J+NtPCfpYTwn5Sq8J+PuvCfjI3wn4yO8J+Mj/CfjJDwn5e68J+XvvCfp63wn4+U4puw8J+Mi/Cfl7vwn4+V8J+PlvCfj5zwn4+d8J+PnvCfj5/wn4+b8J+Pl/Cfp7Hwn6qo8J+qtfCfm5bwn4+Y8J+PmvCfj6Dwn4+h8J+PovCfj6Pwn4+k8J+PpfCfjrXwn46244C94pyU4p2M4oGJ4p2T4p2U4p2V4p2X8J+mtPCfmYjwn5mJ8J+ZivCfkoDimKDwn5Kp8J+kofCfkbnwn5G68J+Ru/Cfkb3wn5G+8J+klvCfmLrwn5KL8J+MgPCfjIjwn4yR8J+MkvCfjJPwn4yU8J+MlfCfjJbwn4yX8J+MmPCfjJnwn4ya8J+Mm/CfjJzwn4yh4piA8J+MnfCfjJ7wn6qQ4q2Q8J+Mn/CfjKDwn4yM4piB4puF4puI8J+MpPCfjKXwn4ym8J+Mp/CfjKjwn4yp8J+MqvCfjKvwn4ys8J+MguKYguKYlOKbseKaoeKdhOKYg+KbhOKYhPCflKXwn5Kn8J+MivCfjoPwn46E4pmg4pml4pmm4pmj4pmf8J+OsvCfp6k='
decoded = base64.b64decode(emoji_encoded)
emojis = ''

for x in str(decoded.decode('utf-8')):
	emojis+=x

icons=list(emojis)

base='┌──('+user+choice(icons)+host+')-[ '+os.getcwd()+' ]'
try: print(base)
except: pass
