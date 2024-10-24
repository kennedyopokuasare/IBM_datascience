# IBM Data Science

This repository contains hands-on completed work following the IBM Data Science professional certification on Coursera. 

## What is Data Science

I learnt how the CRISP-DM methodology aligns with the research methods I’ve been using in the mobile computing and well-being field. The course's practical insights and real-world applications, coupled with hands-on peer-reviewed exercises, made it a truly rewarding experience.

[Certificate of Completion](https://www.coursera.org/account/accomplishments/verify/MGUNWY77TWBN)

## Python for Data Science, AI  & Development

I refreshed my Python knowledge in data structures such as **lists, sets, dictionaries, functions classes, using Pandas, Numpy, string manipulation, web scrapping using Pandas and BeautifulSoup**.

[Source](./web_scrapping/)

[Certificate of Completion](https://www.coursera.org/account/accomplishments/verify/W9A5M2FFUEY5)

## Databases and SQL for Data Science with Python

I refreshed my working knowledge of SQL. 🎓💻 It was an engaging experience querying the publicly available City of Chicago crimes, socioeconomic, and schools dataset within Jupyter Notebook, **with Python DB-API, pandas, SQL Magic and a focus on SQL optimization**. 

Revisiting stored procedures and ACID transactions, brought back a wave of nostalgia from 2012 ⏳ when I was involved in developing the Attendance Management System at Students Loan Trust Fund Ghana 🇬🇭. This reflection led me to read about the evolving role of stored procedures in modern data-driven production systems, weighing their pros and cons, and considering aspects like application testability and the separation of data and business logic.

Pandas can be used to load data and saved directly into an SQL database table over a database connection. Here we use SQlite as a test database. With SQL Magic, the database can be queried directly from a jupyter notebook, as shown in the screenshot below. 

![Loading and saving to db table with pandas](./img/load_data_and_save_to_db_table.png)

![SQL query with sub query](./img/sql_query_in_jupyter.png)

[Source](./database/)

[Certificate of Completion](https://www.coursera.org/account/accomplishments/verify/FXN2LMYKS0BH)


## Data Analysis with Python

While I have previously used statistical regression methods, including multi-level modelling in my work on predicting depression symptom severity using behavioural data 📲 🛌 🚶‍♂️ 🤸‍♀️ passively collected via smartphones and ŌURA ring [[1](https://www.sciencedirect.com/science/article/pii/S1574119222000566), [2](https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2021.625247/full)], in this course, I focused on machine learning regression techniques. 

I explored **Linear, Multi-linear, Polynomial, and Ridge regression using Scikit-learn, Seaborn, and Pandas and gained new insights into Exploratory Data Analysis**.

[Source](./data_analysis/)

[Certificate of Completion](https://www.coursera.org/account/accomplishments/verify/IBRF87JTMPFL)

This plot shows a heatmap of the correlation matrix between various features of the Houses. There is a high corelation between house `prices` and `grade (0.67)`, `number of bathrooms (bathroom, 0.53)`, `square feet of living area (sqrt_living, 0.7)`. There are also notable multicolinearity between sevaral of the features, for instance between square feet above and square feet of living area. Here we consider only pairwise correlations, therefore statistical significance of the correlations have not been computed i.e, the p-values are not determined or adjusted or multiple testing. 


![House price correlation matrix](./img/house_price_correlation%20matrix.png)


## Data Visualization with Python

As Data visualion is a essential part of Data Science, I advanced my working knowledge in Data Visualization with Python through this course. I have previously developed data analysis and compliance dashboards using R Shiny, and conducted exploratory data analysis of smartphone and wearable datasets with ggplot2 in R. In this coourse, **I enhanced my skills in Python, using tools like Folium for geospatial data visualization (clustered markers, choropleth maps), Matplotlib, Seaborn, Pandas, and building dashboards with Plotly Dash**.

During the course, I explored and visualized interesting real-world datasets, such as the United Nations Population data on immigration to Canada, the Australian wildfire dataset, and the United States  automobile sales during recession and non-recession periods. I also deepened my understanding of the Python Data Visualization ecosystem, comparing tools like Streamlit, Plotly Dash, and Panel in terms of production readiness, ease of development and integration with other plotting libraries.

[Source](./data_visualisation/) 

[Certificate of completion](https://coursera.org/share/7df2fe9692ca65e50e23b4b1b1a04801)

Below is a visualisation of crimes in the San Francisco Crimes dataset. Markers are clustered together. Click a cluster expand to show the markers within the cluster. 
![San Fracisco Crimes data](./img/san_franscisco_crimes_data_with_grouped_markers.png)

Here, we see a choropleth showing annual imigration to Canada from various countries. The top countries with immigration to Canada are China and India. The black coloured countries do not have any imigration data, or the countries names in the GeoJSON and the dataset do not match. Folium can also configured to show a specified colour when data is not available. 

![Canada Immigration data](./img/canada_imigration_choropleth.png)

This plot visualizes Autombile sales per vehicle type in the United States during recession and non recession periods. During non recession periods, car sales are generally high, with sports and esecutive cars having the highest sales. The car sales drastically declines during recession periods with sports cars saled being the most affected. 

![Vehicle sale during recession and non recession](./img/Vehicle_sales_during_recession_and_non_recession.png)


## Machine Learning with Python

I refreshed my working knowledge in Machining Learning. In my [previous scientific research work](https://www.sciencedirect.com/science/article/pii/S1574119222000566), I leveraged an ensemble of classifiers to predict the depression status of participants using behavioural data 📲 🛌 🚶‍♂️ 🤸‍♀️ passively collected via smartphones and ŌURA ring. In this course, **I revisited the theoretical aspects of Regression, Classification and Clustering**.  Does on need efficient car engines, drive smaller engine size cars or switch to EV to reduce CO2 emissions ? Those were the question that led my curiosity in analysing Fuel consumption and C02 emission data publicly available from the Canadian Open Government portal.  With 9 out of 12 courses completed, I am inching closer to the final goal of obtaining the IBM Data Science Professional certificate.  Next up is an Applied Machine Learning capstone project. 

[Source](./machine_learning/) 

[Certificate of completion](https://coursera.org/share/762a19f6e96c3d2901423646bfabee84)

```python

sns.histplot(x=df.Co2_Emissions)
plt.axvline(df.Co2_Emissions.mean(), color="b", linestyle="dashed", label="Mean")
plt.axvline(df.Co2_Emissions.median(), color="r", linestyle="dashed", label="Median")
plt.xlabel("Co2 Emissions")
plt.legend()
plt.show()

```
The Distribution of C02 emissions is more closer to a normal distribution, given that the mean and median are almost equal. Are there any outliers ?
![Distribution of Co2 Emissions](./img/fuel_consumption_distro.png)


Distribution plot of true and predicted CO2 Emissions. The model makes higher errors in predicting Co2 Emisisons in ranges 200-300. More dataset in these might improve the performance. Examining the residual plot


![Distribution plot of true and predicted CO2 Emissions](./img/distribution_plot_true_pred_co2_emission.png)

A residual plot for the prediction of Co2 Emissions. The residual plots shows a very that Multiple Linear Regression is not best estimator given the feature set. There is a pattern in the residual plots 
![co2 emmision residual](./img/co2-emission_residual_plot.png)


## Applied Data Science Capstone Project

In this capstone, we predict if the Falcon 9 first stage will land successfully. A Falcon 9 launch costs SpaceX 62 million dollars, while it costs other providers upward of 165 million dollars. Predicting if the first stage of Falco 9 will land succesfully can determine the cost of a launch. 

Key findings of the project included:

* Increased Landing Success Over Time: There has been a notable improvement in successful landings in recent years, especially from launch sites CCAFS SLC 40 and KSC LC 39A.

* Influence of Target Orbits: Missions to orbits such as ES-L1, GEO, HEO, and SSO exhibited higher landing success rates. In contrast, missions targeting GTO and SO faced more challenges.

* Predictive Modeling: A machine learning model was developed, achieving an 83% accuracy rate in predicting successful landings. Nonetheless, there is potential to enhance the model's performance, particularly in reducing false positive predictions.

See the [Full PDF Report of the project](./captone_project/final_report/spacex-capstone-report.pdf) and [Source code](./captone_project/)


## Generative AI

In this course, I explored how to use generative AI to augment the full lifecyle of the Data Science systems, for instance applying generative AI techniques in the development and refinement of machine learning models. I explored data generation and augmentation using generative AI tools like ChatGPT. I utilized ChatGPT to generate and label [data](./generative_ai/digital_phenotyping_data_gpt_labeled.csv) with prompts based on domain knowledge. The CTGAN Python SDK was employed to create additional [synthetic data](./generative_ai/generating_synthetic_data.ipynb) that was comparable to the original GPT-generated data.


Below are example promts and responses used to generate the data. 

![prompt 1](./generative_ai/1.%20gpt_prompt_1.png)
![prompt 2](./generative_ai/2.%20gpt_prompt_2.png)
![prompt 3](./generative_ai/3.%20gpt_prompt_3.png)
![prompt 4](./generative_ai/4.%20gpt_prompt_4.png)
![prompt 4](./generative_ai/5.%20gpt_prompt_5.png)

[Source](./generative_ai/)

[Certificate of completion](https://www.coursera.org/account/accomplishments/verify/UOJDJ8UL7T04)

## More reading more: 
- IntepretML : https://interpret.ml/
- FairLearn: https://fairlearn.org/
