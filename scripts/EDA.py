import os
import sys
import click
import pandas as pd
import altair as alt

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.numeric_cols import create_numeric_cols_chart



@click.command()
@click.option('--input_filepath', type=str, help="Path to raw data")
@click.option('--output_filepath', type=str, help="Path to directory where processed data csv will be written to")



def main(input_filepath, output_filepath):
    
    #reading and 
    data = pd.read_csv(input_filepath, encoding="utf-8")
    data_description= data.describe().T
    data_description = data_description.reset_index().rename(columns={'index': 'variable'})
    pd.DataFrame(data_description).to_csv(os.path.join(output_filepath, "tables", "description.csv"), index=False)
    print(data_description)

    #finding missing value
    zero_val = (data == 0.00).astype(int).sum(axis=0)
    mis_val = data.isnull().sum()
    mis_val_percent = 100 * data.isnull().sum() / len(data)
    mz_table = pd.concat([zero_val, mis_val, mis_val_percent], axis=1)
    mz_table = mz_table.rename(
    columns = {0 : 'Zero Values', 1 : 'Missing Values', 2 : '% of Total Values'})
    mz_table['Total Zero Missing Values'] = mz_table['Zero Values'] + mz_table['Missing Values']
    mz_table['% Total Zero Missing Values'] = 100 * mz_table['Total Zero Missing Values'] / len(data)
    mz_table['Data Type'] = data.dtypes
    mz_table = mz_table[
        mz_table.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(1)
    print ("Your selected dataframe has " + str(data.shape[1]) + " columns and " + str(data.shape[0]) + " Rows.\n"      
           "There are " + str(mz_table.shape[0]) +
              " columns that have missing values.")
    mz_table = mz_table.reset_index().rename(columns={'index': 'variable'})
    pd.DataFrame(mz_table).to_csv(os.path.join(output_filepath, "tables", "missing_values.csv"), index=False)

    # correlation
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
    correlation_matrix = data[numeric_columns].corr().abs()
    correlation_df = correlation_matrix.reset_index().rename(columns={'index': ''})
    correlation_df.columns = correlation_df.columns.astype(str)
    correlation_df = correlation_df.rename_axis('', axis=1)
    correlation_df.to_csv(os.path.join(output_filepath, "tables", "correlation.csv"), index=False)



    #numeric distribution
    numeric_cols = ["MONTH", "DAY", "HOUR", "MINUTE"]
    numeric_plot = create_numeric_cols_chart(data, numeric_cols)
    numeric_plot.save(os.path.join(output_filepath, "figures", "numeric_dist.png"))

    #categrical distribution
    categ_cols_dist = alt.Chart(data).mark_bar().encode(
    y = alt.X(alt.repeat(),type= "nominal").sort("x"),
    x =alt.Y("count()"),).properties(
        width = 400,
        height = 300).repeat(
     ["TYPE", "NEIGHBOURHOOD"],
    columns = 1)

    categ_cols_dist.save(os.path.join(output_filepath, "figures", "categ_dist.png"))
    

if __name__ == '__main__':
    main()
