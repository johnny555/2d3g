__author__ = 'Admin'


def display_acoustic(df):
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


    useful_features = ['ADEN', 'BRDU', 'CADE', 'CODE', 'DENB', 'DENL', 'GRDE', 'LSDU']
    nPlots = len(useful_features) + 2

    iPlot = 1
    for feature in useful_features:
        plt.subplot(1,nPlots,iPlot)
        plt.plot(df[feature].values, df['DEPTH'].values)
        plt.ylim(min(df['DEPTH'].values), max(df['DEPTH'].values))
        plt.title(feature)
        plt.gca().invert_yaxis()
        iPlot += 1

    plt.subplot(1,nPlots,iPlot)
    plt.imshow(accoustic_scan,  aspect='auto')
    plt.ylim(1, len(accoustic_scan))
    plt.title('Acoustic scan')
    plt.gca().invert_yaxis()
    iPlot += 1

    plt.subplot(1,nPlots,iPlot)
    plt.plot([l in coal_label_list for l in df['LABELS'].values], df['DEPTH'].values)
    x1 = [l in coal_label_list for l in df['LABELS'].values]
    x2 = [x+1 if x == True else x  for x in x1]
    y1 = df['DEPTH'].values
    y2 = y1
    plt.plot((x1, x2), (y1, y2), 'k-')


    plt.ylim(min(df['DEPTH'].values), max(df['DEPTH'].values))
    plt.title('Label')
    plt.gca().invert_yaxis()

    plt.show()




if __name__ == '__main__':

    import pandas as pd
    import matplotlib.pyplot as plt

    # holeID = 'DD0541'
    # holeID = 'DD0542'
    # holeID = 'DD0551'
    # holeID = 'DD0980A'
    # holeID = 'DD0989'
    # holeID = 'DD0991'
    # holeID = 'DD0992'
    # holeID = 'DD1000'
    # holeID = 'DD1005'
    # holeID = 'DD1006'
    # holeID = 'DD1010'
    # holeID = 'DD1012'
    # holeID = 'DD1013'
    # holeID = 'DD1014'

    # holeID = 'DD1097'
    # holeID = 'DD1098'
    # holeID = 'DD1099'
    # holeID = 'DD1100'
    ## holeID = 'DD1101'
    # holeID = 'DD1102'

    # holeID = [ 'DD1102']
    #
    # # extract_seams(bore_id = holeID, seam_list = hole_boundaries)
    # [extract_seams(bore_id=h) for h in holeID]

    holeID = 'DD1097'
    holeID = 'DD1098'
    holeID = 'DD1099'
    holeID = 'DD1100'
    holeID = 'DD1102'
    df = pd.read_csv('%s_cleandata.csv'%holeID)
    display_acoustic(df)