
---

# Crime Forecast in Vancouver
  - DSCI-522 Group 23
  - Alias: Project Avalon
  - 
## 🌟 Stakeholders

Our team, in alphabetical order:

- **Orix Au Yeung**
- **Ben Chen**
- **Mo Norouzi**
- **Yiwei Zhang**
    
Welcome to the repository for Project Avalon, a part of the DSCI-522 course by Group 23 in the MDS-V Cohort 8 at UBC.

## ⭐️ Project Summary

**Project Website:** <https://ubc-mds.github.io/project-avalon/>

This project aims to perform statistical analyses on the crimes committed in the City of Vancouver and develop a forecasting algorithm to forecast the number of crimes given a set of lagged values.

We created a model to estimate the frequency of vehicle break-ins each month in Vancouver. It uses historical data to inform its predictions, applying methods that consider both recent occurrences and long-established trends. The chosen approach has an average deviation of about 27 incidents per month from the actual numbers, which is notable given the substantial month-to-month variation in the incident counts. The model's current accuracy demonstrates its potential, and we anticipate that incorporating additional factors, such as weather patterns or significant city events, could enhance its predictive capabilities.

## 📘 Data Source

[Crime Data Download, the Vancouver Police Department](https://geodash.vpd.ca/opendata/)

## 📋 Dependencies

All required dependencies are listed in this [conda environment file](environment.yaml).

## 🧪 Test Automation

To run tests, execute the following command in the project root directory:
```
python3 tests/run_all_tests.py
```

## 🧑‍💻 How to run the notebook server

### Docker/Docker compose (recommended)

Link to [DockerHub Image](https://hub.docker.com/repository/docker/solosynth1/project-avalon/general)

1. Make sure Docker Engine/Desktop is installed and running.
1. Go to the project root folder.
2. Run `docker compose pull && docker compose up` to bring up the container.
4. Use browser to visit http://localhost:8888 and supply the generate token.

**Important Notes:**
- (For Docker Desktop users) The created container will require more than 4GB of RAM to run the analysis notebook. Please ensure the settings in Docker Desktop enables provisioning at least 8GB of RAM to the container.
- (For Apple Silicon users) Please enable the feature "Use Rosetta for x86/amd64 emulation on Apple Silicon" inside the setting menu. Otherwise, the kernel will not be properly run.

### Local conda environment
1. Create a new conda environment based on the provided [YAML file](environment.yaml).
  - Run `conda env create --name avalon --file=environment.yaml`
  - Then switch to `avalon` env by clicking the drop-down, and select `avalon`
    <img width="455" alt="image" src="https://github.com/UBC-MDS/project-avalon/assets/18610590/95c2c615-b7e3-42bd-93ad-a61861bd7d3a">
  - Note:
    - If you need the `avalon` env locally, run  `conda activate avalon`
    - If you added a new package in your local `environment.yaml`, you need to run `conda env update --name avalon --file=environment.yaml` to update your local env.
    - In case that jupyter does not recognize the new conda environment, Install ipykernel's kernel spec thru the following command:
```
conda activate avalon
python -m ipykernel install --user --name avalon --display-name "Python (avalon)"
```
2. Ensure all dependencies are installed.
3. Open Jupyter Notebook or JupyterLab to run the [analysis notebook](milestone_1.ipynb)

### 📔 Run the Scripts

Either in the docker environment/local conda environment, run the following command:

```shell
# Read raw data and perform EDA and output figures and tables
python scripts/EDA.py \
   --input_filepath=data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv \
   --output_filepath=results/

# split and preprocess data
python scripts/split_n_preprocess.py \
   --raw-data=data/raw/crimedata_csv_AllNeighbourhoods_AllYears.csv \
   --data-to=data/processed/

# make forecasting and save results as csv
python scripts/modelling.py \
   --preprocessed_data=data/processed/preprocessed_theft_from_vehicle_full.csv \
   --results_folder=results/ 

# plot out prediction results
python scripts/prediction_plot.py \
   --prediction_df=results/tables/all_predictions.csv \
   --results_folder=results/

# evaluate model on test data and save results
python scripts/autocorrelation_plot.py \
   --preprocessed_data=data/processed/preprocessed_theft_from_vehicle_full.csv \
   --results_folder=results/

# find final metric
python scripts/get_metrics.py \
   --predictions_data=results/tables/all_predictions.csv \
   --results_folder=results/

# build HTML report and copy build to docs folder
jupyter-book build --builder html ./report && \
rm -rf ./docs && \
cp -rf ./report/_build/html ./docs && \
touch ./docs/.nojekyll && \
jupyter-book clean report/ --all 
```

## 📌 Useful URLs

Here are some handy links for quick access:

- **Course Releases**: [DSCI_522 Course Releases](https://github.ubc.ca/MDS-2023-24/DSCI_522_dsci-workflows_students/tree/master/release)
- **Course Notes**: [Reproducible and Trustworthy Workflows for Data Science](https://ubc-dsci.github.io/reproducible-and-trustworthy-workflows-for-data-science/README.html)
- **Slack Channel**: [522_dsci-workflows on Slack](https://ubc-mds.slack.com/messages/522_dsci-workflows)
- **Our GitHub Project**: [Project Kaban](https://github.com/orgs/UBC-MDS/projects/86)
<img width="1439" alt="image" src="https://github.com/UBC-MDS/project-avalon/assets/18610590/9e46d78d-b383-4413-80a4-fac120a29658">


## 📖 License

All reports contained herein are licensed under the [Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License](https://creativecommons.org/licenses/by-sa/4.0/).
 See [the license file](LICENSE.md) for more information.

If re-using/re-mixing please provide attribution and link to this webpage.

The software code contained within this repository is licensed under the
MIT license. See [the license file](LICENSE.md) for more information.
