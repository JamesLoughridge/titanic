from pandas import DataFrame


def find_missing_values(df: DataFrame):
    return {x : df.loc[:, x].isna().sum() for x in df.columns.tolist()}


def find_title(df: DataFrame):
    return df.loc[:, 'Name'].str.extract(' (\w+\.)', expand=False)


