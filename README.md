# College_Cooking_Sourcecode

## Title - 論文タイトル
**An Influence of Reference Group on the Cooking Habit of University Students**  
（学生の自炊習慣の違いにおける準拠集団の影響）

## Abstract - 概要

このリポジトリは、以下の研究論文で使用した分析コードを収録したものです：

> 古川瑠璃, スワン聖里奈, 遊橋裕泰 (2024).  
> *学生の自炊習慣の違いにおける準拠集団の影響.*  
> スマートライフ学会2024年大会発表

本研究では、異なる住環境にある大学生の自炊習慣について、準拠集団の影響を重回帰分析およびt検定により明らかにしました。

## Data - データについて

本研究に使用したデータは、**個人情報を含む収集データであり、再配布はできません**。  
ただし、分析コードは**任意のCSV形式の表データで再現可能**です。以下の構造を参考にしてください。

**Example of Data Structure - データ構造の例**
```csv
id, 現在の居住状況について / Current living condition, あなたの自炊を行う頻度について教えてください/ How often do you cook for yourself in a week?, 他の寮生が自炊するのをよく見ますか/ How often do you see other residents cooking in the kitchen?, 仲の良い友達や家族と自炊についての話をしますか / Do you often talk with your close friends or your family about cooking?, 【自炊を行う】理由 / The reasons why you cook for yourself
1, 寮生活, 週4~6/ 4~6 times per week, よく見る / often, 時々する / sometimes, 節約したいから / To save money
2, 実家暮らし, 週2~3 / 2~3times per week, たまに見る / sometimes, ほとんどしない / rarely, 料理の腕を上げたいから / To improve cooking skills
...
```

## Repository Structure - リポジトリ構成
College_Cooking_Sourcecode/  
├── data/  
│   └── sample_format.csv  
├── Source_Code/  
│   ├── Multiple_linear_regression_talk_and_see.py  
│   ├── Multiple_linear_regression_whycook.py  
│   └── ttest_on_frequency_of_cooking.py  
├── requirements.txt  
├── LICENSE  
└── README.md

## How to Implement - 実行方法

1. Python環境の準備
```bash
pip install -r requirements.txt
```
2. 分析スクリプトの実行
```bash
# Conduct t-test (example)
python Source_Code/ttest_on_frequency_of_cooking.py
```

## 再現性

個人情報を含むデータのため、再現には自身でデータを準備する必要があります。

## License - ライセンス
MIT License
