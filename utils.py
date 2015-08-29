__author__ = 'jvial'
import pandas as pd

lith = pd.read_csv('corrected_lithology.csv')

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
