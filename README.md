# College_Cooking_Sourcecode

## 論文タイトル（Paper Title）
**An Influence of Reference Group on the Cooking Habit of University Students**  
（学生の自炊習慣の違いにおける準拠集団の影響）

## 概要（Overview）

このリポジトリは、以下の研究論文で使用した分析コードを収録したものです：

> 古川瑠璃, スワン聖里奈, 遊橋裕泰 (2024).  
> *学生の自炊習慣の違いにおける準拠集団の影響.*  
> スマートライフ学会2024年大会発表

本研究では、異なる住環境にある大学生の自炊習慣について、準拠集団の影響を重回帰分析およびt検定により明らかにしました。

## データについて（Data Availability）

本研究に使用したデータは、**個人情報を含む収集データであり、再配布はできません**。  
ただし、分析コードは**任意のCSV形式の表データで再現可能**です。以下の構造を参考にしてください。

**データ構造の例：**
```csv
id, 現在の居住状況について / Current living condition, あなたの自炊を行う頻度について教えてください/ How often do you cook for yourself in a week?, 他の寮生が自炊するのをよく見ますか/ How often do you see other residents cooking in the kitchen?, 仲の良い友達や家族と自炊についての話をしますか / Do you often talk with your close friends or your family about cooking?, 【自炊を行う】理由 / The reasons why you cook for yourself
1, 寮生活, 週4~6/ 4~6 times per week, よく見る / often, 時々する / sometimes, 節約したいから / To save money
2, 実家暮らし, 週2~3 / 2~3times per week, たまに見る / sometimes, ほとんどしない / rarely, 料理の腕を上げたいから / To improve cooking skills
...

