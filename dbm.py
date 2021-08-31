from math import sqrt, log10

class dBm:

    def __init__(self):
        self.dbm = 0
    
    def set_dbm(self, val):
        self.dbm = val  
        
    def set_v_p(self, val):
        self.dbm = 10 * log10(val ** 2 / 100) + 30
        
    def set_v_rms(self, val):
        self.dbm = 10 * log10(val ** 2 / 50) + 30
        
    def set_w(self, val):
        self.dbm = 10 * log10(val) + 30
        
    def set_v_pp(self, val):
        self.dbm = 10 * log10((val / 2) ** 2 / 100) + 30
    
    def _db(self, val):
        return 10 ** ((val - 30) / 10)

    def get_values(self):
        db = self._db(self.dbm)
        vp = sqrt(100 * db)
        vrms = sqrt(50 * db)
        watt = db
        vpp = sqrt(100 * db) * 2
        return self.dbm, vp, vrms, watt, vpp

    def __str__(self):
        s = 'db={}\nvp={}\nvrms={}\nwatt={}\nvpp={}'
        return s.format(*self.get_values())

if __name__ == '__main__':
    a = dBm()
    a.set_dbm(0)
    print(a.get_values())