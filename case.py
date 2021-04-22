from rw_data import Yaml
from request import Method
from string import Template

class NLE(object):

  def __init__(self):
    self.m = Method()

  def login(self,*args):
    res = self.m.send(*args)
    global AccessToken
    AccessToken = res['ResultObj']['AccessToken']

  def add_project(self,*args):
    list(args)[1]['AccessToken'] = AccessToken
    args = tuple(list(args))
    res = self.m.send(*args)
    global projectId
    projectId = res['ResultObj']


  def add_device(self,*args):
    list(args)[1]['AccessToken'] = AccessToken
    list(args)[2]['ProjectIdOrTag'] = projectId
    args = tuple(list(args))
    res = self.m.send(*args)
    print(res)
    deviceId = res['ResultObj']

y = Yaml()
L = y.get_data()


obj = NLE()
for i in L:
  try:
    func = getattr(obj,i[0])
    func(*i[1:])

  except AttributeError as e:
    print('%s中没有自动化%s方法' % (obj.__class__,i[0]))