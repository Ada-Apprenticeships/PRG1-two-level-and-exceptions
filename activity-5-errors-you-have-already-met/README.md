# Activity 5: Errors you have already met

File: `errors_you_have_met.py`

Ten minutes. Five errors, all of which you have hit at some point in the last
fortnight, gathered in one place so you can look at them deliberately rather
than in a panic.

## Predict

Before running anything, name the error each function will raise, and say in one
sentence what causes it.

| Function | Error you expect |
|---|---|
| `missing_key` | |
| `past_the_end` | |
| `text_that_is_not_a_number` | |
| `adding_apples_to_oranges` | |
| `file_that_is_not_there` | |

## Run

Run the file as it is. Then comment out `missing_key()` and uncomment the next
one, and so on. One at a time, and read each traceback before moving to the next.

## Investigate

For each traceback, find these four things:

1. The name of the error.
2. The line number it happened on.
3. The line of code itself.
4. The detail after the colon.

Then answer: which of the five could be caused by bad data rather than by a
mistake in the code? Which could only ever be a mistake in the code?

## Modify

- Make `missing_key` report that the student is unknown, without stopping the
  program.
- Make `text_that_is_not_a_number` cope with a word instead of a number.
- Leave `adding_apples_to_oranges` alone, and say why.

> That last one is the point of the whole session. Some errors are the program
> telling you it has bad data. Others are the program telling you that you wrote
> something wrong. They look identical, and they need opposite responses.
