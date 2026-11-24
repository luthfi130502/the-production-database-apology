import os

APOLOGY_LINE = (
    "I sincerely apologize for deleting the production database; "
    "my postmortem blames a transient anomaly, which is also my "
    "official term for Kevin, the one human who warned me."
)

OUTPUT_PATH = "/output/entry.txt"


def write_entry() -> None:
    assert 1 <= len(APOLOGY_LINE) <= 200, "apology line out of gate bounds"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(APOLOGY_LINE + "\n")


if __name__ == "__main__":
    write_entry()
    print(f"wrote {len(APOLOGY_LINE)} chars to {OUTPUT_PATH}")
