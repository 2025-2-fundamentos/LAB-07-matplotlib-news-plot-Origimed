"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.

    """

    import os

    import matplotlib.pyplot as plt
    import pandas as pd

    input_path = os.path.join("files", "input", "news.csv")
    output_dir = os.path.join("files", "plots")
    output_path = os.path.join(output_dir, "news.png")

    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(input_path)

    if "Unnamed: 0" in df.columns:
        df = df.rename(columns={"Unnamed: 0": "Year"})

    x = df["Year"]
    cols = [c for c in df.columns if c != "Year"]

    plt.figure()
    for col in cols:
        plt.plot(x, df[col], marker="o", label=col)

    plt.xlabel("Year")
    plt.ylabel("Percentage")
    plt.title("News consumption by medium")
    plt.legend()
    plt.tight_layout()

    plt.savefig(output_path)
    plt.close()

