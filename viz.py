__author__ = 'Admin'


def group_bands(depth, coal_labels, holeID):

    coal_label_list = ['RU', 'R', 'R1', 'R2', 'RO', 'RL', 'MU', 'MM', 'MML', 'LN', 'TR', 'TRL', 'PS', 'PSL', 'P2', 'P2U',
                       'P2LA', 'P2LB', 'BA', 'G1', 'G2', 'G34', 'G3', 'G4', 'G56', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
                       'G11', 'BGA', 'BGB' 'BGC', 'BG', 'HEU', 'HEL', 'CN', 'FH', 'FL', 'MAC', 'PX', 'PU', 'PM', 'P',
                       'PL', 'AQ', 'AQL', 'T1UA', 'T1UB', 'T1U', 'T1M', 'T1L', 'T2', 'C1U', 'C1', 'C1L', 'CM', 'CM',
                       'CS', 'C2', 'GUS' 'GU', 'GC', 'GL', 'BN']





    deltaD = depth[1]-depth[0]

    dist_from_last_coal_seam = float('inf')

    seam_prop = []
    seam_list = []


    for i, label in enumerate(coal_labels):

        if label in coal_label_list:
            if (dist_from_last_coal_seam == float('inf')) or (dist_from_last_coal_seam is not 0):
                dist_from_last_coal_seam = 0
                seam_prop.append(depth[i])


        elif (label not in coal_labels) and (dist_from_last_coal_seam == 0):
            seam_prop.append(depth[i])
            seam_list.append(seam_prop)

            seam_prop = []

            dist_from_last_coal_seam += deltaD



    print seam_list
    allowable_dist = 20
    group_no = 1
    nSeam = len(seam_list)
    group_list = [group_no]
    for iSeam in range(nSeam-1):

        if seam_list[iSeam+1][0] - seam_list[iSeam][1] > allowable_dist:
            group_no += 1

        group_list.append(group_no)

    print group_list


    out_list = []

    for i, seam in enumerate(seam_list):
        out_dict = {}
        out_dict['top'] = seam[0]
        out_dict['bot'] = seam[1]
        out_dict['type'] = group_list[i]
        out_list.append(out_dict)


    import json
    with open('%s_seaminfo.json'%holeID,'w') as fp:
        json.dump(out_list, fp)

    return seam_list



def display_acoustic(df, holeID, useful_features = ['ADEN', 'BRDU', 'CADE', 'CODE', 'DENB', 'DENL', 'GRDE', 'LSDU']):
    import matplotlib.pyplot as plt

    feature_list = df.columns

    # print feature_list

    accoustic_features = []

    for feature in feature_list:
        if 'ATV_AMP' in feature:
            accoustic_features.append(feature)

    # print accoustic_features

    accoustic_scan = df[accoustic_features].values

    coal_label_list = ['RU', 'R', 'R1', 'R2', 'RO', 'RL', 'MU', 'MM', 'MML', 'LN', 'TR', 'TRL', 'PS', 'PSL', 'P2', 'P2U',
                       'P2LA', 'P2LB', 'BA', 'G1', 'G2', 'G34', 'G3', 'G4', 'G56', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10',
                       'G11', 'BGA', 'BGB' 'BGC', 'BG', 'HEU', 'HEL', 'CN', 'FH', 'FL', 'MAC', 'PX', 'PU', 'PM', 'P',
                       'PL', 'AQ', 'AQL', 'T1UA', 'T1UB', 'T1U', 'T1M', 'T1L', 'T2', 'C1U', 'C1', 'C1L', 'CM', 'CM',
                       'CS', 'C2', 'GUS' 'GU', 'GC', 'GL', 'BN']


    # useful_features = ['ADEN', 'BRDU', 'CADE', 'CODE', 'DENB', 'DENL', 'GRDE', 'LSDU']
    nPlots = len(useful_features) + 2

    iPlot = 1
    for feature in useful_features:
        plt.subplot(1,nPlots,iPlot)
        plt.plot(df[feature].values, df['DEPTH'].values)
        plt.ylim(min(df['DEPTH'].values), max(df['DEPTH'].values))
        # plt.title(feature)
        plt.gca().invert_yaxis()
        plt.axis('off')
        iPlot += 1

    plt.subplot(1,nPlots,iPlot)
    plt.imshow(accoustic_scan,  aspect='auto')
    plt.ylim(1, len(accoustic_scan))
    plt.title('Acoustic scan')
    plt.gca().invert_yaxis()
    iPlot += 1

    plt.subplot(1,nPlots,iPlot)
    # plt.plot([l in coal_label_list for l in df['LABELS'].values], df['DEPTH'].values)
    x1 = [l in coal_label_list for l in df['LABELS'].values]
    # x2 = [2 if x == True else 0 for x in x1]
    x2 = [0]*len(x1)
    y1 = df['DEPTH'].values
    y2 = y1
    plt.plot((x1, x2), (y1, y2), 'k-')


    plt.ylim(min(df['DEPTH'].values), max(df['DEPTH'].values))
    plt.title('Label')
    plt.gca().invert_yaxis()
    iPlot += 1
    # plt.imsave('%s.png'%holeID)
    plt.savefig('%s.png'%holeID)

    group_bands(df['DEPTH'].values, df['LABELS'].values, holeID = holeID)

    plt.show()


if __name__ == '__main__':

    import pandas as pd
    import matplotlib.pyplot as plt





    # holeID = [ 'DD1102']
    #
    # # extract_seams(bore_id = holeID, seam_list = hole_boundaries)
    # [extract_seams(bore_id=h) for h in holeID]

    holeID = 'DD1097'
    holeID = 'DD1098'
    holeID = 'DD1099'
    # holeID = 'DD1100'
    # holeID = 'DD1102'



    shit = [   'DD1101','DD1106' ]

    done = [   ]



    holeId = ['DD1097',
    'DD1098',
    'DD1099',
    'DD1100',
    'DD1102',

'DD1104', 'DD1105' ,'DD1107', 'DD1108','DD1103',

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

    for holeID in holeId:
        df = pd.read_csv('dats/%s_cleandata.csv'%holeID)
        display_acoustic(df, holeID)