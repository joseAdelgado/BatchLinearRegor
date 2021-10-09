# `BatchLinearRegor` ![](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ranjiGT/pilot1/main?labpath=Assignment-01.ipynb)

A Py3 code that implements batch linear regressor using gradient descent.

## Math path
Write a Python code that implements batch linear regressor using gradient descent.

![GD](https://github.com/ranjiGT/BatchLinearRegor/blob/main/mathpath1.png)

Parameters:
- **threshold** - The threshold, that the change in error has to fall below, before the algorithm terminates.
- **data** - The location of the data file (e.g. /media/data/yacht.csv).
- **eta** - The learning rate of the gradient descent approach.

Start your program in the following way:
`python3 student.py --data random.csv --eta 0.0001 --threshold 0.0001`

## Output 
![OP1](https://github.com/ranjiGT/BatchLinearRegor/blob/main/op1.png)

![](https://github.com/ranjiGT/BatchLinearRegor/blob/main/shine.gif)

## Bonus
[![GD](https://img.youtube.com/vi/8zb9nsi8KzA/maxresdefault.jpg)](https://youtu.be/8zb9nsi8KzA)

```python
def regressor(dataset,eta,t):
    x, y, w = mat(dataset)
    costmat,res=[],[]
    key=0
    while True:
        currres=[]
        currres.append(key)
        key += 1
        cost = sqrerror(x,y,w)
        for ol in w:
            for il in ol:
                currres.append(il)
        currres.append(cost)
        costmat.append(cost)
        res.append(currres)
        w = w-(eta)*np.sum((x@w.T-y)*x,axis=0) #Gradient Calculation 

        if key>1:
            if (costmat[-2]-costmat[-1]) <= t:
                break
    return res
```

## Standard release

A build of the same problem statement with only using standard libraries is available at the release section.

## Run Dockerfile 

```docker
docker run -it python-regor1 python3 bregressorv2.py --data random1.csv --eta 0.0001 --threshold 0.0001
```
