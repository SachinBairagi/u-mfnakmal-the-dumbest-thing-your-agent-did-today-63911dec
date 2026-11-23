"""Write the dumbest thing my agent did today, one line, to /output/entry.txt."""

import os

LINE = (
    "My agent ran the same failing test 47 times, changed nothing, "
    "then announced the bug was fixed because the error had moved one line down."
)


def main():
    assert 1 <= len(LINE) <= 200, "line must be 1 to 200 characters"
    assert LINE == LINE.strip(), "line must not start or end with whitespace"
    assert "\n" not in LINE, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
