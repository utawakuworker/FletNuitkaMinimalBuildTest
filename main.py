import flet as ft
from sklearn.linear_model import LinearRegression
import numpy as np

def main(page: ft.Page):
    # Minimal sklearn usage
    X = np.array([[1], [2], [3]])
    y = np.array([1, 2, 3])
    model = LinearRegression().fit(X, y)
    prediction = model.predict([[4]])[0]

    # Minimal Flet UI
    page.add(
        ft.Text(f"Prediction for input 4: {prediction:.2f}")
    )

ft.app(target=main)
