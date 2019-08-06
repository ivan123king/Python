__author__ = 'lenovo'
#coding=utf-8

# import pygal.maps.world
import pygal
from pygal.style import RotateStyle

'''
生成世界地图
'''
wm_style = RotateStyle('#336699')
#设定绘制世界地图的颜色
wm = pygal.maps.world.World(style=wm_style)
wm.title = 'North,Central,and South America'
#生成表示国家人口的地图，ca是加拿大的缩写，缩写在pygal_maps_world.i18n.COUNTRIES中
wm.add('North America',{'ca':3214,'us':4096,'mx':1123})
#下面是仅仅将某个地区的国家统一用一种颜色标识出来
# wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
# wm.add('South Ameriac',['ar','bo','br','cl','co','ec','gf','gy','pe','py','sr','uy','ve'])

wm.render_to_file('americas_people.svg')