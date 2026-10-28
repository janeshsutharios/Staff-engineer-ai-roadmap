# Day 1 — Run Python and calculate expenses

Date: 28 October 2026 · Suggested time: 45–60 minutes
Roadmap alignment: first part of Week 1. Collections, functions, modules and exceptions
will follow; today is a small first step toward the command-line expense calculator.

## Set up VS Code

VS Code and Python 3.13.7 were detected on this Mac when this lesson was prepared.

1. Open VS Code and choose File → Open Folder → select the `ai-learning` folder.
2. Open Extensions (Command + Shift + X), search for **Python**, and install the
   extension published by **Microsoft** if it is not already installed.
3. Press Command + Shift + P, choose **Python: Select Interpreter**, and select
   Python 3.13.7 (`/opt/homebrew/bin/python3`).
4. Open `month-01-python/practice/day_01.py`.
5. Use **Run Python File** at the top right, or open Terminal → New Terminal and run:

```sh
python3 month-01-python/practice/day_01.py
```

No additional Python packages are needed today. Week 2 introduces a virtual environment
before work with external packages.

Official setup reference: https://code.visualstudio.com/docs/python/python-tutorial

## Concept bridge from Swift

| Concept | Swift | Python | What to notice |
|---|---|---|---|
| Variable | `var name = "Janesh"` | `name = "Janesh"` | No `var` keyword |
| Constant | `let days = 7` | `DAYS = 7` | Uppercase is a convention, not enforced immutability |
| Integer | `let count = 3` | `count = 3` | Python values have types; variables can be rebound to another type |
| Decimal | `let price = 19.5` | `price = 19.5` | Python calls this type `float` |
| Boolean | `let ready = true` | `ready = True` | `True` and `False` are capitalized |
| Output | `print(name)` | `print(name)` | Similar call syntax |
| Interpolation | `"Hello \(name)"` | `f"Hello {name}"` | The `f` prefix enables expressions in braces |
| Comment | `// a note` | `# a note` | Comments explain intent |

Python uses indentation to group statements instead of braces. We will practise that
with conditions and loops next. `/` produces a floating-point division result;
`//` performs floor division. This differs from dividing two Swift integers.

## Read, predict, then run

```python
name = "Janesh"
study_minutes = 45
hours = study_minutes / 60
print(f"{name} studied for {hours} hours")
print(type(study_minutes))
```

Predict both output lines before running. Expected output:

```text
Janesh studied for 0.75 hours
<class 'int'>
```

An assignment such as `study_minutes = 45` binds a name to a value. `type(...)`
shows the value's type. Arithmetic is evaluated before the result is assigned.

## Practice — do these yourself

The starter contains a working example and TODO comments, not finished exercise answers.
Use whole rupee amounts today to keep the exercise focused on integers.

1. Run the starter and confirm the total is 200 rupees.
2. Change food from 120 to 150. Predict the new total before running.
3. Add an `internet` expense of 50 and include it in the total.
4. Set a daily budget of 300 and print the remaining amount.
5. Reset the original amounts (120, 50, 30), remove the extra expense from the total,
   and verify the remaining amount is 100.
6. Print the types of your name, total and the result of `total / 3`.
7. Deliberately misspell a variable in a `print` call. Read the error, fix it and
   record what `NameError` means. Then try adding `"120"` to `50`: explain the
   resulting `TypeError` and why a numeric string differs from an integer.

Optional: ask for one expense with `input()`, convert it using `int()`, and add it.
`input()` returns text. Invalid numeric text raises `ValueError`; handling this is a
later Week 1 topic.

## Finish and record

- [ ] I can run the file without help.
- [ ] I can explain `str`, `int`, `float` and `bool`.
- [ ] I can calculate a total and a remaining budget.
- [ ] I can explain one error I caused and fixed.
- [ ] I filled today's note with actual results and unresolved questions.

Next session: lists, dictionaries, conditions and loops using multiple expenses.
