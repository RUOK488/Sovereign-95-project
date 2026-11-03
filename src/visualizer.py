import matplotlib.pyplot as plt
import pandas as pd

class EnergyVisualizer:
    @staticmethod
    def plot_trends(df: pd.DataFrame):
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(df["Month"], df["Units_Consumed"], marker="o", color="b", linestyle="-")
        plt.title("Monthly Energy Consumption (kWh)")
        plt.xlabel("Month")
        plt.ylabel("Units (kWh)")
        plt.grid(True)

        plt.subplot(1, 2, 2)
        plt.bar(df["Month"], df["Total_Bill"], color="orange")
        plt.title("Monthly Bill Amount ($)")
        plt.xlabel("Month")
        plt.ylabel("Cost ($)")
        plt.grid(axis="y")

        plt.tight_layout()
        plt.show()
