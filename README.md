 
# Examples

## Web UI Links

| Category    | Description | Grid.ai Run Link                    |
| ----------- | ----------- | ------------------------------------|
| [Time Series](https://docs.grid.ai/examples/time-series) | [Coin Market Price Forecasting](https://docs.grid.ai/examples/time-series/price-forecasting)       | [`rslee-datastore-optional` branch](https://platform.grid.ai/#/runs?script=https://github.com/gridai/gridai-timeseries-forecasting-demo/blob/1ec5e00aec3a5d0e58c98c7c1ece8f992a60aa40/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0) |
| [NLP](https://docs.grid.ai/examples/nlp)         | [Text Classification](https://docs.grid.ai/examples/nlp/text-classification)        | [`rslee-add-default-download` branch](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-text-classification/blob/5203fdeaf4226195c743374b0732b33c3b26264b/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0%20--max_epochs=1) |
| [Vision](https://docs.grid.ai/examples/vision) | [Kinetics Video Classification](https://docs.grid.ai/examples/vision/kinetics-video-classification) | [`main` branch](https://platform.grid.ai/#/runs?script=https://github.com/aribornstein/KineticsDemo/blob/8d4137f302d08ccc25286c49def65d8db8426243/train.py&cloud=grid&use_spot&instance=g4dn.2xlarge&accelerators=1&gpus=1&framework=lightning&script_args=train.py%20--gpus=1%20--fast_dev_run=1)
| 3rd Party | Optuna | [Single Run](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-optuna/blob/dbb7c20cad6bfb419a037f8ff93cb9774fedb2e5/pytorch_lightning_simple.py&cloud=grid&use_spot&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning), [8x Parallel Hyperparameter Sweeps](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-optuna/blob/dbb7c20cad6bfb419a037f8ff93cb9774fedb2e5/pytorch_lightning_simple.py&cloud=grid&use_spot&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=pytorch_lightning_simple.py%20--pruning%20"[0,1]"%20--batchsize%20"[32,128]"%20--epochs%20"[5,10]") |

## CLI Runs
Environment is set up by sourcing [`. gridenv`](examples/gridenv.sh).  CLI equivalent can are in [here](examples/README.md).

# Tips
- [How to troubleshoot Grid.ai CLI](troubleshooting/README.md)
- [How to create Grid.ai Run Badge](sharing-runs/README.md)

