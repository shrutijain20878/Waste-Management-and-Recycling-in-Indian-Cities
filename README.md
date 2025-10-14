Project objective- to predict the Recycling Rate based on below parameters- 
Waste Generated (Tons/Day)
Population Density
Municipal Efficiency Score
Cost of Waste Management (₹/Ton)
Awareness Campaigns Count
Landfill Capacity (Tons)
Year

How to run the Flask app-- 
in Terminal write-- venv\Scripts\activate -- to activate virtual environment
now cd src - to direct to src directory where app.py file is present
now-- python app.py -- to run flask app

How to deploy (optional)

File/folder explanation
data_preparation.ipynb--- for data preparation
exploratory_data_analysis.ipynb--- for data analysis
model_training.ipynb-- for model training
trained_model.pkl -- stored trained model in pickle file to avoid running large code again and again
index.html -- have html and css code-- frontened part of flask app
app.py -- code for flask app
requirements.txt -- for storing all required libraries or module

Model performance--
Tried 4 diiferent Regressor model i.e. Ridge regressor, DecisionTreeRegressor, RandomForestRegressor, XGBoost Regressor

XGBoost Regressor give the lowest Root Mean Squared Error after training so, use XGBoost Regressor for predicting value.
