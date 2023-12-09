## What's Changed
### version v1.0.0-rc1 - Date Dec 8, 2023

### Changes to address feedbacks
The issues we prioritized to resolve：
- https://github.com/UBC-MDS/data-analysis-review-2023/issues/16#issuecomment-1839700250
  ```
  1. HTML file: An HTML file is present, but I was unable to recreate it, and there were no provided examples on how to generate one.
  2. Tables: The tables in the report are not displayed correctly.
  3. Introduction and Conclusion: The introduction effectively outlines the main goal of the project as "predicting theft from vehicles in Vancouver using historical data". The report successfully demonstrates the analytical and modeling process. However, in the conclusion (or introduction), adding a concise overview of the major findings related to crime prediction, rather than just the model's performance, would be beneficial. This addition would highlight the research's significance, rather than just the model's.
  4. Data Analysis Section: In the section where you address missing data, it would be useful to briefly describe how you manage these missing values, whether by removal or through some form of data imputation.
  ```
  * Issue 1:
    * Update book rendering command in `README` and license information by @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/102
    * And make instructions clearer in `README` by @zywkloo in https://github.com/UBC-MDS/project-avalon/pull/122
  * Issue 2:
    * Change formatting content of tables by @phchen5 and @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/118
  * Issue 3:
    * Add findings and explanation in conclusion by @phchen5 in https://github.com/UBC-MDS/project-avalon/pull/116
  * Issue 4:
    * Clarify treatment of missing values in the notebook by @phchen5 in https://github.com/UBC-MDS/project-avalon/pull/117

- https://github.com/UBC-MDS/data-analysis-review-2023/issues/16#issuecomment-1840091441
  ```
  1. Introduction and conclusion: It is great that in the introduction part, you clearly state that "the primary objective of this project is to forecast instances of theft from vehicles in Vancouver by analyzing historical data", and the report shows clearly the process of analysis and modelling. But in the conclusion(or in the introduction), it would be better to consider adding a brief statement summarizing the key findings regarding the crime forecasting results, not just a conclusion of the performance of models. It could help to emphasize the importance of this research(not the importance of this model).
  
  2. README file: it would be nice to also show the author names here as well as the references in the README file.
  
  3. Data Analysis Section: When discussing missing values in the dataset, could be helpful to briefly mention your approach to handling these missing values. Are they dropped, or is there an imputation strategy in place?
  
  4. Tables in report: the report would be easier to read and look better displayed if tables could be well rendered.
  ```
  * Issue 1:
    * Add findings and explanation in conclusion by @phchen5 in https://github.com/UBC-MDS/project-avalon/pull/116 (same as above)
  * Issue 2:
    * Update README.md to place the author names in the front by @MoNorouzi23 in https://github.com/UBC-MDS/project-avalon/pull/113
  * Issue 3:
    * Clarify treatment of missing values in the notebook by @phchen5 in https://github.com/UBC-MDS/project-avalon/pull/117 (same as above)
  * Issue 4:
    * Change formatting content of tables by @phchen5 and @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/118  (same as above)
  
### Other changes
* Update README.md to include a better project summary by @zywkloo in https://github.com/UBC-MDS/project-avalon/pull/103
* Create CHANGELOG.md by @zywkloo in https://github.com/UBC-MDS/project-avalon/pull/121
* Fix: remove the extra dash in README.md by @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/115
* Remove unused imports in the notebook by @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/114
* Create `makefile` to compile a report by @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/120
* Add makefile workflow to docker by @SoloSynth1 in https://github.com/UBC-MDS/project-avalon/pull/123

**Full Changelog**: https://github.com/UBC-MDS/project-avalon/compare/v0.4.0...v1.0.0-rc1
