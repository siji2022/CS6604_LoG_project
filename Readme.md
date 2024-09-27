# Graph-Based Anomaly Detection and Predictive Modeling on Sensor Networks

#### this is the course project of Virginia Tech 6604 Learnign on Graph

### Daodao Zhou, Jianger Yu and Siji Chen

In this project, we aim to leverage machine learning techniques in conjunction with graph-based approaches to analyze a real-world dataset published by Intel This dataset, collected from 54-node sensor network, encompasses both spatial and temporal information, including measurements of temperature, humidity, light and voltage.


As a real-world dataset, it presents several shortcomings and challenges: It contains numerous missing data points, the data points of each sensor are not balanced, due to the inherent limitations of the sensor, the dataset contains outlier data points and noise. Therefore, the preprocessing of this dataset is a significant step in this project.

The primary problem that our team try to address in this project is: given a real-world inter-correlated time series data, can we find anomalies, patterns? and can we predict the future trend based on the existing data? To address these problems, we proposed the following approaches in this project: 1. Employ various graph-based techniques to impute missing values by incorporating information from neighboring nodes. 2. Identify sensor malfunctions or abnormal environmental patterns by detecting outliers and noise in the graph-structured data. 3. Develop and train a predictive model with machine learning approaches that exploits the graph structure to forecast future sensor readings. 4. Evaluate the performance of our proposed model with the existing dataset.
