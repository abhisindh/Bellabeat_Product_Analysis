![top line](../Resources/Images/topLine.png)
# ChangeLog
All notable changes to the data in this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.3] - 2022-07-25
### Modified
 - Sleep : Changed the formatting of `SleepDay` column.
### Added
 - Sleep : Added a `date` column with different formatting.

## [1.0.2] - 2022-07-25
### Modified
 - Intensities : Changed the formatting of `ActivityDate` column.


## [1.0.1] - 2022-07-24
### Modified
 - Activity : Changed the formatting of `ActivityDate` column.
### Added
 - Activity : Added a `date` column with different formatting.



   











 <!-- ![](https://img.shields.io/badge/-unreleased-lightgrey)

## [1.7.3] - 2022-06-22
### Bugfix
 - Fix incompatibility with GitLab 15

## [1.7.2] - 2022-02-16
### Modified
 - Add a template for terraform deployment to staging and production.

## [1.7.1] - 2022-01-21
### Modified
 - PyPi release: ensure that dangling publish jobs are not created on MR pipelines.
 - PyPi release: allow distribution location to be updated using variables.

## [1.7.0] - 2021-10-27
### Modified
 - Tox tests: removing the usage of a custom gemnasium image as this is no longer needed.

## [1.6.0] - 2021-08-10
### Modified
 - Make terraform lint use variables and thus allow overriding of version and/or docker image
 - Update default lint version to 1.0.4

## [1.5.0] - 2021-03-24
### Modified
 - Tox tests: allow a custom image to be used in tox test job through `TOX_IMAGE_BUILD_COMMAND`.

## [1.4.0] - 2021-03-18
### Modified
 - Deployment: perform Django migrations before deploying to cloud run.

## [1.3.0] - 2021-02-08
### Modified
 - Terraform lint: Fixed the version of Terraform used for linting to 0.14.6.

## [1.2.0] - 2020-12-17
### Added
 - Deployment: A new template added to allow multiple cloud run services to be deployed as part
    of a single deployment project.

## [1.1.5] - 2020-12-11
### Added
 - Terraform lint: Added `-diff` flag

## [1.1.4] - 2020-12-04
### Modified
 - Terraform lint: Fixed the version of Terraform used for linting to 0.13.5.

## [1.1.3] - 2020-12-02
### Added
 - Deployment: allow gitlab deploy environment to be overridden by downstream jobs in
   [deployment CI template job](https://gitlab.developers.cam.ac.uk/uis/devops/continuous-delivery/ci-templates/-/blob/master/auto-devops/deploy.yml)

## [1.1.2] - 2020-11-24
### Fixed
 - Deployment: fixed variable interpolation so that `SERVICE_PREFIX` is used for all variables
   which are required to be set downstream in [deployment CI template job](https://gitlab.developers.cam.ac.uk/uis/devops/continuous-delivery/ci-templates/-/blob/master/auto-devops/deploy.yml)

## [1.1.1] - 2020-09-21
### Added
 - Deployment: Added a
   [deployment CI template job](https://gitlab.developers.cam.ac.uk/uis/devops/continuous-delivery/ci-templates/-/blob/master/auto-devops/deploy.yml)
   that provides jobs for deploying a previously built Docker image to Cloud Run on Google Cloud Platform (GCP).
 - Terraform lint: Added a
   [Terraform lint CI template job](https://gitlab.developers.cam.ac.uk/uis/devops/continuous-delivery/ci-templates/-/blob/master/auto-devops/terraform-lint.yml)
   to run `terraform fmt` on Terraform configuration files in the local repository.

## [1.1.0] - 2020-08-26
### Modified
 - PEP8: Modified the
   [PEP8 CI template job](https://gitlab.developers.cam.ac.uk/uis/devops/continuous-delivery/ci-templates/-/blob/master/auto-devops/pep8.yml)
   to be uninterruptible, and to only run for pipelines other than merge
   request pipelines.
 - Tox tests: Modified the
   [Tox tests template](https://gitlab.developers.cam.ac.uk/uis/devops/continuous-delivery/ci-templates/-/blob/master/auto-devops/tox-tests.yml)
   to make the `d
ocumentation` job run for pipelines other than merge request
   pipelines (previously the job was never running due to a bug in the job
   rules).

## [1.0.1] - 2020-08-06
### Added
 - pypi-release: Added generic stand along jobs designed to allow easy upload of
   Python packages to PyPI. 

 ![](https://img.shields.io/badge/-released-orange)  
  -->
