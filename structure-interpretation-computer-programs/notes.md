# Structure and Interpretation of Computer Programs 

## Framework for languages

* Primitives
* Composition
* Abstraction

LISP examples:

* Primitive: 1
* Composition: (+ 1 4 (- 2 3))
* Abstraction: (define (myfunc x) (* xx))

All languages are formed by these three, always analyse a language through this lenses.


## Iteration VS Linear recursion

Giving some cool examples, it is presented the idea of iteration and linear recursion.
It does not have anything to do with using recursive functions on the language, it is
the nature of the algorithm.

Even using recursion, if the nature is iterative you will have a fixed O(1) space
complexity. If the nature is recursive, space complexity will be N (for some N,
depending on the algorithm).

It seems to me that the iteration version is what is optimized to tail recursion, so even
if you have a recursion, the space complexity is O(1). Linear recursion would be when
you cant tail optimize and the space complexity linearly (or worse) grows.

Iterative add:

```
(define (add x y) 
    (if (= x 0) (y) (add (-1+ x) (1+ y))))
```

Linear recursive add:

```
(define (add x y) 
    (if (= x 0) (y) (1+ (add (-1+ x) (y))))
```

When you evaluate the linear recursive one, it will expand as big as X.
The iterative one has always the same size.

Iterative add:

```
(add 3 4)
(add 2 5)
(add 1 6)
(add 0 7)
7
```

Linear recursive add:

```
(add 3 4)
(1+ (add 2 4))
(1+ (1+ (add 1 4)))
(1+ (1+ (1+ (add 0 4))))
(1+ (1+ (1+ 4)))
(1+ (1+ 5))
(1+ 6)
7
```

## Cool Quick Stuff

* High order functions as a way to separate concerns, isolate changes, avoid duplication and express patterns (so much for OO)
* I found another human being that dislikes mathematical notation as me, got happy :-)
* Abstractions is a way to apply divide and conquer


## Interesting tasks

* Implement sieve of Eratosthenes
