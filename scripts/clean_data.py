clean_df = bank_df.copy()

clean_df.columns = clean_df.columns.str.replace(' ', '_')

# Remove all rows where all the columns are nan/null. Removes ~ 500 observations
clean_df.dropna(axis=0, how='all', inplace=True)

# Remove all observation with credit scores higher than 900. These an enigma borrower and only account for ~4% of the data
_ = clean_df[clean_df['Credit_Score'] <= 900].index
clean_df.drop(_, inplace=True) 

# There were too many missing values in these columns. We removed both to perserve as much data as possible.
clean_df.drop(['Credit_Score', 'Annual_Income'], axis=1, inplace=True) 

# Dropiing to nan value of year in current job. There are ~ 1056 which is ~ 4.45% of the remaining
_ = clean_df[clean_df['Years_in_current_job'].isna()].index
clean_df.drop(_, inplace=True) 

# Fill in all nan values for "months since last delinquent" with the mean of the catagorical column Purpose
_ = clean_df.groupby('Purpose').mean()['Months_since_last_delinquent'] # A temporary dictionary like object. also called a pandas series

clean_df = clean_df.apply(lambda x : fillna_average_by_target_column(row=x, 
                                                          avg_dict=_, 
                                                          target_col=7, 
                                                          effected_col=10),axis=1)

# Drop the remaining nan values in Maximun open credit, bankruptcies, and tax liens
clean_df.dropna( subset=['Maximum_Open_Credit', 'Bankruptcies', 'Tax_Liens'], axis=0, inplace=True)

#Drop all loans amount with 9999999999. This is too extreme 
_ = clean_df.loc[clean_df['Current_Loan_Amount'] >= 99999999.0].index
clean_df.drop(index=_, inplace=True)

clean_df.drop(['Loan_ID', 'Customer_ID'], axis=1, inplace=True)