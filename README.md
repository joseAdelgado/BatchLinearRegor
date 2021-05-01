# `BatchLinearRegor` ![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
A Py3 code that implements batch linear regressor using gradient descent.

## Math path

![GD](https://github.com/ranjiGT/BatchLinearRegor/blob/main/mathpath1.png)

Parameters:
- **threshold** - The threshold, that the change in error has to fall below, before the algorithm terminates.
- **data** - The location of the data file (e.g. /media/data/yacht.csv).
- **eta** - The learning rate of the gradient descent approach.

Start your program in the following way:
`python3 student.py --data random.csv --eta 0.0001 --threshold 0.0001`

## Output 
![OP1](https://github.com/ranjiGT/BatchLinearRegor/blob/main/op1.png)

## Bonus
[![GD](https://img.youtube.com/vi/8zb9nsi8KzA/maxresdefault.jpg)](https://youtu.be/8zb9nsi8KzA)

## Standard release

A build of the same problem statement with only using standard libararies is available at the release section.

## Run Dockerfile 

`docker run -it python-regor1 python3 bregressorv2.py --data random1.csv --eta 0.0001 --threshold 0.0001`
