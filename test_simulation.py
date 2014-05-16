import unittest
import datetime
import math
from chubmodel import WaterBody, longitude, Temperature

class TestSimulation(unittest.TestCase):

    def test_simulation(self):
        hydro_data = [
            WaterBody('Saint-Jean', longitude(78,  1, 48), Temperature(3.23, 8.3, 67)),
            WaterBody('Etchemin',   longitude(70, 29, 40), Temperature(3.53, 9.4, 67))
            ]
        self.assertEqual(chubmodel.getBestLake(hydro_data, 280).name, 'Saint-Jean')

    def test_longitude(self):
        self.assertEqual(1, longitude(0,0,1))
        self.assertEqual(60, longitude(0,1,0))
        self.assertEqual(3600, longitude(1,0,0))
        self.assertEqual(3666, longitude(1,1,6))

    def test_temperature_model(self):
        model = Temperature(10, 100, 30)
        
        for d in range(1,366):
            t = model.getTemperature(d)
            self.assertTrue(89.9 < t < 110.1)

        t0 = model.getTemperature(1)
        t = model.getTemperature(365)
        self.assertTrue(math.fabs(t - t0) < 0.1)
        t = model.getTemperature(0)
        self.assertTrue(math.fabs(t - t0) < 0.1)
        t = model.getTemperature(373)
        self.assertTrue(math.fabs(t - t0) < 0.1)

        t = model.getTemperature(30)
        self.assertTrue(math.fabs(t - 90.0) < 0.5)
        t = model.getTemperature(30 + 91)
        self.assertTrue(math.fabs(t - 100.0) < 0.5)
        t = model.getTemperature(30 + 182)
        self.assertTrue(math.fabs(t - 110.0) < 0.5)
        t = model.getTemperature(30 + 273)
        self.assertTrue(math.fabs(t - 100.0) < 0.5)

if __name__ == '__main__':
    unittest.main()
