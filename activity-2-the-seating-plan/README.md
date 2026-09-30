# Activity 2: The seating plan

File: `seating_plan.py`

A working program. Five rows of eight cinema seats, `X` for booked and `.` for
free. It draws the auditorium and reports how full it is.

## Predict

Look at `seats` in the code, not at the program's output.

- How many seats are free in row 1?
- Which row is completely full?
- How many seats are sold in total?

Write all three down before running anything.

## Run

Execute and compare.

## Investigate

- `ROWS` and `COLUMNS` are worked out from the data rather than typed in. Why is
  that better than writing `5` and `8`?
- `COLUMNS` uses `len(seats[0])`. What does that assume about the other rows?
  What would happen if row 3 had nine seats in it?
- `free_in_row` takes one row, not the whole grid. What does that let you do
  that a function taking the whole grid would not?
- `show_plan` loops over `range(ROWS)` and uses `seats[row_number]`, while
  `free_in_row` loops over the row directly. Both are correct. Why did each one
  need what it has?

## Modify

- Report which row has the most free seats.
- Book seat 4 in row 2, then run the report again.
- Report the number of free seats in the front two rows only.

## Stretch

Optional. Report how many seats are free in each *column*, which is harder than
it sounds, because the data is stored by row.
