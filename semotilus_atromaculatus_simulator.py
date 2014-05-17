import sys
import datetime
from chubmodel import WaterBody, Temperature, longitude, getBestLake

hydro_data = [
    WaterBody('Abitibi'   , longitude(79, 45,  0), Temperature(4.35, 7.97, 75)),
    WaterBody('Brome'     , longitude(72, 29, 46), Temperature(5.45, 9.73, 58)),
    WaterBody('Champlain' , longitude(73, 20,  0), Temperature(2.81, 7.39, 72)),
    WaterBody('Etchemin'  , longitude(70, 29, 40), Temperature(3.53, 9.44, 56)),
    WaterBody('Fraser'    , longitude(72, 10, 40), Temperature(6.43, 10.1, 73)),
    WaterBody('Leamy'     , longitude(75, 43, 22), Temperature(6.12, 12.2, 77)),
    WaterBody('Matapedia' , longitude(67, 35, 8), Temperature(3.30, 13.7, 84)),
    WaterBody('Meech'     , longitude(75, 53, 33), Temperature(5.93, 9.60, 70)),
    WaterBody('Mitis'     , longitude(67, 45, 17), Temperature(5.93, 15.9, 34)),
    WaterBody('Pohenegamook', longitude(69, 15, 32), Temperature(3.03, 12.4, 49)),
    WaterBody('Stukely'   , longitude(72, 15, 7), Temperature(7.03, 8.05, 77)),
    WaterBody('Saint-Francois', longitude(74, 22, 22), Temperature(6.40, 9.65, 83)),
    WaterBody('Saint-Jean', longitude(78,  1, 48), Temperature(3.23, 8.3, 67)),
    WaterBody('Tourouvre' , longitude(72, 53, 41), Temperature(7.14, 8.93, 92)),
    WaterBody('Temiscouata', longitude(68, 52, 20), Temperature(7.63, 9.01, 37))
    ]

if __name__ == '__main__':
    day = datetime.datetime.today();
    if len(sys.argv) > 1:
        day = datetime.datetime.strptime(sys.argv[1], '%m-%d')
    nth = (day - datetime.datetime(day.year, 1, 1)).days + 1
    print(getBestLake(hydro_data, nth).name)
#    for nth in range(1,365):
#        print(getBestLake(hydro_data, nth).name)
   
