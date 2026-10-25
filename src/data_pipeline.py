import os
import numpy as np
import pandas as pd


def load_data(path=None):
    if path is None:
        path = os.path.join('data', 'dataset_part_2.csv')
    return pd.read_csv(path)


def prepare_features(df):
    features = df[[
        'FlightNumber', 'PayloadMass', 'Orbit', 'LaunchSite', 'Flights',
        'GridFins', 'Reused', 'Legs', 'LandingPad', 'Block',
        'ReusedCount', 'Serial'
    ]]
    X = pd.get_dummies(features, columns=['Orbit', 'LaunchSite', 'LandingPad', 'Serial'], drop_first=True)
    y = df['Class']
    return X.astype(float), y


def summarize(df):
    return {
        'rows': df.shape[0],
        'columns': df.shape[1],
        'target_distribution': df['Class'].value_counts().to_dict()
    }
