import requests,json


class Method(object):
    def send(self,url,headers,data):
        r = requests.post(url=url,headers=headers,data=data)
        res = json.loads(r.text)
        return res









"""
m = Method()
r = m.send('http://api.nlecloud.com/Projects',{'Content-Type': 'application/x-www-form-urlencoded','AccessToken':'7D7B27D53AE0C8F4C52CCFBE16BDE35B0127E039354B5A785BE3D2447EE5F798B5D1C8D3F1B1C5228CA2AD1F7DC81D9D6E47D352F1FA9AA394F58235D7F8DB8DA2DB2A52630E2AA689263102A2712D1500EE4EDEAF6B149B41578A1198F11F1875C62C0E33FE131EF35257F3E364E1BCD8E222692880FAACD77FE68C0F7628E36CD1F2CDFEFB3B0B8E7F41BB2E810976CBC32C18701B43A626B47208081AF36FBEF45CF650C24ACA5B258F593B7460ED8CFF12C0D22A2ED52F67EA075E0748F5'},{'Industry': 5, 'NetWorkKind': 2, 'Name': 'Project_123', 'Remark': None})
print(type(r))
print(r)
"""
