__author__ = 'Admin'



def coal_classification(holeID):

    import pandas as pd
    import numpy as np
    import sklearn
    import sklearn.preprocessing as pre
    import sklearn.pipeline as pipe
    import sklearn.decomposition as decomp
    import sklearn.svm as svm
    import sklearn.cross_validation as crossval
    import sklearn.metrics as metrics


    cleaned = pd.read_csv('dats/%s_cleandata.csv'%holeID)

    cleaned.set_index('DEPTH', inplace=True)

    cols = cleaned.columns.tolist()
    cols.remove('Unnamed: 0')
    cleaned = cleaned[cols]

    target = np.logical_not(cleaned.LABELS.isnull())
    print(target.sum())
    target.shape


    cols.remove('LABELS')
    cols.remove('LABELS_ROCK_TYPE')

    imputer = pre.Imputer()
    scalar = pre.StandardScaler()
    n_components=20
    svc = svm.SVC()

    pca = decomp.PCA(n_components=n_components, whiten=True)

    tx = pipe.make_pipeline(imputer, pca)

    x_train, x_test, y_train, y_test = crossval.train_test_split(cleaned[cols], target, test_size=0.4)

    print x_train
    print y_train
    result = tx.fit_transform(x_train)

    svc.fit(result, y_train)
    pred = svc.predict(tx.transform(x_test))

    metrics.roc_auc_score(pred, y_test)

    pre.scale(cleaned[cols].fillna(0))

    print('F1 test validation score {}'.format(metrics.f1_score(pred, y_test)))


def feature_selection(holeID):

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import sklearn.preprocessing as pre
    from sklearn.feature_selection import SelectKBest
    from sklearn.feature_selection import chi2
    from sklearn.feature_selection import SelectPercentile
    from sklearn.feature_selection import f_classif

    cleaned = pd.read_csv('dats/%s_cleandata.csv'%holeID)
    # cleaned = pd.read_csv('dats/all_data.csv')

    cleaned.set_index('DEPTH', inplace=True)

    target = np.logical_not(cleaned.LABELS.isnull())

    cols = cleaned.columns.tolist()
    # cols.remove('Unnamed: 0')
    cols.remove('LABELS')
    cols.remove('LABELS_ROCK_TYPE')

    cleaned = cleaned[cols]

    # normalise column by col
    cleaned = (cleaned - cleaned.mean()) / (cleaned.max() - cleaned.min())

    shit = []
    for col in cols:
        if cleaned[col].isnull().sum() == len(cleaned): # find column full of nans
            # print col
            shit.append(col)

    non_empty_cols = list(set(cols).difference(set(shit)))
    # cleaned.fillna(0)


    cols = non_empty_cols
    X, y = cleaned[cols], target


    imputer = pre.Imputer(missing_values='NaN', strategy='mean')
    X = imputer.fit_transform(X)


    # blah, pval = chi2(X, y) # x can't have negative values
    blah, pval = f_classif(X,y)

    useful_feat = []
    for i, feat in enumerate(cols):
        # if scores[i] == float('inf'):
        if pval[i] == 0:
            print feat, pval[i]

            useful_feat.append(feat)

    return useful_feat




if __name__ == '__main__':
    import pandas as pd
    from viz import display_acoustic
    # holeID = 'DD1103'
    holeID = 'DD1013'
    # holeID = 'DD0541'
    # holeID = 'DD0542'
    # holeID = 'DD0551'
    # holeID = 'DD0980A'
    holeID = 'DD0989'
    # holeID = 'DD0991'
    # holeID = 'DD0992'
    # holeID = 'DD1000'
    # holeID = 'DD1005'
    # holeID = 'DD1006'
    # holeID = 'DD1010'
    # holeID = 'DD1012'
    # holeID = 'DD1013'
    # holeID = 'DD1014'

    # coal_classification(holeID)


    useful_feat = feature_selection(holeID)

    df = pd.read_csv('dats/%s_cleandata.csv'%holeID)


    display_acoustic(df, holeID, useful_feat[-12:-1])




