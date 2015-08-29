__author__ = 'jvial'
import pandas as pd
import numpy as np

lith = pd.read_csv('corrected_lithology.csv')
geo = pd.read_csv('Complete_Geophysics.csv')

# Read in all ATV data once.

atv_dictionary = {}
print('Read in lith and geo')

def get_label(bore_id, depth):
    """
    Function to get the label, will return either a string, nan or None.
    I bore_id is unknown it will raise an error.

    If we are at a labelled stratigraphy it will return a string.
    If we are at an unlabbelled stratigraphy it will return NaN
    if we are outside the bounds it will return None.

    :param bore_id: A string containing the bore id
    :param depth: a float for the depth
    :return:
    """
    holeid = pd.unique(lith.HOLEID)

    if bore_id not in holeid.tolist():
        raise Exception('BoreId {} not in corrected lith logs'.format(bore_id))

    bore = lith.query('HOLEID == @bore_id and GEOLFROM < @depth and GEOLTO >= @depth')

    if bore.shape[0] >= 1:
        seam = bore.iloc[0, 5]  # The lith_seam is at location 5

    else:

        seam = None

    return seam



cols = ['ADEN', 'AUCS', 'AVOL', 'AXLE', 'AXLN', 'AZID', 'AZIF', 'AZP1', 'BBRG',
       'BISI', 'BRAD', 'BRDU', 'BRG1', 'BRG2', 'BRG3', 'BRG4', 'CADE', 'CALD',
       'CODE', 'CORF', 'DECR', 'DENB', 'DENL', 'DEPO', 'DIPF', 'FE1', 'FE1C',
       'FE1U', 'FE2', 'FMAG', 'GRDE', 'GRNP', 'HVOL', 'LSDU', 'LSN', 'MC2A',
       'MC2F', 'MC2U', 'MC4F', 'MC6F', 'MCUF', 'MDTC', 'MSAL', 'P1F', 'P2F',
       'P3F', 'PCH1', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RPOR', 'SPOR', 'SSN',
       'TDEP', 'TDIF', 'TEMP', 'TILD', 'UCS', 'UCSM', 'VDEN', 'VL2A', 'VL2F',
       'VL4F', 'VL6F', 'VLUF', 'UCSD', 'TILF', 'GRFE', 'DTCA',
       'DTCB', 'DTCC', 'DTCD', 'DTCE', 'DTCF']

