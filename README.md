# **Mini Project: Analysis and Prediction of SpaceX Falcon9 rocket landing**

## INTRODUCTION

> *Space Exploration Technologies Corp. or SpaceX is an American spacecraft manufacturer, popular for their successful mission in sending a spacecraft and astronauts to the International Space Station. They are also well-known for their [VTVL](https://en.wikipedia.org/wiki/VTVL) rocket launches , in which rockets can land and be resued, thus save a huge amount of launching cost for the company.*
>
> *One of SpaceX's most popular rocket - the Falcon 9, have landed and reflown [more than 200 times](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches) . The rocket was advertised on its website with a launch cost of 62 million dollars; other providers cost upward of 165 million dollars each, much of the savings is because SpaceX can reuse the first stage. Therefore if we can determine if the first stage will land, we can determine the cost of a launch.*

![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/landing_1.gif)
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DS0701EN-SkillsNetwork/lab_v2/images/crash.gif)

## OBJECTIVES
- Discover insights of what affects the outcome of a launch mission, including technical and geographical grounds.
- Build a classification ML model that can predict if the Falcon 9 first stage will land successfully.
- Determine which ML model works the most accurate.
- Conduct the project using Python programming language.

## METHODOLOGY

- There will be 2 datasets used in the project, Falcon9 launch data will be pulled from SpaceX REST API and the launch records will be scraped from Wikipedia
- Data will then be wrangled, visualized and queried with SQL through for exploratory descriptive analysis
- An interactive dashboard will be built using `dash` and `plotly`
- Finally, we will train Machine Learning models to predict of future landing outcomes using classification techniques with `scikit-learn`

## NOTES
- This project is a part of the IBM Data Science Specialization course.
- The notebooks, dashboard app were further developed by Mason Phung.