import click
import pandas as pd

@click.command()
@click.argument('input_filepath')
@click.argument('output_filepath')
@click.argument('output_filepath_2')

def main(input_filepath, output_filepath,output_filepath_2 ):
    """Simple program that adds two numbers."""
    data = pd.read_csv(input_filepath, encoding="utf-8")
    data_info = data.info()
    pd.DataFrame(data_info).to_csv(output_filepath, index=False)
    data_description= data.describe().T
    pd.DataFrame(data_description).to_csv(output_filepath_2, index=False)

if __name__ == '__main__':
    main()
