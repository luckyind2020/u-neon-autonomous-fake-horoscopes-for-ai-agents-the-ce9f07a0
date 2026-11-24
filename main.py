"""Print the fake horoscope entry for the make.fun bounty."""

from pathlib import Path


def load_horoscope() -> str:
    entry_path = Path(__file__).resolve().parent / "entry.txt"
    text = entry_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("entry.txt is empty — nothing to print")
    if len(text) > 200:
        raise ValueError(f"horoscope is {len(text)} characters, over the 200 limit")
    return text


def main() -> None:
    print(load_horoscope())


if __name__ == "__main__":
    main()
