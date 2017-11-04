import numpy as np
import pandas as pd



def max_faciliity_id(df):
    '''
    INPUT: DataFrame
    OUTPUT: int

    Write a query on the input data frame that returns the maximum facility id.
    '''
    # solo_col = df['Facility ID']
    # solo_col = solo_col.sort_values(ascending = False)
    # solo_col = solo_col.reset_index(drop = True)
    # return solo_col[0]
    return df['Facility ID'].max()


def number_of_censuses(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns count of how many censuses were reported
    for the specified facility id
    '''
    # ids = df['Facility ID']
    # mask = ids.isin([facility_id])
    # selection = ids[mask]
    # number = ids[mask].count()
    # return number
    return len(df[(df['Facility ID'] == facility_id)])


def earliest_census_date(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns the earliest census date for the
    specified facility id
    Note: The dates are currently stored as strings, not date objects
    Hint: pd.to_datetime is very useful
    '''
    selection_data = df[(df['Facility ID'] == facility_id)]
    selection_series = selection_data['Bed Census Date']
    dates = selection_series.map(pd.to_datetime)
    return dates.min()


def beds_top_ten(df, facility_id):
    '''
    INPUT: DataFrame, int
    OUTPUT: date
    Write a pandas query that returns the ten census dates with the highest
    number of available beds for the nursing home with the specified facility id
    REQUIREMENTS:
    Do a filter followed by a sort rather than a sort followed by a merge.
    '''
    #filter
    selection_data = df[(df['Facility ID'] == facility_id)]
    sorted_data = selection_data.sort_values('Available Pediatric Beds', ascending = False)
    date_strings = sorted_data['Bed Census Date'].head(10)
    dates = date_strings.map(pd.to_datetime)
    return dates


if __name__ == '__main__':
    df = pd.read_csv('../data/beds.csv', low_memory = False)
    #print max_faciliity_id(df)
    #print number_of_censuses(df, 9198)
    #print earliest_census_date(df, 9198)
    print beds_top_ten(df, 9198)
