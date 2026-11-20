import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

FACTORS = ["unemployment", "median_income", "mental_distress", "mh_providers_rate"]

def baseline_predict(train, test):
    return np.full(len(test), train["overdose_rate"].mean())

def four_factor_predict(train, test, cols=FACTORS):
    X = np.column_stack([np.ones(len(train)), train[cols].values])
    beta, *_ = np.linalg.lstsq(X, train["overdose_rate"].values, rcond=None)
    Xt = np.column_stack([np.ones(len(test)), test[cols].values])
    return Xt @ beta

def cross_validate(df, predict_fns, n_splits=100, n_test=9, seed=42):
    rng = np.random.default_rng(seed)
    rmse = {name: [] for name in predict_fns}
    for _ in range(n_splits):
        idx = rng.permutation(len(df))
        test, train = df.iloc[idx[:n_test]], df.iloc[idx[n_test:]]
        y = test["overdose_rate"].values
        for name, fn in predict_fns.items():
            rmse[name].append(np.sqrt(np.mean((y - fn(train, test)) ** 2)))
    return pd.DataFrame(rmse)