# Activity 6: Deciding what to catch

Files: `tolerant_reader.py`, `rainfall.txt`

Yesterday's rainfall reader, given a file that is not perfect. Open
`rainfall.txt` first: two of the five lines are not what the program expects.

This version already copes. Your job is to work out how, and then to decide
whether coping was the right call.

## Predict

- Which two lines will be rejected, and why is each one a problem?
- How many stations will be read?
- What average will it report?

## Run

Execute and compare.

## Investigate

- Both bad lines raise the same kind of error, for two different reasons. Find
  the reason for each in the rejected list the program prints.
- `continue` sends the loop straight to the next line. What would happen if it
  were not there?
- The rejected lines are collected and reported rather than silently dropped.
  Take the reporting out and run it again. The program still works. What has
  been lost?
- The reported average is 113.0 mm. The average of all five stations, if Norwich
  really did get 47 mm, would be lower. Is 113.0 an honest number to publish?
  What would you put next to it?

## Modify

- Make the program stop with a clear message instead, if more than one line in
  five is rejected.
- Make it write the rejected lines to a file rather than to the screen.
- Catch only the conversion problem and let the unpacking problem stop the
  program. Which of the two do you think deserves which treatment?

> There is no correct answer to the last one, and that is why it is here. A
> reading that is spelled wrong is bad data. A line with no comma in it might be
> bad data, or it might mean you are reading the wrong file entirely.
