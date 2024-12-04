# **Mini Project: Data Analysis and Prediction of SpaceX Falcon9 rocket launches**

Mason Phung
Last updated: December 2024

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
- After completing the base project, I created a new personal version, the dashboard app as well as the machine learning section by adding extra integrations, new features and customization (Details below)
- Have been refining this project for several times since then!

## THE PROJECT COVERS

- `Python` programming and `SQL` data analysis.
- Data collection: API data collection w. `requests` and webscraping w. `BeautifulSoup`
- Data analysis with SQL using local database `mySQL` and `SQLalchemy` toolkit for python
- Exploratory analysis by visualization with `matplotlib` and `seaborn`
- Building an interactive dashboard using `dash` and `plotly.express`
- Train classification models (Logistic Regression, SVM, Decision Tree, kNN, XGBoost, Multi-layer perceptron) with hyperparameter tuning to predict of future landing outcomes with `scikit-learn`

![image](https://github.com/masonphung/project_falcon9/assets/131331827/11c3e7ac-fe07-4861-93fc-2dae37f74940)

## SOME FINDINGS

### **The increasing trend in success rate**

The data analysis project provides an in-depth view of the space industries. The data not only presents the important features to be considered in each rocket launch to the space, but also let us know which essential data to be recored when it finished. 
   
The exploratory analysis shows the incredible progress the company made after a period of 10 years, with the success rate increased from about 20% at the first 10 launches to around 70-80% from flight 20th and achieved a complete 100% success after flight 80th. 
   
Based on the analysis, there are many factors contributing to the success rate, including:
- `GridFins`: High correlation strength with success outcome, means that the launch is more likely to be successful when using grid fins.
- `Legs`: High correlation strength with success outcome, means that the launch is more likely to be successful when using legs in landing.
- `ReusedCount`: High correlation strength with success outcome, means that higher core reused count is likely to lead to a success launch.
   
### **Higher payload mass equals to higher success rate?**
Success rate increased had allowed the company to conduct further experiments with higher payloads. According to the data, the carried payload tended to increase launches after launches. With the average of about 3000 kg each launch in the period from 2010-2014, the average payload increased about 30% every 2 years and sharply went up for 230% in the last 3 years 2018-2020. Note that this is the period where SpaceX achieves the highest launch success rate. 
   
However, it is suggested that the increase in payload mass is not the main contributor to the higher success rate, but technology advanced and with knowledge learned from past launches are the main reasons for the increase in success rate. These criteria allowed rockets to carry larger payload into the space.
   
   
### **Launch site and geography's role**
Since all of the launches has a high success rate, geography may be a important contributor to this outcome. Three launch sites are all located in the coast of the United States. There are some remarkable points that can be noticed:
- The sites are far from the urban, where there is no residential area. 
- The sites are close to forest or natural/wild life area.
- The sites has one side faced the ocean.
- There are railway routes went through the sites (black/white lines).

The first three criteria contribute to the safety of the population. Based on the [information from the industry](https://www.bbc.com/future/article/20230518-what-are-the-odds-of-a-successful-space-launch#), the failure rate of rocket launches is usually at around 4-5%, while in initial phase, it can be up to 30% (In our analysis, we observed a failure rate of 80% in the first 10 launches). Therefore, it is extremely important for launch sites to be built close to an uninhabited zone (such as forest, wild life area). Moreover, as the ocean is also considered to be uninhabited, it would be an ideal place for crashing rockets to land, reduce noises, damages and negative influences to the home country.
   
Railway is also an necessary part of a launch site. It provides support to the logistic systems of the facilities as launching space rocket is an expensive operation and requires heavy supplies. Even in a world where air transportation is dominating, we can not neglect the cost-effectiveness and reliability of railways.

However, to further determine the impact of geography on success rate, we will need more information as the our data only focus on technical aspect of the rocket and its launch.
   
   
### **Hyperparameter tuning brings the reliability to the models**
In this project, we need to use Classification models because the target variable (`class`: success or not sucess) is a categorical variable. All of the machine learning models perform well and yielded high accuracy scores. 

The model was superior in predicting successful launches (`class = 1`, with f1-score = 87.5% in average) while they seem to be a little bit less reliable in predicting the other outcome. This can be explained by the imbalance in the number of `class=0` vs `class=1` values, while we have doubled `class=1` compared to the other. This caused imbalanced weight between the two class and can affect the accuracy score negatively. In our work, we have applied two strategies to overcome this problem including stratification and using parameter `class_weight = 'balanced'` to penalize class `1`.

Tuning hyperparameters conducted by changing default parameters into ones that are suitable to the data, helps the model to make accurate predictions. We also used `GridSearchCV` to cross validate the results, reduce the chance of a score happens by randomness.

Hyperparameter tuning results in a generally higher accuracy score for 2 models kNN and XGBoost, with the accuracy score increase by 5% in average.

Hyperparameter tuning also helps the models to overcome the issue of overfitting, which were observed in Decision Tree and XGBoost. The sign of overfitting can be observed in the accuracy score of the model with the training set.

The most difficult tune was the MLP neural network model, which is complex and requires different parameters to be tuned. As we are using `GridSearchCV`, which leads to an issue of balancing between the number of tuned parameters and training time, it is important to remove some of the underperforming paramters after a few runs to save resources. By observing then removing factors that are not working well in the model we can reducing the running time of grid search.

Note: Check parameters performance by using `cv_results_`, convert it into a pandas dataframe and sort by `mean_test_score`


### **Improvements for the Machine Learning models**
There are many factors that we still need to consider to make the models work better and make sure it predicts without bias or overfitting.
- More data is needed, especially with failed launches. Out of 90 launches, we have 60 successful outcome while only have 30 failed outcomes. This not only may make the weight of each class imbalanced when modeling, but also shows that we may not have enough `failed` data for the model to train (even though we applied stratification to overcome this, but it is clearly better to have actual data.
- The dataset is relatively small. With more dataset, the model can have more data to learn, thus prevent overfitting and bias predictions.
- Only v9. core models considered. Aerospace and rocket launching industry is huge and there are countless type of space rockets. Since our models were built around v9. Falcon core, the model can only work best with this type of core. If we would like to use the models to have the ability to predict the outcomes of other rocket types, we'll also need to have our training data covers more types of rockets.

## ADDED FEATURES

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

## <span style="color:#ff9933">LATEST UPDATES: ver 3.0</span>
Ver 3.0
- Fix linguist to detect Python.
- Split the analysis notebook into small notebooks for easier interpretation.
- Add some SQL scripts in `/sql`.
- Refine working repo.

Ver 2.0
- Remove separate notebooks, combine all parts of the project into a single jupyter notebook (the dash app is still in a separate .py file).
- Refine data cleaning part, add new cleaning features so we can use the collected data to all parts of the projects (Originally, later parts used pre-cleaned data, not the data that we collected in the beginning).
- Remove multiple excess datasets, only use original datasets from collected.

## Let me know if you see any rooms for improvement!!
