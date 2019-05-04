from pandas import DataFrame


def find_title(df: DataFrame):
    return df.loc[:, 'Name'].str.extract(' (\w+\.)', expand=False)
