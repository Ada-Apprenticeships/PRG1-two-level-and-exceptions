# Activity 1: Rows and columns

File: `rows_and_columns.py`

Fifteen minutes. A grid of numbers, and three ways of getting at it.

## Predict

Write down all three of the first block's outputs, then what each of the two
loops prints.

- `scores[1][2]`
- `len(scores)`
- `len(scores[0])`

## Run

Execute and compare.

## Investigate

- `len(scores)` and `len(scores[0])` give the same answer here, for two
  completely different reasons. Say what each one is counting. What would happen
  if one row had four marks in it?
- Read `scores[1][2]` out loud, left to right, in words. Then do the same for
  `scores[2][1]`. They are different values.
- The first loop prints three things. The second prints nine. Describe the
  difference in one sentence without using the word "nested".
- Add a fourth row with only two marks in it. Does anything break? Should it?

## Modify

- Print only the middle row.
- Print the first mark of every row.
- Print the total of the second row.

> `scores[1][2]` is the same idea as `exam_results["steve"][0]` from Day 6. You
> ask the outer thing for one of its items, then ask that item for one of its
> items. Nothing new is happening.
