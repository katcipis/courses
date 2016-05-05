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

There is two approaches to find the thetas to the linear regression algorithm, gradient descendent and
normal equation. Normal equation advantage is that it will find the best theta by setting the derivative to 0.
With one set of matrices operations you will find the best possible theta.

The disadvantage is exactly the matrices operations. There is two cases where you will have problems:

* You cant inverse the matrix (probably because of linear dependent stuff)
* The matrix is too bug, calculating the inverse of the matrix is O(N^3)
