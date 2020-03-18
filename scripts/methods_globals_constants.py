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
                                       Index 0 = Counts, index 1 = mean, index 2 = median 
    
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

def fillna_average_by_target_column(row, avg_dict, target_col, effected_col):
    """
    When given a row of a dataframe, this method will use the target column to fill nan values with 
    the average associated with the catagorical values in the effected column. 
    
    Parameters
    ----------
    row 			: [Pandas Series] : A row of a dataframe.
    avg_dict 		: [Dictionary] 	  : A dictionary of the average of the catagorical values in the target column of the dataframe
    target_col 		: [int] 		  : index of where the catagorical target is to base means on
    effected_col 	: [int] 		  : index of where the effected column is in the dataframe
    
    Returns
    -------
    a dataframe row with effect column value changed if it is null
    """
    try:
        if np.isnan(row[effected_col]):      
            row[effected_col] = np.round(avg_dict[row[target_col]], 2)
    except:
        pass #row[effected_col] = "???"
        
    return row
	
	