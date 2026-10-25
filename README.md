# SpaceX Falcon 9 First Stage Landing Prediction

A complete end-to-end data science project for predicting whether a Falcon 9 first stage will land successfully using mission features, launch metadata, and machine learning models.

## Project overview

This repository contains:
- a data preparation and feature engineering pipeline
- exploratory data analysis (EDA)
- model training with comparison of several classifiers
- a dashboard for interactive analysis
- a PowerPoint deck generator for a professional presentation

## Key objective

Predict whether the Falcon 9 first stage will land successfully based on features such as:
- flight number
- payload mass
- orbit type
- launch site
- booster version
- landing pad
- reusable status
- block version

## Repository structure

```text
.
├── README.md
├── requirements.txt
├── notebooks/
│   └── SpaceX_Falcon9_Landing_Prediction.ipynb
├── src/
│   ├── data_pipeline.py
│   ├── model_pipeline.py
│   └── dashboard_app.py
├── scripts/
│   └── generate_presentation.py
├── presentation/
│   └── SpaceX_Presentation.md
├── data/
│   └── README.md
├── .gitignore
└── LICENSE
```

## Quick start

### 1) Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2) Run the notebook

Open the notebook in Jupyter:

```bash
jupyter notebook notebooks/SpaceX_Falcon9_Landing_Prediction.ipynb
```

### 3) Run the dashboard

```bash
python src/dashboard_app.py
```

Then open the local URL shown in the terminal (typically http://127.0.0.1:8050).

### 4) Generate the PowerPoint deck

```bash
python scripts/generate_presentation.py
```

This script creates a professional PowerPoint file in the `presentation/` folder.

## Machine learning models evaluated

- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- K-Nearest Neighbors (KNN)
- Model comparison using validation and test accuracy

## Presentation summary

The final presentation focuses on:
- business context of SpaceX reusability
- data collection strategy
- EDA insights
- feature engineering choices
- predictive modeling
- model performance and business interpretation
- recommendations and conclusion

## Data source

The project uses the SpaceX launch dataset prepared during the lab workflow and can be adapted to the public SpaceX API or the cleaned CSV versions used in the assignment.

## License

This project is intended for educational and portfolio purposes.

## Author

Created for a complete SpaceX data science portfolio project.
