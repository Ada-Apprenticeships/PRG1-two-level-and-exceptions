# Activity 3: Records with fields

File: `bike_fleet.py`

A working program, and the most important activity of the morning.

A grid of numbers is one kind of two-level data. This is the other kind, and the
one you will actually meet: a list where every item is a dictionary with the same
set of fields.

## Predict

From the fleet data alone, work out:

- Which bikes are ready to hire?
- Which bikes need charging?
- What is the average battery level?

Be careful with the first one. It has two conditions.

## Run

Execute and compare.

## Investigate

- `fleet[0]` gives a whole bike. `fleet[0]["battery"]` gives one number. Say the
  second one out loud, left to right.
- Compare `fleet[1][2]` from activity 1 with `fleet[1]["battery"]` here. What has
  changed, and what has not?
- `ready_to_hire` checks `bike["available"] and bike["battery"] > LOW_BATTERY`.
  B-120 has 91% charge and is not in the list. Why not?
- Every one of these four functions has the same shape: start with an empty list,
  loop the fleet, test each record, keep the ones that match. Where have you
  written that shape before?
- `list(fleet[0].keys())` prints the field names. What does it assume about the
  other four bikes?

## Modify

- Report the bikes at Shoreditch.
- Report the average battery of the available bikes only.
- Add a bike with no `station` field and run the program. Which function breaks
  first, and what does the error tell you?

> This shape, a list of records that each have named fields, is how almost all
> real data arrives: a database query, a spreadsheet, a web API. Learn to read it
> and a great deal of professional code stops being mysterious.
