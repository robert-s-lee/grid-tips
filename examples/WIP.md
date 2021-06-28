

# CocoDemo (Does not Work)

https://github.com/gridai/grid-docs/issues/38

```
git clone https://github.com/aribornstein/CocoDemo.git
cd CocoDemo
gridenv 
python train.py --gpus=0 --max_epochs=1
grid run train.py --gpus=0 --max_epochs=1


grid run \
--instance_type 1_v100_16gb \
--framework lightning \
--gpus 1 \
train.py \
--max_epochs 5 \
--gpus 1

```

