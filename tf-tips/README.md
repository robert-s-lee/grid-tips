Why Build From source




conda create -n tf tensorflow

```
conda create -n tf python=3.8 tensorflow

Package python conflicts for:
python=3.8
tensorflow -> python[version='2.7.*|3.7.*|3.6.*|3.5.*']
tensorflow -> tensorboard[version='>=2.0.0'] -> python[version='>=2.7,<2.8.0a0|>=3.2|>=3.5|>=3|>=3.7,<3.8.0a0|>=3.6,<3.7.0a0|>=3.5,<3.6.0a0']
```

this version does not support early stop
```
conda create -n tf tensorflow

tensorboard==2.0.0
tensorflow==2.0.0
tensorflow-estimator==2.0.0

2021-08-01 09:11:17.449346: I tensorflow/core/platform/cpu_feature_guard.cc:145] This TensorFlow binary is optimized with Intel(R) MKL-DNN to use the following CPU instructions in performance critical operations:  SSE4.1 SSE4.2 AVX AVX2 FMA
To enable them in non-MKL-DNN operations, rebuild TensorFlow with the appropriate compiler flags.
```


```
pip install tensorflow

tensorflow==2.5.0
tensorflow-estimator==2.5.0

2021-07-30 17:15:53.481538: I tensorflow/core/platform/cpu_feature_guard.cc:142] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX2 FMA
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.

```



https://www.tensorflow.org/install/source

