import pandas as pd

df = pd.read_csv(r".\docs\data\clear\strikers\shooting.csv")

df[df["Goals"]>0].to_csv(r".\docs\data\clear\strikers\shooting_goals.csv", index=False)