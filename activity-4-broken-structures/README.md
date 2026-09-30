# Activity 4: Broken structures

File: `broken_structures.py`

Three faults across three small programs. Nothing crashes, and every answer looks
like an answer.

## Predict

Work out what each part **should** produce:

1. A three by three grid of zeros with `9` in the top-left corner only.
2. The totals of column 0 and column 1 of the sales table.
3. Whether B-104 and B-111 are at Kings Cross. Check the data yourself.

## Run

Execute it. All three are wrong.

## Investigate

- Setting one corner to `9` changed three rows. Nothing in the code touches the
  other two rows. So what is `[[0] * 3] * 3` actually building? You met exactly
  this on Day 5, with playlists.
- The two column totals are the same number. Change the column argument to `2`
  and look at what happens. Which numbers is `column_total` actually adding up?
  Write them down and see where they sit in the table.
- B-111 is plainly at Kings Cross in the data and the program says it is not.
  How many bikes does `is_at_station` ever look at? Read the `else` carefully.

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three. You should get one `9` in the whole grid, column totals of 39 and
47, and `True` for both bikes.

> Fault 2 produced a perfectly plausible number that did not change when you
> asked for a different column. A figure that ignores its own arguments is worth
> being suspicious of, and it is the kind of thing a test suite catches and
> reading does not.
