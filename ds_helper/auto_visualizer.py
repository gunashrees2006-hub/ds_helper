import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from wordcloud import WordCloud

def visualize(df):
    for col in df.columns:
        if df[col].dtype in ['int64','float64']:
            fig, axes = plt.subplots(1, 3, figsize=(15, 4))
            sns.histplot(df[col], kde=True, ax=axes[0])
            sns.scatterplot(x=df.index, y=df[col], ax=axes[1])
            sns.boxplot(x=df[col], ax=axes[2])
            plt.suptitle(f"Numerical Column: {col}")
            plt.show()
        elif df[col].dtype == 'object' and df[col].nunique() < 20:
            fig, axes = plt.subplots(1, 2, figsize=(12, 4))
            sns.countplot(x=df[col], ax=axes[0])
            df[col].value_counts().plot(kind='bar', ax=axes[1])
            plt.suptitle(f"Categorical Column: {col}")
            plt.show()
        elif df[col].dtype == 'object':
            text = " ".join(str(x) for x in df[col].dropna())
            wc = WordCloud(width=800, height=400, background_color='white').generate(text)
            plt.figure(figsize=(10, 5))
            plt.imshow(wc, interpolation='bilinear')
            plt.axis("off")
            plt.title(f"Text Column: {col}")
            plt.show()
data = {
    "Age":[23,45,21,34,42,55],
    "Gender":["M","F","F","M","M","F"],
    "Remarks":["good","excellent","bad","average","good","bad"]
}
df = pd.DataFrame(data)
visualize(df)