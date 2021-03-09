# preprocessing.py

import config
import pandas as pd
import numpy as np
import datetime
import argparse
import os
from operator import attrgetter


def preprocess_retail_df(country, out):
    """Preprocesses the original retail file

    Args:
        country (str): a country name(eg. 'United Kingdom' , or 'all', to include all)
        out (str): name of the csv file to save
    """
    df = pd.read_csv(config.RETAIL_FILE)
    if country == 'all':
        pass;
    else:
        df = df.loc[df['Country'] == country]   
    df.loc[:,'customer_id'] = df['CustomerID'].apply(lambda x: str(int(x)) if pd.notna(x) else np.nan)
    df = df.dropna(subset = ['customer_id'])
    df.loc[:,'date'] = df['InvoiceDate'].apply(lambda x: datetime.datetime.strptime(x, '%m/%d/%Y %H:%M'))
    df = df.sort_values(by='date')
    df.loc[:,'revenue'] = df['UnitPrice']*df['Quantity']
    df.loc[:,'order_month'] = df['date'].dt.to_period('M')
    # first purchase month as determinant of the cohort, note the transform in groupby 
    df['cohort'] = df.groupby('customer_id')['date'].transform('min').dt.to_period('M')
    df.to_csv(os.path.join(config.INPUT_DIR, f"{out}.csv"), index=False)


if __name__ == "__main__":
    #initialize ArgumentParser class of argparse
    parser = argparse.ArgumentParser()
    # add the different arguments you need and their type

    parser.add_argument(
        # if you want to specify all the df you should specify 'all'
        "--country",
        type=str,
        default='United Kingdom'
	)
    parser.add_argument(
        # if you want to specify all the df you should specify 'all'
        "--out",
        type=str,
        default='df_modified'
    )	
	
	# read the arguments from the command line
    args = parser.parse_args()
    preprocess_retail_df(country = args.country, out=args.out)