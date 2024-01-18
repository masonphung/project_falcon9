**Mini Project: Analysis and Prediction of SpaceX Falcon9 rocket landing**

INTRODUCTION

> *SpaceX advertises Falcon 9 rocket launches on its website with a cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because
> SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch.*

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/crash.gif)

- In the project, we will predict if the Falcon 9 first stage will land successfully.
- This project is a part of the IBM Data Science Specialization, further developed by Mason Phung


METHODOLOGY

- There will be 2 datasets used in the project, Falcon9 launch data will be pulled from SpaceX REST API and the launch records will be scraped from Wikipedia
- Data will then be wrangled, visualized and queried with SQL for exploratory descriptive analysis
- An interactive dashboard will be built using `dash` and `plotly`
- Finally, we will train Machine Learning models to predict of future landing outcomes using classification techniques with `scikit-learn`
