import pandas as pd
from sklearn.linear_model import LinearRegression

def load_data(file):
    data = pd.read_csv(file)

    # tidy up the data
    # drop some less useful columns
    data.drop('Alley', axis=1, inplace=True)
    data.drop('Fence', axis=1, inplace=True)
    data.drop('Utilities', axis=1, inplace=True)

    # fix up some mixed format numeric cols
    data[data['LotFrontage'].isnull()] = 0 # assume no lot == 0 size



    return data




if __name__ == '__main__':
    train = load_data('./data/train.csv')

    print(train)