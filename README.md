# Global Happiness Report Analysis

## About the project
This is a simple Python project for analysing the World Happiness Report dataset.

The main aim is to understand how GDP, social support and healthy life expectancy are related to the happiness score of different countries.

## Dataset
Download the World Happiness Report dataset from Kaggle:

https://www.kaggle.com/datasets/unsdsn/world-happiness

After downloading, keep the CSV file in the same folder as the Python program and rename it to:

`world_happiness.csv`

The program uses these columns:
- Country name
- Life Ladder
- Log GDP per capita
- Social support
- Healthy life expectancy at birth

If your downloaded CSV has different column names, you may need to change the column names in the Python file.

## Requirements
Install Python and these libraries:

```bash
pip install pandas matplotlib seaborn
```

## How to run
1. Keep `global_happiness.py` and `world_happiness.csv` in the same folder.
2. Open the folder in VS Code or terminal.
3. Run this command:

```bash
python global_happiness.py
```

## What the program does
1. Reads the CSV dataset.
2. Displays the first few rows and missing values.
3. Removes rows with missing values in the main columns.
4. Finds the top 10 and bottom 10 happiest countries.
5. Makes graphs to compare happiness with:
   - GDP per capita
   - Social support
   - Healthy life expectancy
6. Displays the correlation values.

## Output
The program creates these graph images:
- `top_10_happiest_countries.png`
- `gdp_vs_happiness.png`
- `social_support_vs_happiness.png`
- `life_expectancy_vs_happiness.png`

## Conclusion
The graphs and correlation values help us see whether GDP, social support and life expectancy have a relationship with happiness. This project is only for basic data analysis and does not prove that these factors directly cause happiness.
