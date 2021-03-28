# BatchLinearRegor
A Py3 code that implements batch linear regressor using gradient descent.

Parameters:
- **threshold** - The threshold, that the change in error has to fall below, before the algorithm terminates.
- **data** - The location of the data file (e.g. /media/data/yacht.csv).
- **eta** - The learning rate of the gradient descent approach.

where ~xi is one data point (with N being the size of the data set),  the learning rate, yi
is the target output and f(~xi) is the linear function dened as f(~x) = ~wT ~x or equivalently
f(~x) =
P
i wi  xi. Whereas ~w and ~x include the bias/intercept, i.e. w0 (x0 is always 1).
All weights should be initialized as 0.
