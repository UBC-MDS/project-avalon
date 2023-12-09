.PHONY: all clean

all : docs/index.html

# Read raw data and perform EDA and output figures and tables
results/tables/description.csv \
results/tables/missing_values.csv \
results/tables/correlation.csv \
results/figures/numeric_dist.png \
results/figures/categ_dist.png : \
data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv
	python scripts/EDA.py \
	--input_filepath=data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv \
	--output_filepath=results/

# split and preprocess data
data/processed/preprocessed_data_full.csv \
data/processed/preprocessed_data_head.csv \
data/processed/preprocessed_theft_from_vehicle_full.csv \
data/processed/preprocessed_theft_from_vehicle_head.csv \
data/processed/preprocessed_theft_from_vehicle_info.csv : \
data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv
	python scripts/split_n_preprocess.py \
	--raw-data=data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv \
	--data-to=data/processed/

# make forecasting and save results as csv
results/tables/all_predictions.csv : \
data/processed/preprocessed_theft_from_vehicle_full.csv
	python scripts/modelling.py \
	--preprocessed_data=data/processed/preprocessed_theft_from_vehicle_full.csv \
	--results_folder=results/

# plot out prediction results
results/figures/original_plot.png \
results/figures/arima_prediction_plot.png \
results/figures/es_prediction_plot.png \
results/figures/sma_prediction_plot.png : \
results/tables/all_predictions.csv
	python scripts/prediction_plot.py \
	--prediction_df=results/tables/all_predictions.csv \
	--results_folder=results/

# evaluate model on test data and save results
results/figures/autocorrelation_plot.png results/figures/autocorrelation_with_diff_plot.png : \
data/processed/preprocessed_theft_from_vehicle_full.csv
	python scripts/autocorrelation_plot.py \
	--preprocessed_data=data/processed/preprocessed_theft_from_vehicle_full.csv \
	--results_folder=results/

# find final metric
results/tables/observations.csv : results/tables/all_predictions.csv
	python scripts/get_metrics.py \
	--predictions_data=results/tables/all_predictions.csv \
	--results_folder=results/

# build HTML report and copy build to docs folder
docs/index.html : results/tables/description.csv \
results/tables/missing_values.csv \
results/tables/correlation.csv \
results/tables/all_predictions.csv \
results/tables/observations.csv \
results/figures/es_prediction_plot.png \
results/figures/categ_dist.png \
results/figures/arima_prediction_plot.png \
results/figures/autocorrelation_with_diff_plot.png \
results/figures/autocorrelation_plot.png \
results/figures/original_plot.png \
results/figures/numeric_dist.png\
results/figures/sma_prediction_plot.png \
data/processed/preprocessed_data_head.csv \
data/processed/preprocessed_theft_from_vehicle_full.csv \
data/processed/preprocessed_theft_from_vehicle_head.csv
	jupyter-book build --builder html ./report && \
	rm -rf ./docs && \
	cp -rf ./report/_build/html ./docs && \
	touch ./docs/.nojekyll && \
	jupyter-book clean report/ --all

clean :
	rm -rf docs/ && \
	rm -f data/processed/* && \
	rm -f results/figures/* &&\
	rm -f results/tables/*
