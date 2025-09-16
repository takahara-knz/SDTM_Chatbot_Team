import pandas as pd
import os

# ファイル名の入力（拡張子なし）
filename_base = input("ファイル名（.xlsx不要）：").strip()

# 拡張子付きのファイル名
input_filename = filename_base + ".xlsx"
output_filename = filename_base + ".txt"

# Excelファイルを読み込む（最初のシート）
df = pd.read_excel(input_filename)

# NotebookLM用のテキスト出力
with open(output_filename, "w", encoding="utf-8") as f:
    for index, row in df.iterrows():
        for col in df.columns:
            f.write(f"{col}\n")
            f.write(f"{row[col]}\n")
        f.write("\n")  # レコードごとの空行