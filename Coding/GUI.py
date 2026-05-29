import tkinter as tk
from sklearn.ensemble import RandomForestRegressor


# -----------------------------
# Dummy Model (แทนโมเดลจริง)
# -----------------------------
forest = RandomForestRegressor()

# สมมุติ train model
import numpy as np
X_dummy = np.random.rand(100,5)
y_dummy = np.random.rand(100)
forest.fit(X_dummy, y_dummy)


# -----------------------------
# Functions
# -----------------------------
def predict_bleaching():

    try:
        latitude = float(entry_lat.get())
        longitude = float(entry_lon.get())
        depth = float(entry_depth.get())
        clim_sst = float(entry_clim.get())
        ssta = float(entry_ssta.get())

        features = [[latitude, longitude, depth, clim_sst, ssta]]

        prediction = forest.predict(features)[0]

        result_label.config(
            text=f"Predicted Bleaching Percentage: {prediction:.2f}",
            bg="orange"
        )

    except ValueError:
        result_label.config(
            text="Please enter valid numbers",
            bg="red"
        )


def clear_fields():

    entry_lat.delete(0, tk.END)
    entry_lon.delete(0, tk.END)
    entry_depth.delete(0, tk.END)
    entry_clim.delete(0, tk.END)
    entry_ssta.delete(0, tk.END)

    result_label.config(text="")


# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("Coral Bleaching Predictor")

canvas = tk.Canvas(root, width=600, height=350)
canvas.pack()

# Header
header = tk.Label(root, text="Bleaching Predictor", font=("Arial",20))
canvas.create_window(300,40, window=header)


# -----------------------------
# Input Fields
# -----------------------------

def create_input(label_text, y_position):

    label = tk.Label(root, text=label_text, font=("Helvetica",12))
    entry = tk.Entry(root)

    canvas.create_window(120, y_position, window=label)
    canvas.create_window(350, y_position, window=entry)

    return entry


entry_lat = create_input("Latitude (Degrees)", 100)
entry_lon = create_input("Longitude (Degrees)", 130)
entry_depth = create_input("Depth (Meters)", 160)
entry_clim = create_input("ClimSST", 190)
entry_ssta = create_input("SST Anomaly (Celsius)", 220)


# -----------------------------
# Buttons
# -----------------------------
predict_button = tk.Button(
    root,
    text="Predict",
    command=predict_bleaching,
    bg="brown",
    fg="white",
    font=("Helvetica",10,"bold")
)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_fields,
    bg="gray",
    fg="white",
    font=("Helvetica",10,"bold")
)

canvas.create_window(250,260, window=predict_button)
canvas.create_window(350,260, window=clear_button)


# -----------------------------
# Result Label
# -----------------------------
result_label = tk.Label(root, text="", font=("Helvetica",12))
canvas.create_window(300,300, window=result_label)


# -----------------------------
# Run GUI
# -----------------------------
root.mainloop()