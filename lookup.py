from data import cc2_cn
from data import cc3_cn

def lookup_countrycode(data):
    if data:
        data = data.strip()
        if len(data) == 2:
            county_name = cc2_cn.get(data.upper())
            if not county_name:
                # log misses to impove data set
                pass
            else:
                return county_name

        elif len(data) == 3:
            county_name = cc3_cn.get(data.upper())
            if not county_name:
                # log misses to impove data set
                pass
            else:
                return county_name