atv_cols = ['ATV_AMP[0]',
            'ATV_AMP[1]',
            'ATV_AMP[2]',
            'ATV_AMP[3]',
            'ATV_AMP[4]',
            'ATV_AMP[5]',
            'ATV_AMP[6]',
            'ATV_AMP[7]',
            'ATV_AMP[8]',
            'ATV_AMP[9]',
            'ATV_AMP[10]',
            'ATV_AMP[11]',
            'ATV_AMP[12]',
            'ATV_AMP[13]',
            'ATV_AMP[14]',
            'ATV_AMP[15]',
            'ATV_AMP[16]',
            'ATV_AMP[17]',
            'ATV_AMP[18]',
            'ATV_AMP[19]',
            'ATV_AMP[20]',
            'ATV_AMP[21]',
            'ATV_AMP[22]',
            'ATV_AMP[23]',
            'ATV_AMP[24]',
            'ATV_AMP[25]',
            'ATV_AMP[26]',
            'ATV_AMP[27]',
            'ATV_AMP[28]',
            'ATV_AMP[29]',
            'ATV_AMP[30]',
            'ATV_AMP[31]',
            'ATV_AMP[32]',
            'ATV_AMP[33]',
            'ATV_AMP[34]',
            'ATV_AMP[35]',
            'ATV_AMP[36]',
            'ATV_AMP[37]',
            'ATV_AMP[38]',
            'ATV_AMP[39]',
            'ATV_AMP[40]',
            'ATV_AMP[41]',
            'ATV_AMP[42]',
            'ATV_AMP[43]',
            'ATV_AMP[44]',
            'ATV_AMP[45]',
            'ATV_AMP[46]',
            'ATV_AMP[47]',
            'ATV_AMP[48]',
            'ATV_AMP[49]',
            'ATV_AMP[50]',
            'ATV_AMP[51]',
            'ATV_AMP[52]',
            'ATV_AMP[53]',
            'ATV_AMP[54]',
            'ATV_AMP[55]',
            'ATV_AMP[56]',
            'ATV_AMP[57]',
            'ATV_AMP[58]',
            'ATV_AMP[59]',
            'ATV_AMP[60]',
            'ATV_AMP[61]',
            'ATV_AMP[62]',
            'ATV_AMP[63]',
            'ATV_AMP[64]',
            'ATV_AMP[65]',
            'ATV_AMP[66]',
            'ATV_AMP[67]',
            'ATV_AMP[68]',
            'ATV_AMP[69]',
            'ATV_AMP[70]',
            'ATV_AMP[71]',
            'ATV_AMP[72]',
            'ATV_AMP[73]',
            'ATV_AMP[74]',
            'ATV_AMP[75]',
            'ATV_AMP[76]',
            'ATV_AMP[77]',
            'ATV_AMP[78]',
            'ATV_AMP[79]',
            'ATV_AMP[80]',
            'ATV_AMP[81]',
            'ATV_AMP[82]',
            'ATV_AMP[83]',
            'ATV_AMP[84]',
            'ATV_AMP[85]',
            'ATV_AMP[86]',
            'ATV_AMP[87]',
            'ATV_AMP[88]',
            'ATV_AMP[89]',
            'ATV_AMP[90]',
            'ATV_AMP[91]',
            'ATV_AMP[92]',
            'ATV_AMP[93]',
            'ATV_AMP[94]',
            'ATV_AMP[95]',
            'ATV_AMP[96]',
            'ATV_AMP[97]',
            'ATV_AMP[98]',
            'ATV_AMP[99]',
            'ATV_AMP[100]',
            'ATV_AMP[101]',
            'ATV_AMP[102]',
            'ATV_AMP[103]',
            'ATV_AMP[104]',
            'ATV_AMP[105]',
            'ATV_AMP[106]',
            'ATV_AMP[107]',
            'ATV_AMP[108]',
            'ATV_AMP[109]',
            'ATV_AMP[110]',
            'ATV_AMP[111]',
            'ATV_AMP[112]',
            'ATV_AMP[113]',
            'ATV_AMP[114]',
            'ATV_AMP[115]',
            'ATV_AMP[116]',
            'ATV_AMP[117]',
            'ATV_AMP[118]',
            'ATV_AMP[119]',
            'ATV_AMP[120]',
            'ATV_AMP[121]',
            'ATV_AMP[122]',
            'ATV_AMP[123]',
            'ATV_AMP[124]',
            'ATV_AMP[125]',
            'ATV_AMP[126]',
            'ATV_AMP[127]',
            'ATV_AMP[128]',
            'ATV_AMP[129]',
            'ATV_AMP[130]',
            'ATV_AMP[131]',
            'ATV_AMP[132]',
            'ATV_AMP[133]',
            'ATV_AMP[134]',
            'ATV_AMP[135]',
            'ATV_AMP[136]',
            'ATV_AMP[137]',
            'ATV_AMP[138]',
            'ATV_AMP[139]',
            'ATV_AMP[140]',
            'ATV_AMP[141]',
            'ATV_AMP[142]',
            'ATV_AMP[143]']


def get_windows(boreid, centre_point, window_size, bin_width):
    """
    Function to get data related to the windows around a point.
    Note that the first run with a new bore id will need to load
    the data from xls (SLOOOOW!) subsequent runs will use a cached
    form of this data.

    :param bore_id: String of the bore id.
    :param centre_point: depth of the centre oint
    :param window_size: window size in meters.
    :param bin_width: bin width in meters
    :return: will return a pandas data frame containing data.
    """

    bore = geo.query('HOLEID == @boreid').sort('DEPTH')

    if atv_dictionary.get(boreid, None) is None:
        print('Need to read the acoustic scanner file')
        atv = pd.read_excel('Acoustic Scanner/ATV_Data_{}.xlsx'.format(boreid))
        print('done')
        atv_dictionary[boreid] = atv
    else:
        atv = atv_dictionary[boreid]

    bottom = centre_point - window_size/2.
    top = centre_point + window_size/2.

    bore = bore.query('DEPTH > @bottom and DEPTH <= @top').sort('DEPTH')

    atv = atv.rename(columns={'MD': 'DEPTH'})
    atv = atv.query('DEPTH > @bottom and DEPTH <= @top').sort('DEPTH')

    def bin_number(depth):
        return np.floor(depth/bin_width)*bin_width

    geo_df = bore.set_index('DEPTH')[cols].groupby(bin_number, axis=0).mean()
    atv_df = atv.set_index('DEPTH').groupby(bin_number).mean()

    result = pd.concat([geo_df, atv_df], axis=1)

    return result


def get_data(boreid, centre_point, window_size, bin_width):

    result = get_windows(boreid, centre_point, window_size, bin_width)

    result = result.reset_index().rename(columns={'index':'DEPTH'})

    result['LABELS'] = result.DEPTH.apply(lambda x: get_label(boreid, x))

    return result
