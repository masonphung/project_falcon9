# **Mini Project: Data Analysis and Prediction of SpaceX Falcon9 rocket landing**

## INTRODUCTION

> *Space Exploration Technologies Corp. or SpaceX is an American spacecraft manufacturer, popular for their successful mission in sending a spacecraft and astronauts to the International Space Station. They are also well-known for their [VTVL](https://en.wikipedia.org/wiki/VTVL) rocket launches , in which rockets can land and be resued, thus save a huge amount of launching cost for the company.*
>
> *One of SpaceX's most popular rocket - the Falcon 9, have landed and reflown [more than 200 times](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches) . The rocket was advertised on its website with a launch cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch.*

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/crash.gif)

*We are working at a business in the aerospace industry who are developing a space rocket and are researching different rocket technologies and their competitiors.*

*In this project, we will collect & analyze past launches data of the Falcon 9 rockets then try to predict the outcome of future launches using different Machine Learning models. The main purpose is to find which factor contributes to the success of each flight and to build a Machine Learning model that can predict the outcome of a rocket launch.*

## IMPORTANT !!

- This original questions & problem sets are initally parts of the IBM Data Science Specialization capstone project.
- After completing the base project, I created a new personal version, the dashboard app as well as the machine learning section by adding extra integrations, new features and customization (details below)

## THE PROJECT COVERS

- `Python` programming
- Data collection: API data collection w. `requests` and webscraping w. `BeautifulSoup`
- Data analysis with SQL using local database `mySQL` and `SQLalchemy` toolkit for python
- Exploratory analysis by visualization with `matplotlib` and `seaborn`
- Building an interactive dashboard using `dash` and `plotly.express`
- Train classification models (Logistic Regression, SVM, Decision Tree, kNN, XGBoost, Multi-layer perceptron) with hyperparameter tuning to predict of future landing outcomes with `scikit-learn`

![image](https://github.com/masonphung/project_falcon9/assets/131331827/11c3e7ac-fe07-4861-93fc-2dae37f74940)

## ADDED FEATURES (COMPARED TO THE ORIGINAL 'SUPPOSED-TO-DO' WORK)

### Notebooks

- Removed lengthy features, convert repeated functions into predefined functions.
- Added step explanations, result comments to each section.
- Set up and worked with SQL in a local MySQL database (Originally IBM Skills Network Lab Environment).
- Added new ML models with correlation-based features selection and hyperparameter tuning.
- Estimate the models' performance with classification report, ROC curve and AUC score.

### Dashboard app

- Styled with `dash_bootstrap_components`, external css, responsive customized layout.
- Added multiple-inputs callbacks.
- Added extra plots, statistic summary, global attribute selection and year slider.

## <span style="color:#ff9933">LATEST UPDATES: ver 2.1</span>
- Refine Machine Learning section: 
    - Consider imbalanced data: Add stratification.
    - Improve feature selection.
    - Refine existed models.
    - Add XGBoost and Multi-layer perceptron models.
    - Add ROC curve and AUC score to determine the performance of the models.
    - Change `Conclusion` based on the new results.
- Modify `Part 5. Discussion` based on the new results.
