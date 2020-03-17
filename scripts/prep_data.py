prep_df = clean_df.copy()
prep_df.reset_index(drop=True, inplace=True)

# Label Encoding term with label encoding because it is binary
le = LabelEncoder()
prep_df['Term'] = le.fit_transform(prep_df['Term']) 

# One hot encoding all other object columns

ohe = OneHotEncoder(drop="first")
cat_var = prep_df.select_dtypes(include="object")
array_to_df = ohe.fit_transform(cat_var).toarray()  # Array values of the transformed columns
encoded = pd.DataFrame(array_to_df, columns=ohe.get_feature_names(cat_var.columns))  # Creating a pandas dataframe
prep_df = prep_df.join(encoded, how="left")

# Getting ride of all object columns for the model
_ = prep_df.select_dtypes(include="object").columns
prep_df.drop(columns=_, axis=1, inplace=True)

# Fix column names
prep_df.columns = prep_df.columns.str.replace(' ', '_')

# Fixing class imbalance
majority_df = prep_df[prep_df['Loan_Status_Fully_Paid']==1]

minority_df = prep_df[prep_df['Loan_Status_Fully_Paid']==0]
minority_df = resample(minority_df, replace=True, n_samples=13200, random_state=123)

prep_df = pd.concat([majority_df, minority_df])

# Preparing the X,y train test data
X = prep_df.drop(columns='Loan_Status_Fully_Paid', axis=1)
y = prep_df['Loan_Status_Fully_Paid']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2)