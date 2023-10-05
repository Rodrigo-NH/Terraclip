from terraclip import Terraclip

# tr = Terraclip(r'D:\srtm\cipo.kmz')
tr = Terraclip(r'D:\srtm\MP\dem\tobo.shp')
# tr = Terraclip(r'D:\MA\Trabalhos\2023\Amanda\sig\APP2.shp')
tr.setofolder(r'D:\srtm\MP')
# tr.listOTsources()
# tr.setdem(r'D:\srtm\ita.kml')
# tr.setdem(OTsource='SRTMGL1', OTapi='YourOpenTopographyAPIkeyHere')
tr.setdem(r'D:\srtm\MP\dem\test.tif')


tr.setparams(20, 0, 50, Takeoff=True, Land=False)
tr.execute()
print(tr.rtlalt())

# print(tr.maxterrain())
# print(tr.minterrain())
# print(tr.rtlalt())
tr.savemission(r'D:\srtm\MP\mission.kml')
tr.savemission(r'D:\srtm\MP\mission.txt')
