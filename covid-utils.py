from source.downloader import *
from source.mzcrurls import *

if __name__=="__main__":
    json_data = download_json(HEALED_PER_DISTRICT)
    print(json_data)