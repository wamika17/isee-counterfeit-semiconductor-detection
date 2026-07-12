"""
--------------------------------------------------------
Model Training

This script trains a Decision Tree classifier using
electrical and OCR features.

Author: Wamika Varada
--------------------------------------------------------
"""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv("dataset.csv")

# Features
X = data[[
    "OCR_Confidence",
    "Truth_Table_Accuracy",
    "Average_Input_Voltage",
    "Average_Output_Voltage",
    "Voltage_Drop",
    "Failed_Logic_Tests"
]]

# Labels
y = data["Label"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print(f"Model Accuracy: {accuracy*100:.2f}%")
