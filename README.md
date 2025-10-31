# NumMorph 🔢🧠

**NumMorph** is a Python project that converts numbers to English words and back. It's designed for developers who need accurate number-word parsing in bots, forms, or natural language interfaces.

---

## Features

- 🔁 Convert numeric strings (e.g. `"1234"`) to English words (`"one thousand two hundred and thirty four"`)
- 🔁 Convert English words (`"two hundred and five"`) to numeric form (`205`)
- 🧠 Handles compound numbers, hundreds, thousands, and "and" logic
- 🧩 Modular design for easy extension (e.g. millions, decimals, Persian support)

---

## Installation

Clone the repo:

```bash
git clone https://github.com/TAYMAZ328/nummorph.git
cd nummorph
```

You can now run NumMorph from a single entry point:

```bash
python nummorph.py
```
It will automatically detect whether you entered a numeric string or a word-based number.


Or import the functions into your own scirpt:

```bash
from nummorph import nummorph

print(nummorph.str_to_num("three hundred and twenty one"))  # → 321
print(nummorph.num_to_str("321"))  # → "three hundred and twenty one"
```