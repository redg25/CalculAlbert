# CalculAlbert
At the moment simple script to generate random operations based on 4 parameters:
- Maximum result expected
- Number of numbers in the operations
- Operators to be used
- Range for each number of the oepration

The script returns a string representation of the operation and an integer as the result.<br>
<br>
Example:
```
# The result is maximum 20
# The operation includes 3 numbers
# The operators can be either + or -
# One is in the range [2:15], the 2 others in the range [2:10]
c1 = Calcul(20,3,['+','-'],[15,10])
print(c1.make_calcul())
```
```
# Returns a tuple with the string representation and the result
('3-2+12=', 13)
```

```
c2 = Calcul(200,4,['+','-','*','/'],[50,10])
print(c2.make_calcul())
('6/3*30-8=', 52)
```
Note: operators are selected randomly so even if you select 4 of them, you could end up with an operation with only one of a kind.
```
# Using the same parameters as for above
('7+3+4+38=', 52)
```
