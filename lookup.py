from data import cc2_cn
from data import cc3_cn
from data import m49_cn

def lookup_countrycode(data):

    if isinstance(data, basestring):
        data = data.strip()
        if len(data) == 2:
            county_name = cc2_cn.get(data.upper())
            if not county_name:
                # To imporve data set log misses
                pass
            else:
                return county_name

        elif len(data) == 3:
            county_name = cc3_cn.get(data.upper())
            if not county_name:
                # To imporve data set log misses
                pass
            else:
                return county_name

    elif isinstance(data, int):
        if data < 895:
            county_name = m49_cn.get(data)
            if not county_name:
                # To imporve data set log misses
                pass
            else:
                return county_name
