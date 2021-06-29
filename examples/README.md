



# [Time Series](https://docs.grid.ai/examples/time-series/price-forecasting)

Run with Grid.ai WebUI

**NOTE**: 
- Use `rslee-datastore-optional` branch
- Use Spot Instance if desired

[![Single Run](https://img.shields.io/badge/rid_AI-run-78FF96.svg?labelColor=black&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEgMTR2MjBhMTQgMTQgMCAwMDE0IDE0aDlWMzYuOEgxMi42VjExaDIyLjV2N2gxMS4yVjE0QTE0IDE0IDAgMDAzMi40IDBIMTVBMTQgMTQgMCAwMDEgMTR6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTM1LjIgNDhoMTEuMlYyNS41SDIzLjl2MTEuM2gxMS4zVjQ4eiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==)](https://platform.grid.ai/#/runs?script=https://github.com/gridai/gridai-timeseries-forecasting-demo/blob/1ec5e00aec3a5d0e58c98c7c1ece8f992a60aa40/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0)


```bash
git clone https://github.com/gridai/gridai-timeseries-forecasting-demo
cd gridai-timeseries-forecasting-demo
git switch rslee-datastore-optional
gridenv 

python train.py --gpus 0 --max_epochs 1
grid run train.py --gpus 0
```

# [Text Classification](https://docs.grid.ai/examples/nlp/text-classification)

Run with Grid.ai WebUI
**NOTE**: 
- Use `rslee-add-default-download` branch
- Use Spot Instance if desired


[![Single Run](https://img.shields.io/badge/rid_AI-run-78FF96.svg?labelColor=black&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEgMTR2MjBhMTQgMTQgMCAwMDE0IDE0aDlWMzYuOEgxMi42VjExaDIyLjV2N2gxMS4yVjE0QTE0IDE0IDAgMDAzMi40IDBIMTVBMTQgMTQgMCAwMDEgMTR6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTM1LjIgNDhoMTEuMlYyNS41SDIzLjl2MTEuM2gxMS4zVjQ4eiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==)](https://platform.grid.ai/#/runs?script=https://github.com/robert-s-lee/grid-text-classification/blob/5203fdeaf4226195c743374b0732b33c3b26264b/train.py&cloud=grid&instance=t2.medium&accelerators=1&disk_size=200&framework=lightning&script_args=train.py%20--gpus=0%20--max_epochs=1)

Run with Grid.ai CLI

```bash
git clone https://github.com/robert-s-lee/grid-text-classification
cd grid-text-classification
git switch rslee-add-default-download
gridenv 

python train.py --gpus 0 --max_epochs 1
grid run train.py --gpus 0
```

# [KineticsDemo](https://docs.grid.ai/examples/vision/kinetics-video-classification)

Run with Grid.ai WebUI
**NOTE**: 
- Use Spot Instance if desired

[![Single Run](https://img.shields.io/badge/rid_AI-run-78FF96.svg?labelColor=black&logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iNDgiIGhlaWdodD0iNDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEgMTR2MjBhMTQgMTQgMCAwMDE0IDE0aDlWMzYuOEgxMi42VjExaDIyLjV2N2gxMS4yVjE0QTE0IDE0IDAgMDAzMi40IDBIMTVBMTQgMTQgMCAwMDEgMTR6IiBmaWxsPSIjZmZmIi8+PHBhdGggZD0iTTM1LjIgNDhoMTEuMlYyNS41SDIzLjl2MTEuM2gxMS4zVjQ4eiIgZmlsbD0iI2ZmZiIvPjwvc3ZnPg==)](https://platform.grid.ai/#/runs?script=https://github.com/aribornstein/KineticsDemo/blob/8d4137f302d08ccc25286c49def65d8db8426243/train.py&cloud=grid&use_spot&instance=g4dn.2xlarge&accelerators=1&gpus=1&framework=lightning&script_args=train.py%20--gpus=1%20--fast_dev_run=1)

Run with Grid.ai CLI

```bash
git clone https://github.com/aribornstein/KineticsDemo.git
cd KineticsDemo
gridenv 

python train.py --gpus=0 --fast_dev_run=1
grid run --instance_type=g4dn.2xlarge  --use_spot --gpus=1 train.py --gpus=1 --fast_dev_run=1
```

# References

## gridenv

``` bash
# setup conda environment
gridenv() {
  local name=${1:-$(basename -- $(pwd))}
  local pyver=${2:-3.7}
  local envexist=$(conda env list | grep "^${name}[ \t]*")
  [ -z "${envexist}" ] && conda create --yes --name ${name} python=${pyver}
  conda activate ${name}
  pip install lightning-grid --upgrade
  [ -f requirements.txt ] && pip install -r requirements.txt
  [ ! -z "${GRID_API}" ] && eval grid login $GRID_API
}
```
