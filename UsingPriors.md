Using [makeprior](http://sourceforge.net/apps/trac/lemur/wiki/makeprior):

```
The "MakePrior" application allows you to add document prior values into an existing Indri index.

The command to run "makeprior" is:
  makeprior <parameter_file>

Where the parameter file is a well-formed XML file (wrapped in <parameters> </parameters> tags) and contains the following fields:
  index: path to an Indri Repository.
  name: the name for the prior (i.e. what the prior will be referred to as in Indri queries).
  input: path to the input file for this prior. The input file should contain a list of entries containing first an external document id and second a log probability value. There should be one entry per line of the file.
  memory: an integer value specifying the number of bytes to use for the table building process. The value can include a scaling factor by adding a suffix. Valid values are (case insensitive) K=1000, M=1000000, G=1000000000. So 100M would be equivalent to 100000000. The value should contain only decimal digits and the optional suffix.
```


Computing the factor of boost 2 for the focused set (10280) in relation to the rest (21466) out of the total (31746).

![http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%0A%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2010280%20%5Ccdot%20x%20%2B%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2021466%20%5Ccdot%20y%20%3D%201%0A%5C%5C%0Ax%20%3D%204%20%5Ccdot%20y%0A%5Cend%7Bmatrix%7D%5Cright.%0A&nonsense=.png](http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%0A%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2010280%20%5Ccdot%20x%20%2B%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2021466%20%5Ccdot%20y%20%3D%201%0A%5C%5C%0Ax%20%3D%204%20%5Ccdot%20y%0A%5Cend%7Bmatrix%7D%5Cright.%0A&nonsense=.png)

![http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20x%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B31746%7D%7B21013%7D%20%5Cright%20)%20%5Capprox%20-9.9528%0A&nonsense=.png](http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20x%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B31746%7D%7B21013%7D%20%5Cright%20)%20%5Capprox%20-9.9528%0A&nonsense=.png)

![http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20y%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B15873%7D%7B21013%7D%20%5Cright%20)%20%5Capprox%20-10.6460%0A&nonsense=.png](http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20y%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B15873%7D%7B21013%7D%20%5Cright%20)%20%5Capprox%20-10.6460%0A&nonsense=.png)


Computing the factor of boost 4 for the focused set (10280) in relation to the rest (21466) out of the total (31746).

![http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%0A%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2010280%20%5Ccdot%20x%20%2B%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2021466%20%5Ccdot%20y%20%3D%201%0A%5C%5C%0Ax%20%3D%202%20%5Ccdot%20y%0A%5Cend%7Bmatrix%7D%5Cright.%0A&nonsense=.png](http://chart.googleapis.com/chart?cht=tx&chl=%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%0A%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2010280%20%5Ccdot%20x%20%2B%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%2021466%20%5Ccdot%20y%20%3D%201%0A%5C%5C%0Ax%20%3D%202%20%5Ccdot%20y%0A%5Cend%7Bmatrix%7D%5Cright.%0A&nonsense=.png)

![http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20x%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B21164%7D%7B10431%7D%20%5Cright%20)%20%5Capprox%20-9.6580%0A&nonsense=.png](http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20x%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B21164%7D%7B10431%7D%20%5Cright%20)%20%5Capprox%20-9.6580%0A&nonsense=.png)

![http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20y%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B5291%7D%7B10431%7D%20%5Cright%20)%20%5Capprox%20-11.0442%0A&nonsense=.png](http://chart.googleapis.com/chart?cht=tx&chl=%0Alog%20%5Cleft%20(%20%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20y%20%5Cright)%20%3D%20log%20%5Cleft%20(%5Cfrac%7B1%7D%7B31746%7D%20%5Ccdot%20%5Cfrac%7B5291%7D%7B10431%7D%20%5Cright%20)%20%5Capprox%20-11.0442%0A&nonsense=.png)