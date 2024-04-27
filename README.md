# **Mini Project: Data Analysis and Prediction of SpaceX Falcon9 rocket landing**

## INTRODUCTION

> *Space Exploration Technologies Corp. or SpaceX is an American spacecraft manufacturer, popular for their successful mission in sending a spacecraft and astronauts to the International Space Station. They are also well-known for their [VTVL](https://en.wikipedia.org/wiki/VTVL) rocket launches , in which rockets can land and be resued, thus save a huge amount of launching cost for the company.*
>
> *One of SpaceX's most popular rocket - the Falcon 9, have landed and reflown [more than 200 times](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches) . The rocket was advertised on its website with a launch cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch.*

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/crash.gif)

## IMPORTANT !!

- This original questions & problem sets are initally parts of the IBM Data Science Specialization capstone project.
- After completing the base project, I created a new personal version, the dashboard app as well as the machine learning section by adding extra integrations, new features and customization (Details below)

## THE PROJECT COVERS

- `Python` programming
- Data collection: API data collection w. `requests` and webscraping w. `BeautifulSoup`
- Data analysis with SQL using local database `mySQL` and `SQLalchemy` toolkit for python
- Exploratory analysis by visualization with `matplotlib` and `seaborn`
- Building an interactive dashboard using `dash` and `plotly.express`
- Train classification models (Logistic Regression, SVM, Decision Tree, kNN) to predict of future landing outcomes with `scikit-learn`

![image](https://github.com/masonphung/project_falcon9/assets/131331827/11c3e7ac-fe07-4861-93fc-2dae37f74940)

## ADDED FEATURES

### Notebooks

- Removed lengthy features, convert repeated functions into predefined functions
- Added step explanation, result comments to each section
- Setting up and work with SQL in a local MySQL database (Originally IBM Skills Network Lab Environment)

### Dashboard app

- Styled with `dash_bootstrap_components`, external css, responsive customized layout
- Added multiple-inputs callbacks
- Added extra plots, statistic summary, global attribute selection and year slider

## <span style="color:#ff9933">LATEST UPDATES: ver 2.0</span>
- Remove separate notebooks, combine all parts of the project into a single jupyter notebook (the dash app is still in a separate .py file).
- Refine data cleaning part, add new cleaning features so we can use the collected data to all parts of the projects (Originally, later parts used pre-cleaned data, not the data that we collected in the beginning).
- Remove multiple excess datasets, only use original datasets from collected.