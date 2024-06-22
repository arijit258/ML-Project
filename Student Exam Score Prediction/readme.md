# Student Performance Prediction

## Project Overview
This project aims to predict students' exam scores based on various features such as the number of hours studied, previous exam scores, and attendance. Regression techniques are used to build models that estimate a student's final grade given these input features. The project provides insights into factors influencing student performance and helps educators identify students who may need additional support.

## Dataset Description
The data comes from two Portuguese secondary schools, and it includes student grades, demographic, social, and school-related features. The datasets cover two distinct subjects: Mathematics (`student-mat.csv`) and Portuguese (`student-por.csv`). 

### Attribute Information
1. **school**: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
2. **sex**: Student's sex (binary: 'F' - female or 'M' - male)
3. **age**: Student's age (numeric: from 15 to 22)
4. **address**: Student's home address type (binary: 'U' - urban or 'R' - rural)
5. **famsize**: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
6. **Pstatus**: Parent's cohabitation status (binary: 'T' - living together or 'A' - apart)
7. **Medu**: Mother's education (numeric: 0 - none, 1 - primary education, 2 - 5th to 9th grade, 3 - secondary education, 4 - higher education)
8. **Fedu**: Father's education (numeric: 0 - none, 1 - primary education, 2 - 5th to 9th grade, 3 - secondary education, 4 - higher education)
9. **Mjob**: Mother's job (nominal: 'teacher', 'health', 'services', 'at_home', 'other')
10. **Fjob**: Father's job (nominal: 'teacher', 'health', 'services', 'at_home', 'other')
11. **reason**: Reason to choose this school (nominal: 'home', 'reputation', 'course', 'other')
12. **guardian**: Student's guardian (nominal: 'mother', 'father', 'other')
13. **traveltime**: Home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, 4 - >1 hour)
14. **studytime**: Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, 4 - >10 hours)
15. **failures**: Number of past class failures (numeric: n if 1<=n<3, else 4)
16. **schoolsup**: Extra educational support (binary: 'yes' or 'no')
17. **famsup**: Family educational support (binary: 'yes' or 'no')
18. **paid**: Extra paid classes within the course subject (binary: 'yes' or 'no')
19. **activities**: Extra-curricular activities (binary: 'yes' or 'no')
20. **nursery**: Attended nursery school (binary: 'yes' or 'no')
21. **higher**: Wants to take higher education (binary: 'yes' or 'no')
22. **internet**: Internet access at home (binary: 'yes' or 'no')
23. **romantic**: With a romantic relationship (binary: 'yes' or 'no')
24. **famrel**: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
25. **freetime**: Free time after school (numeric: from 1 - very low to 5 - very high)
26. **goout**: Going out with friends (numeric: from 1 - very low to 5 - very high)
27. **Dalc**: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
28. **Walc**: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
29. **health**: Current health status (numeric: from 1 - very bad to 5 - very good)
30. **absences**: Number of school absences (numeric: from 0 to 93)
31. **G1**: First period grade (numeric: from 0 to 20)
32. **G2**: Second period grade (numeric: from 0 to 20)
33. **G3**: Final grade (numeric: from 0 to 20, output target)

## Project Steps

### 1. Data Exploration and Preprocessing
- Load and inspect the datasets.
- Handle missing values.
- Encode categorical variables.
- Normalize/standardize numerical variables.
- Split the data into training and test sets.

### 2. Feature Selection
- Analyze the correlation between features and the target variable (G3).
- Select important features based on correlation and domain knowledge.

### 3. Model Selection and Training
- Choose regression models such as Linear Regression, Decision Tree Regressor, Random Forest Regressor, and Gradient Boosting Regressor.
- Train models on the training set.

### 4. Model Evaluation
- Evaluate the models using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and R-squared.
- Compare the performance of different models.


## Getting Started

### Prerequisites
- Python 3.x
- Required libraries: pandas, numpy, scikit-learn, matplotlib, seaborn

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/arijit258/student-exam-score-prediction.git
    cd student-exam-score-prediction
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Run the data preprocessing and feature selection script:
    ```bash
    python student_exam_score_prediction.py
    ```

2. Project Showcase:
    ```bash
    streamlit run app.py
    ```


## Results
Model's Performance with r2-score:
LinearRegression : 0.789291454376445
Lasso Regression : -0.00042191125799884155
Ridge Regression : 0.7803303067917783
DecisionTreeRegressor : 0.71668659025385
RandomForestRegressor : 0.8553250814523123
AdaBoostRegressor : 0.8400906811768062
GradientBoostingRegressor : 0.8737952006611264
ExtraTreesRegressor : 0.8173330309635984
KNeighborsRegressor : 0.5634751423950496
SVR : 0.653756057520791
XGBRegressor : 0.8032137653482628

TThe best model is GradientBoostingRegressor

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
This project uses the dataset provided by [Kaggle](https://www.kaggle.com/datasets/impapan/student-performance-data-set).
