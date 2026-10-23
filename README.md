# python-machine_learning-assignment theory questions

1. What is supervised machine learning?

Supervised machine learning is a type of machine learning where a model learns from labelled data. Each training example has input features and a known correct output (the label or target). The model studies these input-output pairs to learn the relationship between them, and can then predict the output for new, unseen inputs.

2. What is unsupervised machine learning?

Unsupervised machine learning is a type of machine learning where a model learns from unlabelled data. There are no correct answers provided. Instead, the model looks for hidden structure, patterns or groupings in the data on its own, such as clusters of similar items.

3. Explain the difference between supervised and unsupervised learning.
Aspect	Supervised Learning	Unsupervised Learning
Data	Labelled (inputs and known outputs)	Unlabelled (inputs only)
Goal	Predict an outcome	Discover patterns or groups
Feedback	The model's predictions are compared with the correct answers	No correct answers to compare against
Typical tasks	Regression, classification	Clustering, dimensionality reduction
Example in this assignment	Predicting exam scores from study hours	Grouping customers by spending and visits
4. Why is Linear Regression considered supervised learning?

Linear Regression is supervised because it is trained on data where the correct answer is already known. In Part A, every value of Hours Studied (the input) comes with a known Exam Score (the target). The model uses these known pairs to find the best-fitting line, and it measures how well it fits by comparing its predictions with the actual scores. Without the target values, it could not learn the line.

5. Why is K-Means considered unsupervised learning?

K-Means is unsupervised because it works without any labels. In Part B, the dataset has only monthly spending and monthly visits. Nobody tells the model which customer belongs to which group. K-Means groups customers by how close they are to each other, and the cluster numbers it assigns are arbitrary labels it creates itself, not correct answers it was given.

6. What is the difference between fit() and predict()?
fit() trains the model. It learns from the training data. For Linear Regression, fit(X, y) learns the slope and intercept of the line. For K-Means, fit(X) learns the cluster centres.
predict() uses the trained model to produce output for new data. For Linear Regression, predict() returns an estimated exam score. For K-Means, predict() returns the cluster a data point belongs to.

In short, fit() is the learning step and predict() is the using step. fit() must be called before predict().

7. Real-world applications

Supervised learning

Email spam detection: a model is trained on emails labelled "spam" or "not spam" and then classifies new incoming emails.
House price prediction: a model learns from past sales (size, location, number of rooms and the sale price) and then estimates the price of a new house.

Unsupervised learning

Customer segmentation: a business groups customers by purchasing behaviour to target marketing, as in Part B.
Anomaly or fraud detection: a model learns what normal transactions look like and flags unusual ones that do not fit any usual pattern, without needing labelled examples of fraud.

This assignment was geared towards understanding how supervised and unsupervised machine learning in python
