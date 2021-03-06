__author__ = 'Admin'
import utils as john


# list of holes in Complete_Geophysics.csv
# ['DD0509' 'DD0541' 'DD0542' 'DD0544' 'DD0551' 'DD0473' 'DD0409' 'DD0415'
#  'DD0980A' 'DD0989' 'DD1000' 'DD0991' 'DD1006' 'DD1005' 'DD1010' 'DD0992'
#  'DD1012' 'DD1013' 'DD1014' 'DD1070' 'DD1073' 'DD1077' 'DD1080' 'DD1081'
#  'DD1083' 'DD1082' 'DD1083A' 'DD1086A' 'DD1091' 'DD1095' 'DD1097' 'DD1098'
#  'DD1099' 'DD1100' 'DD1097A' 'DD1101' 'DD1102' 'DD1103' 'DD1105' 'DD1104'
#  'DD1106' 'DD1107' 'DD1104A' 'DD1108' 'DD1110' 'DD1111' 'DD1112' 'DD1113'
#  '\x1a']

def n_holes(df):
    return len(df.HOLEID.unique())


def extract_holes(HOLEID):
    import pandas as pd
    import os

    if os.path.isfile('%s.csv'%HOLEID):
        subset = pd.read_csv('%s.csv'%HOLEID)

    else:
        geo = pd.read_csv('Complete_Geophysics.csv')
        hole = geo.query('HOLEID == "%s"'%HOLEID)
        subset = hole[['DEPTH','DENB','DENL','GRDE', 'LSDU']].sort('DEPTH')
        subset.to_csv('%s.csv'%HOLEID, index = False)

    return subset


def extract_peak_loc(hole, holeID):

    response_th = 1000

    # window_size = 1# meters
    window_size = 4# meters

    peak_flag = [0]*len(hole['DEPTH'])

    seam_list = [] # list of holes

    nRows = len(hole)

    coal_seam_bound_start = False
    for i,depth in enumerate(hole['DEPTH']):

        if i%200 == 0:
            print( '%s progress: %i/%i'%(holeID, i, nRows))

        # if depth > 80: # start looking at 80 meters
        if depth > 90: # start looking at 80 meters
            # get the indexes within the scan window, this is very slow, maybe faster query?
            window_idx = hole[(hole['DEPTH'] >= (depth - window_size/2.0)) & ((hole['DEPTH'] <= (depth + window_size/2.0)))].index.tolist()


            bottom =depth -  window_size/2.0
            top = depth + window_size/2.0

            # atv = hole.query('DEPTH > @bottom and DEPTH <= @top')['LSDU'].mean()

            # print hole['LSDU'][window_idx].mean()
            if hole['LSDU'][window_idx].mean() > response_th:
            # if hole.query('DEPTH > @bottom and DEPTH <= @top')['LSDU'].mean() > response_th:
                peak_flag[i] = 10000


                if coal_seam_bound_start == False:
                    seam_prop = [depth]
                    coal_seam_bound_start = True
                    # print 'ich bin hier'

            elif coal_seam_bound_start == True:
                # print 'ich bin wieder hier'
                seam_prop.append(depth) # add the end depth
                seam_list.append(seam_prop) # add hole [start end] to hole list
                seam_prop = [] # reset hole [start end]
                coal_seam_bound_start = False

            # if  hole['LSDU'][i] > response_th:
            #     peak_flag[i] = 10000


    hole['Flag'] = peak_flag

    total_depth = depth
    coal_depth = 0
    for coal_seam in seam_list:
        coal_depth += (coal_seam[1] - coal_seam[0])
    coal_percentage = coal_depth/total_depth

    # write to txt
    f = open('%s.txt'%holeID, 'w')
    f.write('Coal Percentage: %s\n'%coal_percentage)
    f.write('Coal Depth: %s\n'%coal_depth)
    f.write('Total Depth: %s\n'%total_depth)
    f.write('Seam Structure: %s'%seam_list)
    f.close()

    # write to json
    out_dict = {}
    out_dict['Coal Percentage'] = coal_percentage
    out_dict['Coal Depth'] = coal_depth
    out_dict['Total Depth'] = total_depth
    out_dict['Seam Structure'] = seam_list
    import json
    with open('%s.json'%holeID,'w') as fp:
        json.dump(out_dict, fp)


    return seam_list


def extract_seams(bore_id, seam_list = []):
    import numpy as np
    # depth = seam_list[0][0]
    print('Extracting {}'.format(bore_id))
    top = 100
    bottom = 400
    window_size = bottom-top
    mid = (top+bottom)/2.0
    bin_size = 0.1
    try:
        df_data = john.get_data(boreid = bore_id, centre_point = mid, window_size = window_size, bin_width = bin_size)
    except Exception as e:
        print('Exception raised! {}'.format(e))
        return

    df_data.to_csv('%s_cleandata.csv'%bore_id, ignore_index=True)

    return df_data



    # ['ADEN', 'GRDE', 'DENB', 'LSDU', 'acoustic']


# hole data exist in both geophysics and acoustic scanner
# ['DD0541' 'DD0542' 'DD0551'
#  'DD0980A' 'DD0989' 'DD1000' 'DD0991' 'DD1006' 'DD1005' 'DD1010' 'DD0992'
#  'DD1012' 'DD1013' 'DD1014' 'DD1070' 'DD1073' 'DD1077' 'DD1080' 'DD1081'
#  'DD1083' 'DD1082' 'DD1083A' 'DD1086A' 'DD1091' 'DD1095' 'DD1097' 'DD1098'
#  'DD1099' 'DD1100' 'DD1097A' 'DD1101' 'DD1102' 'DD1103' 'DD1105' 'DD1104'
#  'DD1106' 'DD1107' 'DD1104A' 'DD1108' 'DD1110' 'DD1111' 'DD1112' 'DD1113'
#  '\x1a']


if __name__ == '__main__':

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    holeId = [
    'DD1097',
    'DD1098',
    'DD1099',
    'DD1100',
    'DD1101',
    'DD1102',
    'DD1103', 'DD1104', 'DD1105', 'DD1106',
    'DD1107', 'DD1108',
    'DD0541',
    'DD0542',
    'DD0551',
    'DD0980A',
    'DD0989',
    'DD0991',
    'DD0992',
    'DD1000',
    'DD1005',
    'DD1006',
    'DD1010',
    'DD1012',
    'DD1013',
    'DD1014']

    # extract_seams(bore_id = holeID, seam_list = hole_boundaries)
    result = pd.concat([extract_seams(bore_id=h) for h in holeId], ignore_index=True)
    result.to_csv('all_data.csv', index=False)





