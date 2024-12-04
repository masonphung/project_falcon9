# Define a function to report missing data
def report_missing(df):
    """
    Create a dataframe, then calculate the number of null and blank value.
    
    Parameter:
    df (DataFrame)
        The dataframe used to check for missing values
    
    Return:
    completed_report (DataFrame)
        The report table including the number of null, blank values and their percentage in total
    """
    # Total observation count
    total_obs = df.shape[0]
    # Create a dataframe
    missing = pd.DataFrame()
    # Total nulls
    missing['null_count'] = df.isnull().sum()
    # Total blank value
    missing['blank_count'] = [df[df[c].astype(str) == ""][c].count() for c in df.columns]
    # Total missing value
    missing['total_missing'] = missing.sum(axis = 1)
    # Report missing percentage
    missing['null_percent'] = round(100* (missing['null_count']/ total_obs), 2)
    missing['blank_percent'] = round(100* (missing['blank_count']/ total_obs), 2)
    missing['total_missing_percent'] = round(100* (missing['total_missing']/ total_obs), 2)
    
    completed_report = missing.sort_values(
        by = 'total_missing_percent',
        ascending = False
    )
    return completed_report

# Function used to extract column name
def extract_column_from_header(row):
    """
    This function returns the column name from the HTML table cell,
    clean them by removing links, line breaks and superscript tags.
    
    Parameter: 
    row: The element of a table data cell extracts extra row
    
    Return:
    column_name: Cleaned header cell to be used as column name
    """
    if (row.br):
        row.br.extract()
    if row.a:
        row.a.extract()
    if row.sup:
        row.sup.extract()
        
    colunm_name = ' '.join(row.contents)
    
    # Filter the digit and empty names
    if not(colunm_name.strip().isdigit()):
        colunm_name = colunm_name.strip()
        return colunm_name    
    
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
import matplotlib_inline as plt
import seaborn as sns
    
# Define a function to plot confusion matrix
def plot_confusion_matrix(y_test,y_pred_test):
    """
    Plot the confusion matrix to evaluate the performance of the model
    
    Parameters
    - y_test (Series): Contains the target values for the test set.
    - y_pred_test (Series): Predicted target variable based on the ML model
    
    Return:
        Confusion matrix heat map
    """

    matrix = confusion_matrix(y_test, y_pred_test)
    ax = plt.subplot()
    sns.heatmap(
        matrix, 
        fmt = 'd', # integer format for labels
        annot = True, # annot = True to annotate cells
        ax = ax
    )
    ax.set_xlabel('Predicted labels')
    ax.set_ylabel('True labels')
    ax.set_title("Confusion Matrix")
    plt.show()
    
    
    
# Define a model to fit data into the model then predict
def modeling(model, X_train, y_train, X_test, y_test):
    """
    Trains a machine learning model on training data, then evaluates and compares its performance on the test dataset.

    Parameters:
    - model: The machine learning model to be trained and evaluated. Must have fit and predict methods.
    - X_train (dataframe): Contains the desired features for the training set.
    - y_train (Series): Contains the target values for the training set.
    - X_test (dataframe): Contains the desired features for the test set.
    - y_test (Series): Contains the target values for the test set.

    The function fits the model on the training dataset. 
    It then makes predictions on the test dataset to evaluate the model's performance. 
    Accuracy scores and classification report both sets are printed to provide insights into the model's effectiveness. 

    Returns:
    - model: The trained model instance.
    - accuracy (float): Accuracy score of the model on the test set.
    """
    # Fit the model
    model.fit(X_train, y_train)
    # Predict with test data
    y_predicted = model.predict(X_test)
    y_predicted_train = model.predict(X_train)
    
    # Calculate accuracy score
    accuracy = accuracy_score(y_test, y_predicted)
    accuracy_train = accuracy_score(y_train, y_predicted_train)
    pred_prob = model.predict_proba(X_test)
    
    # Print results
    print("Training Set Accuracy = {:.5f}".format(accuracy_train))
    print("Test Set Accuracy = {:.5f}".format(accuracy), '\n')

    print("Training Set Classification Report:")
    print(classification_report(y_train, y_predicted_train, digits = 5))
    
    print("Test Set Classification Report:")
    print(classification_report(y_test, y_predicted, digits = 5))
    plot_confusion_matrix(y_test, y_predicted)
    
    return model, accuracy, pred_prob 