def feature_extract_mean_count_median(df, columns, target, return_trig=[True, True, True]):
    """
    Using a dataframe this method can get the mean, median, and count of any columns specified in relation 
    to a target variable. The columns must be catagorical 
    
    Parameters
    ----------
    df          : [Pandas Dataframe] : Dataframe/Data.
    columns     : [List of Strings]  : list of catagory column names
    target      : [String]           : index of where the target column is in the dataframe
    return_trig : [List of Boolean]  : triggers for what extractions to  perform.
                                       Index 1 = Counts, index 2 = mean, index 3 = median 
    
    Returns
    -------
    a dataframe with new features mean, median, and count for all catagorical columns and specfied triggers
    """
    
    for name in columns:
        if return_trig[0] == True:
            _ =  df[name].value_counts()
            df[f'{name}_Count'] = df[name].map(lambda value: _[value])
        if return_trig[1] == True:
            _ =  df.groupby(name).mean()[target]
            df[f'{name}_Mean'] = df[name].map(lambda value: _[value])
        if return_trig[2] == True:
            _ =  df.groupby(name).median()[target]
            df[f'{name}_Median'] = df[name].map(lambda value: _[value])

			