import os

CUR_LOC = os.getcwd()
CSV_DATA_LOC = os.path.join(CUR_LOC, 'data', 'SBC001.csv')

TEST_SPLIT_PERCENTAGE = 0.2
RANDOM_STATE = 42
RANDOM_CV_SPLIT = 5
EMPTY_TOKEN = 'eeemmmppptttyyy'