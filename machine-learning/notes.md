# Intro

We have two kinds of machine learning:

* Classifiers (enumerate stuff)
* Regressions (generates numbers)

Course starts with linear regression and goes to polinomial regression.
Two concepts that helps on multi-variable linear regression:

* Scale the values (to eliminate big differences on the value of variables, remember the deformed contour plot :-)
* Mean normalization (like scaling, but make the mean value of all variables be 0)

Modeling house prices for example, there is a great difference of magnitude between age and size of the house.
This will make it harder to find the minimum global minimum of the cost function (J(theta)).
