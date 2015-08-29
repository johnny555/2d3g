__author__ = 'Admin'


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

    geo = pd.read_csv('Complete_Geophysics.csv')

    hole = geo.query('HOLEID == "%s"'%HOLEID)

    subset = hole[['DEPTH','DENB','DENL','GRDE', 'LSDU']].sort('DEPTH')

    subset.to_csv('%s.csv'%HOLEID, index = False)


def extract_peak_loc(hole):

    response_th = 1000

    window_size = 1# meters

    peak_flag = [0]*len(hole['DEPTH'])

    hole_list = [] # list of holes

    nRows = len(hole)

    coal_seam_bound_start = False
    for i,depth in enumerate(hole['DEPTH']):

        if i%200 == 0:
            print 'progress: %i/%i'%(i, nRows)

        if depth > 80: # start looking at 80 meters

            # get the indexes within the scan window, this is very slow, maybe faster query?
            window_idx = hole[(hole['DEPTH'] >= (depth - window_size/2.0)) & ((hole['DEPTH'] <= (depth + window_size/2.0)))].index.tolist()

            # print hole['LSDU'][window_idx].mean()
            if hole['LSDU'][window_idx].mean() > response_th:
                peak_flag[i] = 10000

                if coal_seam_bound_start == False:
                    hole_prop = [depth]
                    coal_seam_bound_start = True
                    # print 'ich bin hier'

            elif coal_seam_bound_start == True:
                # print 'ich bin wieder hier'
                hole_prop.append(depth) # add the end depth
                hole_list.append(hole_prop) # add hole [start end] to hole list
                hole_prop = [] # reset hole [start end]
                coal_seam_bound_start = False

            # if  hole['LSDU'][i] > response_th:
            #     peak_flag[i] = 10000

    hole['Flag'] = peak_flag

    return hole_list


if __name__ == '__main__':

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # extract_holes(HOLEID = 'DD0509')
    # extract_holes(HOLEID = 'DD1113')


    df_hole = pd.read_csv('DD0509.csv')
    # df_hole = pd.read_csv('DD1113.csv')


    print df_hole.fillna(0)

    print extract_peak_loc(df_hole)

    df_hole.plot(x = 'DEPTH', y = ['LSDU','Flag'])
    plt.show()




