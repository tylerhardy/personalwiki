# Operators
## Mathematic Operators
| Operator | Operation                         | Example   | Evaluates to... |
|----------|-----------------------------------|-----------|-----------------|
| `**`     | Exponent                          | `2 ** 3`  | `8`             |
| `%`      | Modulus/remainder                 | `22 % 8`  | `6`             |
| `//`     | Integer division/floored quotient | `22 // 8` | `2`             |
| `/`      | Division                          | `22 / 8`  | `2.75`          |
| `*`      | Multiplication                    | `3 * 5`   | `15`            |
| `-`      | Subtraction                       | `5 - 2`   | `3`             |
| `+`      | Addition                          | `2 + 2`   | `4`             |

- The order of operations (also called *precedence*) of Python math operators is similiar to that of mathematics.
- The `**` operator is evaluated first; the `*`, `/`, `//`, and `%` operators are evaluated next, from left to right; and the `+` and `-` operators are evaluated last (also from left to right). 
- You can use parentheses to override the usual precedence if you need to. 
- The meaning of an operator may change based on the data types of the values next to it.

## Comparison Operators
| Operator | Meaning                  |
|----------|--------------------------|
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater than             |
| `<=`     | Less than or equal to    |
| `>=`     | Greater than or equal to |

- The operators evaluate to `Ture` or `False` depending on the values you give them.

## Boolean Operators
### Boolean Basics
- The three Boolean operators (`and`, `or`, and `not`) are used to compare Boolean values.
- The `and` and `or` operators always take two Boolean values (or expressions), so they are considered *binary* operators
- **Order of precedence** applies to Boolean operators.
  * Python evaluates the `not` operators first, then the `and` operators, and then the `or` operators.
- When used in conditions `0`, `0.0`, and `''`(the empty string) are considered `False`
- When used in conditions all other values are considered `True`.
- Short-circuit operators is when both vars are true, `or` will return the **first** (as it only evaluates it), while `and` will return the **second**.
### Truth Table for `and`
| Expression        | Result  |
|-------------------|---------|
| `True and True`   | `True`  |
| `True and False`  | `False` |
| `False and True`  | `False` |
| `False and False` | `False` |

- The `and` operator evaluates an expression to `True` if both Boolean values are `True`; otherwise, it evaluates to False.

### Truth Table for `or`
| Expression        | Result  |
|-------------------|---------|
| `True or True`    | `True`  |
| `True or False`   | `True`  |
| `False or True`   | `True`  |
| `False or False`  | `False` |

- The `or` operator evaluates an expression to `True` if either of the two Boolean values is `True`. If both are `False`, it evaluates to `False`.

### Truth Table for `not`
| Expression    | Result  |
|---------------|---------|
| `not True`    | `False` |
| `not False`   | `True`  |

- The `not` operator operates on only one Boolean value (or expression). 
- The `not` operator simply evaluates to the opposite Boolean value.

## Augmented Assignment Operators
| Augmented Assignment Statement | Equivalent Assignment Statement|
|--------------------------------|--------------------------------|
| `var += 1` |  `var = var + 1`|
| `var -= 1` |  `var = var - 1`|
| `var *= 1` |  `var = var * 1`|
| `var /= 1` |  `var = var / 1`|
| `var %= 1` |  `var = var % 1`|

- The `+=` operator can do strings and list concatenation.
- The `*=` operator can do strings and list replication.
