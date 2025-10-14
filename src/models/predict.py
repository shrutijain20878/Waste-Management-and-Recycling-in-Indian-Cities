import pandas as pd
import joblib

model = joblib.load(r"C:\Users\ShrutiJain\Downloads\Waste_management_project\models\trained_model.pkl")
test_data = pd.read_csv(r"C:\Users\ShrutiJain\Downloads\Waste_management_project\data\processed\processed_data.csv")

X = test_data[['Waste Generated (Tons/Day)', 'Population Density (People/km²)','Municipal Efficiency Score (1-10)', 
       'Cost of Waste Management (₹/Ton)','Awareness Campaigns Count','Landfill Capacity (Tons)','Year']]

predictions = model.predict(X)

output = pd.DataFrame()
output['predicted Recycling Rate (%)'] = predictions
output.to_csv('predictions.csv', index=False)

print("Predictions saved to predictions.csv")
