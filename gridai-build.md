
## Execution Environment

By default, Grid.ai uses `conda` within `grid run` and `grid session`.  Within `grid run`, a custom `Dockerfile` specification be be provide wih an alternate execution environment, such as Poetry.  `conda` environment can be tailored using `requirements.txt`, `environment.yml`, and `config.yml`

Ranking in simplicity in usage (from simple to more complex),  requirements.txt, environment.yml, config.yml actions, and Dockerfile.

`grid run` has the following options:
- `--config FILENAME` 
Path to Grid config YML      
- `-d, --dockerfile FILENAME` 
Dockerfile for the image building
- `--dependency_file FILENAME`                                       Dependency file path. If not provided and if either `requirements.txt` or `environment.yml` is present in th current-working-directory, that'll be used

## Image Building

Q: If a `grid run` is submitted with `--dockerfile` option, is the image built on the same instance type as the job?  i.e. `grid run --instance_type t2.medium --dockerfile custom.dockerfile script.py`, how is the image built?  Is the image built on a `t2.medium instance` or is the image building completely separate?

- Grid.ai image building process happens in a completely separate instance (CPU only; memory optimized). Experiment resources are not used in building the image 
