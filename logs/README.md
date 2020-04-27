# logs
Manually altered calibration run files.

## Organization
- The repository is organized with a `xls_source` directory and the logs themselves, e.g. `a1_log.txt`.
- `xls_source` contains all of the `.xls` files which are edited to produce the log files

## Recommended Usage
- You should fill in the `.txt` format with tab separated values for import into the SQL system

## File Content
- The files contain four columns:
  - `run_num`: the run number to which the comment applies
  - `username`: the person adding the comment
  - `run_quality`: the type of run it is / why it's status is being modified from "normal"
  - `user_comment`: a user comment about the run
- This follows the paradigm laid out in the [run log proposal](http://ara.icecube.wisc.edu/wiki/index.php/Run_Log_Proposal).
