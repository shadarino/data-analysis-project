import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# --- 1. CSV-Datei einlesen ---
data_file = "data/messdaten.csv"
df = pd.read_csv(data_file)

# --- 2. Statistik ---
mean_temp = df['temperature_C'].mean()
std_temp = df['temperature_C'].std()
print(f"Mittelwert der Temperatur: {mean_temp:.2f} °C")
print(f"Standardabweichung: {std_temp:.2f} °C")

# --- 3. Plot erstellen ---
if not os.path.exists("plots"):
    os.makedirs("plots")

plt.figure(figsize=(8,5))
plt.plot(df['time_s'], df['temperature_C'], marker='o', linestyle='-')
plt.title("Temperatur über Zeit")
plt.xlabel("Zeit [s]")
plt.ylabel("Temperatur [°C]")
plt.grid(True)

plot_file = "plots/temperature_plot.png"
plt.savefig(plot_file)
plt.show()
print(f"Plot gespeichert: {plot_file}")

# --- 4. Histogramm ---
plt.figure(figsize=(6,4))
plt.hist(df['temperature_C'], bins=10, color='skyblue', edgecolor='black')
plt.title("Histogramm der Temperatur")
plt.xlabel("Temperatur [°C]")
plt.ylabel("Häufigkeit")
plt.grid(True)
hist_file = "plots/temperature_hist.png"
plt.savefig(hist_file)
plt.show()
print(f"Histogramm gespeichert: {hist_file}")
