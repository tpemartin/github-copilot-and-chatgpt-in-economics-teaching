# Ordinary Least Squares (OLS) Regression

## Model 

Consider the following linear model:
$$
y_i = \beta_0 + \beta_1 x_i + \epsilon_i
$$
where $y_i$ is the dependent variable, $x_i$ is the independent variable, and $\epsilon_i$ is the error term.

> `$$` 表示要插入數學公式，再透過按enter換行，提示copilot要的是數學公式。

The model has several assumptions on the error term $\epsilon_i$:
* $\mathbb{E}[\epsilon_i] = 0$
* $\mathbb{E}[\epsilon_i | x_i] = 0$
* $\mathbb{E}[\epsilon_i^2 | x_i] = \sigma^2$
* $\epsilon_i$ is independent of $x_i$
* $\epsilon_i$ is independent of $\epsilon_j$ for $i \neq j$
* $\epsilon_i$ is normally distributed

> `*`再空一格提示copilot要的是列點。教師要自行判斷何時要停止列點。

## Estimation in R

We use the `lm()` function to estimate the model. The first argument is the formula, and the second argument is the data frame.

```r
# estimate the model
model = lm(y ~ x, data = data)
```