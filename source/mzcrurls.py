# just a fucking bunch of urls for MZCr API

# v1 urls

# TODO

# v2 urls

# basic info
# '-> SINGLE DAY
BASE_INFO_V2 = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/zakladni-prehled.json"

# entry for each infected person
# '-> a lot of data, do not print :)
INFECTED_PER_DISTRICT = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/osoby.json"

# entry for each healed person
# '-> a lot of data, do not print :)
HEALED_PER_DISTRICT = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/vyleceni.json"

# entry for each deceased person
# '-> a lot of data, do not print :)
DEAD_PER_DISTRICT = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/umrti.json"

# entry for each hospitalized person
# '-> a lot of data, do not print :)
HOSPITALIZED_PER_DISTRICT = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/hospitalizace.json"

# history of all essential data throughout history
# '-> HISTORY
CUMULATIVE_DATA = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/nakazeni-vyleceni-umrti-testy.json"

# cumulative history per districts
# '-> HISTORY, per disctricts
CUMULATIVE_DATA_PER_DISTRICT = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/kraj-okres-nakazeni-vyleceni-umrti.json"

# daily reports from small districts
# '->
ORP_REPORTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/orp.json"

# daily reports from the smallest avialable districts
# '-> 
VILLAGE_REPORTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/obce.json"

# daily reports from the Prague districts
PRAGUE_REPORTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/mestske-casti.json"

WEEKLY_REPORTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/incidence-7-14-cr.json"

WEEKLY_REPORTS_PER_DISTRICTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/incidence-7-14-kraje.json"

WEEKLY_REPORTS_PER_VILLAGE = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/incidence-7-14-okresy.json"

# TESTING

DAILY_TESTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/testy-pcr-antigenni.json"

DAILY_CUMULATIVE_TESTS_PER_DISTRICTS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/kraj-okres-testy.json"

TESTING_AREAS = "https://onemocneni-aktualne.mzcr.cz/api/v2/covid-19/prehled-odberovych-mist.json"

# VACCINATION
# TODO

# ICU
# TODO only csv format