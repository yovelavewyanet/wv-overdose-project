import numpy as np
import matplotlib.pyplot as plt

def plot_and_fit(df, x_col, y_col="overdose_rate", label=None):
    x, y = df[x_col].values, df[y_col].values
    r = np.corrcoef(x, y)[0, 1]
    slope, intercept = np.polyfit(x, y, 1)
    y_hat = slope * x + intercept
    r2 = 1 - np.sum((y - y_hat) ** 2) / np.sum((y - y.mean()) ** 2)
    plt.figure(figsize=(6, 4))
    plt.scatter(x, y)
    xs = np.linspace(x.min(), x.max(), 100)
    plt.plot(xs, slope * xs + intercept, color="red")
    plt.xlabel(label or x_col)
    plt.ylabel("Overdose deaths per 100,000")
    plt.title(f"r = {r:.2f}, R² = {r2:.2f}")
    plt.tight_layout()
    plt.show()
    return {"factor": x_col, "r": r, "slope": slope, "r2": r2}