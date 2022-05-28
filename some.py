# flight_df = pd.DataFrame(response['states'])
# flight_df = flight_df.loc[:, 0:16]
# flight_df.columns = col_name
# flight_df = flight_df.fillna('No Data')
#
# # fix display table problem pycharm
# pd.set_option('display.max_columns', 100)
# pd.set_option('display.max_rows', 1000)
#
# pd.set_option('display.width', 500)

import pandas as pd

data_cow = [line.strip('\n') for line in open(r'C:\Users\red\Desktop\cow_frame.txt', 'r+', encoding='utf-8')]

col_name = ['ISO3166A2', 'ISO3166A3', 'ISO3166N3', 'FIPS104', 'ISOen_name', 'ISOen_proper', 'ISOen_ro_name',
            'ISOen_ro_proper', 'ISOfr_name', 'ISOfr_proper', 'ISOes_name', 'UNGEGNen_name', 'UNGEGNen_longname',
            'UNGEGNfr_name', 'UNGEGNfr_longname', 'UNGEGNes_name', 'UNGEGNes_longname', 'UNGEGNru_name',
            'UNGEGNru_longname', 'UNGEGNlc_ro_name', 'UNGEGNlc_ro_longname', 'BGN_name', 'BGN_proper',
            'BGN_longname', 'BGNlc_longname', 'BGNlc_name', 'PCGN_name', 'PCGN_proper', 'PCGN_longname',
            'FAOit_name', 'FAOit_proper', 'FAOit_longname', 'EKI_name', 'EKI_longname', 'conabbr', 'HasCapital',
            'BGN_capital', 'UNGEGNlc_capital', 'UNen_capital', 'UNfr_capital', 'UNes_capital', 'UNru_capital',
            'EKI_capital', 'BGNc_latitude', 'BGNc_longitude', 'UNc_latitude', 'UNc_longitude', 'continent',
            'subcontinent', 'ISOregion', 'ISOsubregion', 'language', 'population', 'year', 'BGN_demonym',
            'BGN_demomyn_adj', 'ITU', 'IVC', 'land', 'water', 'land_total', 'latitude', 'longitude',
            'max_latitude', 'min_latitude', 'max_longitude', 'min_longitude',
            'url_gov', 'url_stats', 'url_gis', 'url_post']

pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.width', 1000)

coordinates_df = pd.DataFrame(data_cow)
# coordinates_df = coordinates_df.loc[:, 0:71]
# coordinates_df.columns = col_name


print(coordinates_df.head())
