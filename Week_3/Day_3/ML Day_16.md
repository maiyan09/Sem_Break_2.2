# Day 16 --- Introduction to Machine Learning Thinking

> Goal: Learn **how Machine Learning thinks** before using any ML
> libraries.

Machine Learning is not magic.

It follows a simple idea:

``` text
Input → Find Pattern → Prediction
```

Example:

If students study more, they usually score more.

A machine looks at examples and learns a pattern.

------------------------------------------------------------------------

# Real Life Example

Imagine these students:

  Study Hours   Exam Score
  ------------- ------------
  1             10
  2             20
  3             30
  4             40

Question:

What score might a student get if they study **5 hours**?

Possible prediction:

``` text
5 → 50
```

This is the basic idea behind Machine Learning.

------------------------------------------------------------------------

# 1. Dataset

A **dataset** is a collection of examples.

Example:

``` text
Study Hours | Score
1           | 10
2           | 20
3           | 30
```

Think:

Dataset = Previous experiences + examples.

------------------------------------------------------------------------

# 2. Feature

A **feature** is the input information.

Question:

What information are we using?

Answer:

``` text
Study Hours
```

Feature = Input.

------------------------------------------------------------------------

# 3. Label

A **label** is the value we want to predict.

Question:

What are we trying to know?

Answer:

``` text
Exam Score
```

Label = Output.

------------------------------------------------------------------------

# 4. Train vs Test

## Train

Use known examples:

``` text
1 → 10
2 → 20
3 → 30
```

Goal:

Find a pattern.

## Test

Try new input:

``` text
5 → ?
```

Prediction:

``` text
50
```

------------------------------------------------------------------------

# Mini Project --- Student Performance Predictor

No ML library.

Only prediction logic.

``` python
print("=== Student Performance Predictor ===")

study = int(input("Study Hours: "))

score = study * 10

if score > 100:
    score = 100

print("Predicted Score:", score)
```

Example:

``` text
Input:
6

Output:
Predicted Score: 60
```

------------------------------------------------------------------------

# Why This Is Not Real Machine Learning Yet

This project uses a fixed rule:

``` python
score = study * 10
```

Real ML learns the rule automatically.

------------------------------------------------------------------------

# Quick Quiz

1.  What is a dataset?
2.  What is a feature?
3.  What is a label?
4.  What is train/test?
5.  What will happen for study = 8?

------------------------------------------------------------------------

# Day 17 Checklist

-   [ ] I understand dataset
-   [ ] I understand feature
-   [ ] I understand label
-   [ ] I understand train/test
-   [ ] I built Student Performance Predictor

