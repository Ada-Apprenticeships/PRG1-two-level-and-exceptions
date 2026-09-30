# Stretch 2: Raising your own

File: `raising_your_own.py`

Optional. Sometimes catching an error is the wrong thing to do, and the right
thing is to raise one yourself.

## Predict

Three lines are printed. Work out all three.

## Run

Execute and compare.

## Investigate

- `average_or_zero([])` returns `0`. Is that an average? What would a reader of
  a report containing that zero believe?
- `average([])` raises instead. Who now has to decide what to do, and is that
  better?
- The `try` at the bottom catches the error and prints the message. Where would
  you put that `try` in a real program: around this one call, or somewhere else?

## Modify

- Make `average` refuse a list containing anything that is not a number.
- Write a version that returns both the average and how many readings it used,
  so the caller can judge for themselves.
