## Image Building

Q: If a `grid run` is submitted with `--dockerfile` option, is the image built on the same instance type as the job?  i.e. `grid run --instance_type t2.medium --dockerfile custom.dockerfile script.py`, how is the image built?  Is the image built on a `t2.medium instance` or is the image building completely separate?

- Grid.ai image building process happens in a completely separate instance (CPU only; memory optimized). Experiment resources are not used in building the image 
