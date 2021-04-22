import yaml,os


class Yaml(object):
  def read(self):
    file = os.getcwd() + '\data.yml'
    with open(file,'r',encoding='utf-8') as f:
       return yaml.load(f.read(),Loader=yaml.FullLoader)

  def get_data(self):
    return [[i['test_interface'],i['url'],i['header'],i['data']] for i in self.read()]


# y = Yaml()
# H = y.read()
# L = y.get_data()
# print(type(L))
# print(L)
# print((" ".join('%s' %id for id in L)))



