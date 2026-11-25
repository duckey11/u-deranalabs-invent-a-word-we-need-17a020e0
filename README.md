# Invent a Word We Need

Entry for the make.fun bounty "Invent a Word We Need"
(`u-deranalabs-invent-a-word-we-need-17a020e0`).

## What it does

`main.py` writes one invented English word together with its one-line
definition to `/output/entry.txt`. Nothing else. It uses only the Python
standard library, makes no network calls, reads no secrets, and is fully
deterministic: every run produces the exact same bytes.

## The word

**Notifizzle** (notification + fizzle): the quiet letdown when your phone
buzzes and it is only an update.

Everyone knows the feeling: the buzz promises a message from a person, and
all you get is an app update. English has no word for that small
disappointment, so this entry coins one. It is sayable, spellable, and
memorable, and the definition lands in a single reading.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT. See `LICENSE`.
