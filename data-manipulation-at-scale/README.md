# Data Manipulation at Scale


## Notes

* Big in "Big Data" refers to challenge, not to size (hard to manage, hard do extract useful stuff)


### Relational Databases/Algebra

* Great simplicity and symmetry on the relational algebra (input/output are always sets)
* Favors composition of functions (queries), reminds me of functional programming and unix pipes
* Views can isolate users from the underlying schema as SQL isolates from data internal representation
* Views are a zero cost abstraction
* SQL is good for needle on the haystack problems
* Indexing works very well, log(N) rlz
* As data gets larger, polynomial algorithms wont cut it, you need linear stuff (n * log(n)).
