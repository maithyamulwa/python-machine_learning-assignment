import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dataset
hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

# Separate features (X) and target (y)
X = [[h] for h in hours]
y = scores

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Get user input and predict
hours_studied = float(input("Enter hours studied: "))
predicted = model.predict([[hours_studied]])[0]

print(f"Predicted exam score: {predicted:.2f}")

# Plot
plt.figure(figsize=(8, 5))
plt.scatter(hours, scores, color="blue", label="Actual data")
plt.plot(hours, model.predict(X), color="red", label="Regression line")
plt.scatter(hours_studied, predicted, color="green", s=100, marker="*",
            zorder=3, label=f"Prediction ({hours_studied:g} hrs, {predicted:.2f})")

plt.title("Study Hours vs Examination Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.xticks(range(0, 12))
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend()
plt.show()
