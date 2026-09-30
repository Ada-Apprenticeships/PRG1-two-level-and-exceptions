# Stretch 1: Following the chain

File: `following_the_chain.py`

Optional. A two-level structure where the second row is not data about the first
one, but directions.

Row 0 holds plant names in planting order. Row 1 holds, for each plant, the
position of the next plant alphabetically.

## Predict

Work out the printed order by hand before running anything. Start at position 0
and follow the numbers.

## Run

Execute and compare.

## Investigate

- The loop stops when `current` becomes `None`. Which plant is that, and why is
  it that one?
- What would happen if one of the numbers in row 1 pointed backwards to a
  position already visited?
- The plants are stored in planting order and printed in alphabetical order, and
  nothing is sorted anywhere. Where does the alphabetical order actually live?

## Modify

- Print each plant's position as well as its name.
- Add "Iris" to the data in the right place, which means changing more than one
  number.
- Report how many steps the chain takes, without counting the names.
