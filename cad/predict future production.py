from sklearn.linear_model import LinearRegression #LLM - AGENTIC AI
import numpy as np

# Historical production data
days = np.array([1, 2, 3, 4, 5]).reshape(-1, 1) # reshape[[1],[2],[3],[4],[5]]
production = np.array([100, 120, 130, 150, 170]) 

# Create and train model
model = LinearRegression()
model.fit(days, production)

# Predict day 6 production
prediction = model.predict([[6]])

print("Predicted Production for Day 6:", prediction[0])















# from sklearn.linear_model import LinearRegression
# import numpy as np

# # Historical production data
# days = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# production = np.array([100, 120, 130, 150, 170])

# # Create and train model
# model = LinearRegression()
# model.fit(days, production)

# # Predict Day 6, 7, 8
# future_days = np.array([6, 7, 8]).reshape(-1, 1)
# predictions = model.predict(future_days)

# # Print results
# for i, pred in enumerate(predictions, start=6):
#     print(f"Predicted Production for Day {i}: {pred}")