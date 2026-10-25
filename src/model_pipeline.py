import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix


def train_and_compare_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    models = {
        'LogisticRegression': LogisticRegression(),
        'SVM': SVC(),
        'DecisionTree': DecisionTreeClassifier(),
        'KNN': KNeighborsClassifier(),
    }

    metrics = {}
    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
        metrics[name] = accuracy_score(y_test, preds)

    return metrics, X_train_scaled, X_test_scaled, y_train, y_test


def optimize_model(model, param_grid, X_train, y_train):
    grid = GridSearchCV(model, param_grid, cv=5)
    grid.fit(X_train, y_train)
    return grid
