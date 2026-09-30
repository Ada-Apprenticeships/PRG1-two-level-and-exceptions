# Activity 7: The error that was hidden

File: `hidden_errors.py`

Three faults. Nothing crashes. Nothing prints an error message. Every fault in
this file is a `try` or an `except` doing something it should not.

The depot uses this report to decide which bikes to collect overnight, so being
quietly wrong here means a bike is left out all night on 8% charge.

## Predict

Read the fleet data at the top carefully, one record at a time, before reading
any of the functions.

- Which bikes should be collected?
- Which stations have bikes?

## Run

Execute it. Neither answer is right.

## Investigate

- B-111 is on 8% and is not on the collection list. Look at that record and
  compare its fields against the others. Then look at the `except: pass` and say
  exactly what it swallowed.
- B-118 **is** on the collection list. Look at its battery value. Does anybody
  actually know whether that bike needs collecting? What did `battery_percent`
  decide on your behalf?
- The stations list is empty, which is plainly untrue. `stations_covered` wraps
  its whole body in a `try` and returns an empty list on any problem. Work out
  which record triggers it, and what the caller now cannot tell.

## Fault log

| # | What you saw | What was wrong | How you fixed it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |

## Modify

Fix all three so that the report names B-111 as needing collection, is honest
about B-118, and lists all three stations.

There is more than one defensible fix for the second one. Whichever you pick,
write down in your fault log what the program now does when a battery reading
cannot be read, and why that is better than reporting zero.

> `except: pass` is the most dangerous two words in this module. It turns a
> program that would have told you something was wrong into one that carries on
> and reports a number. Everything else this fortnight has been about spotting
> code that runs and lies. This is how you write it on purpose.
