
![CALCULATOR](calgif.gif)

# Clipboard Calculator

Instantly evaluate mathematical expressions anywhere using a global hotkey.

Clipboard Calculator is a lightweight Python tool that removes the need to open a separate calculator. Copy an expression, press a shortcut, and paste the result directly into your workflow.

---

## Features

* Works system-wide with a global hotkey
* Uses clipboard for seamless input and output
* Fast, minimal, and efficient
* No graphical interface required
* Basic safety filtering for expressions

---

## How It Works

1. Select any mathematical expression (for example, `12 + 5 * 3`)
2. Press **Ctrl + Shift + C**
3. The script will:

   * Copy the selected text
   * Evaluate the expression
   * Replace it with the result

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/clipboard-calculator.git
cd clipboard-calculator
```

### 2. Install dependencies

```bash
pip install keyboard pyperclip
```

---

## Usage

Run the script:

```bash
python calculator_shortcut.py
```

Run in the background (Windows):

```bash
pythonw calculator_shortcut.py
```

---

## Hotkeys

| Action               | Shortcut         |
| -------------------- | ---------------- |
| Calculate expression | Ctrl + = |
| Stop script          | ESC              |

---

## Example

Input:

```
45 * (2 + 3)
```

Output:

```
225
```

---

## Safety Note

Only basic mathematical characters are allowed:

```
0123456789+-*/().
```

This reduces the risk of executing unsafe code. Still, use the tool responsibly.

---

## Limitations

* Does not support advanced functions like `sin`, `log`, etc.
* Requires text selection to work
* Depends on clipboard behavior, which may vary across systems

---

## Future Improvements

* Add support for advanced math functions
* Allow customizable hotkeys
* Add system tray support
* Improve expression evaluation using AST parsing

---

## Contributing

Contributions are welcome. Fork the repository and submit a pull request with your improvements.

---

## Author

Developed by Rutik Ingle
