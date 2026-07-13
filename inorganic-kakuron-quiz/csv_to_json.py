import csv
import json
from pathlib import Path

INPUT = Path("reactions.csv")
OUTPUT = Path("reactions.json")

AFFILIATION_LABELS = {
    "ア": "アルカリ金属元素",
    "イ": "2族元素",
    "ウ": "両性元素",
    "エ": "遷移元素",
    "オ": "14族元素",
    "カ": "15族元素",
    "キ": "16族元素",
    "ク": "17族元素",
}


def split_affiliations(raw: str) -> list[str]:
    if raw is None:
        return []
    text = str(raw).strip()
    for old, new in [
        ("（", "("),
        ("）", ")"),
        ("、", ";"),
        ("，", ";"),
        ("|", ";"),
        (" ", ";"),
    ]:
        text = text.replace(old, new)
    parts = []
    for token in text.split(";"):
        token = token.strip().replace("(", "").replace(")", "")
        if token:
            parts.append(token)
    return parts


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"{INPUT} が見つかりません。")

    reactions = []
    with INPUT.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader, start=1):
            affiliations = split_affiliations(row.get("affiliations") or row.get("affiliation") or row.get("categories") or "")
            item = {
                "id": row.get("id") or f"row-{i}",
                "unit": row.get("unit", ""),
                "chapter": row.get("chapter", ""),
                "statement": row.get("statement", ""),
                "equation": row.get("equation", ""),
                "affiliations": affiliations,
                "note": row.get("note", ""),
                "level": int(row["level"]) if row.get("level") else None,
            }
            reactions.append(item)

    data = {
        "meta": {
            "title": "無機化学小テスト：各論編",
            "source": str(INPUT),
        },
        "affiliationLabels": AFFILIATION_LABELS,
        "reactions": reactions,
    }

    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"{OUTPUT} を作成しました。登録問題数: {len(reactions)}問")


if __name__ == "__main__":
    main()
