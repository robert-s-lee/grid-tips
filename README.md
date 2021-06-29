These are unofficial [Grid.ai](https://grid.ai/) examples. Please refer to Grid.ai [docs](https://docs.grid.ai) for the latest.  View using [GitHub Pages](https://robert-s-lee.github.io/grid-tips/)

# Examples

These are a collection of Grid.ai Run Badge ![Grid.ai Run Badge](https://img.shields.io/badge/rid_AI-run-78FF96.svg?labelColor=black&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEgMTR2MjBhMTQgMTQgMCAwMDE0IDE0aDlWMzYuOEgxMi42VjExaDIyLjV2N2gxMS4yVjE0QTE0IDE0IDAgMDAzMi40IDBIMTVBMTQgMTQgMCAwMDEgMTR6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTM1LjIgNDhoMTEuMlYyNS41SDIzLjl2MTEuM2gxMS4zVjQ4eiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==) examples. The Badge allows one click reproduction of an experiment.  It is so easy these experiments can be kicked off from an iPhone.

## Web UI Links

| Category    | Description | Grid.ai Run Link                    |
| ----------- | ----------- | ------------------------------------|
| [Time Series](https://docs.grid.ai/examples/time-series) | [Coin Market Price Forecasting](https://github.com/gridai/gridai-timeseries-forecasting-demo/tree/rslee-datastore-optional)       | - [`rslee-datastore-optional` branch](https://platform.grid.ai/#/runs?script=https://github.com/gridai/gridai-timeseries-forecasting-demo/blob/1ec5e00aec3a5d0e58c98c7c1ece8f992a60aa40/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0), <br/> <br/> - [15x Paralle Hyperparameter sweep --learning_rate "uniform(0,0.03,5)" --hidden_size "[16,32,64]"](https://platform.grid.ai/#/runs?script=https://github.com/gridai/gridai-timeseries-forecasting-demo/blob/1ec5e00aec3a5d0e58c98c7c1ece8f992a60aa40/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0%20--learning_rate%20"uniform(0,0.03,5)"%20--hidden_size%20"[16,32,64]") |
| [NLP](https://docs.grid.ai/examples/nlp)         | [Text Classification](https://github.com/robert-s-lee/grid-text-classification/tree/rslee-add-default-download)        | [`rslee-add-default-download` branch](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-text-classification/blob/5203fdeaf4226195c743374b0732b33c3b26264b/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0%20--max_epochs=1) |
| [Vision](https://docs.grid.ai/examples/vision) | [Kinetics Video Classification](https://github.com/aribornstein/KineticsDemo) | [`main` branch](https://platform.grid.ai/#/runs?script=https://github.com/aribornstein/KineticsDemo/blob/8d4137f302d08ccc25286c49def65d8db8426243/train.py&cloud=grid&use_spot&instance=g4dn.2xlarge&accelerators=1&gpus=1&framework=lightning&script_args=train.py%20--gpus=1%20--fast_dev_run=1)
| 3rd Party | [Optuna](https://github.com/robert-s-lee/grid-optuna) | - [Single Run](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-optuna/blob/dbb7c20cad6bfb419a037f8ff93cb9774fedb2e5/pytorch_lightning_simple.py&cloud=grid&use_spot&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning), <br/> <br/> - [8x Parallel Hyperparameter Sweeps](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-optuna/blob/dbb7c20cad6bfb419a037f8ff93cb9774fedb2e5/pytorch_lightning_simple.py&cloud=grid&use_spot&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=pytorch_lightning_simple.py%20--pruning%20"[0,1]"%20--batchsize%20"[32,128]"%20--epochs%20"[5,10]") |
|  |  | 


## CLI Runs
Environment is set up by sourcing [`. gridenv`](examples/gridenv.sh).  CLI equivalent can are in [here](examples/README.md).

# Tips
- [How to troubleshoot Grid.ai CLI](troubleshooting/README.md)
- [How to create Grid.ai Run Badge](sharing-runs/README.md)

