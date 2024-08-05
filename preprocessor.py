


def preprocess(df, region_df):
    # Filter for Summer Olympics
    df = df[df['Season'] == 'Summer']

    # Merge with region_df
    df = df.merge(region_df, on='NOC', how='left')

    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # One hot encoding medals
    df['Gold'] = df['Medal'].apply(lambda x: 1 if x == 'Gold' else 0)
    df['Silver'] = df['Medal'].apply(lambda x: 1 if x == 'Silver' else 0)
    df['Bronze'] = df['Medal'].apply(lambda x: 1 if x == 'Bronze' else 0)

    return df
