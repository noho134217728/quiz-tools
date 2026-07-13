#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reactions.csv を reactions.json に変換するスクリプト。

使い方:
    python csv_to_json.py
    python csv_to_json.py reactions.csv reactions.json
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

CATEGORY_LABELS = {
    "ア": "酸塩基反応：酸化物と水の反応",
    "イ": "酸塩基反応：中和反応",
    "ウ": "酸塩基反応：遊離反応",
    "エ": "酸化還元反応",
    "オ": "熱分解反応",
    "カ": "沈殿生成反応",
    "キ": "錯体生成反応",
}

REQUIRED_COLUMNS = ["id", "statement", "equation", "categories"]
OPTIONAL_COLUMNS = ["unit", "chapter", "note", "level"]


def normalize_category_token(token: str) -> str:
    """'(ア)' や 'ア ' のような入力を 'ア' に正規化する。"""
    token = token.strip()
    token = token.replace("（", "(").replace("）", ")")
    token = token.strip("() ")
    return token


def split_categories(raw: str) -> list[str]:
    """'イ;カ'、'イ,カ'、'イ カ' などを ['イ', 'カ'] にする。"""
    parts = re.split(r"[;,|、，\s]+", raw.strip())
    categories = [normalize_category_token(part) for part in parts if part.strip()]
    return categories


def convert(csv_path: Path, json_path: Path) -> None:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSVが見つかりません: {csv_path}")

    reactions: list[dict[str, object]] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSVのヘッダー行が見つかりません。")

        missing = [col for col in REQUIRED_COLUMNS if col not in reader.fieldnames]
        if missing:
            raise ValueError(f"必須列が足りません: {', '.join(missing)}")

        for row_number, row in enumerate(reader, start=2):
            item = {key: (row.get(key, "") or "").strip() for key in REQUIRED_COLUMNS + OPTIONAL_COLUMNS}

            if not item["id"]:
                item["id"] = f"auto-{row_number - 1:04d}"

            categories = split_categories(item["categories"])
            invalid = [cat for cat in categories if cat not in CATEGORY_LABELS]
            if invalid:
                raise ValueError(
                    f"{row_number}行目: 未定義の分類記号があります: {invalid}。"
                    f"使用可能: {list(CATEGORY_LABELS)}"
                )

            try:
                level = int(item["level"]) if item["level"] else None
            except ValueError as exc:
                raise ValueError(f"{row_number}行目: level は整数にしてください。") from exc

            reactions.append(
                {
                    "id": item["id"],
                    "unit": item["unit"],
                    "chapter": item["chapter"],
                    "statement": item["statement"],
                    "equation": item["equation"],
                    "categories": categories,
                    "note": item["note"],
                    "level": level,
                }
            )

    payload = {
        "meta": {
            "title": "無機化学 化学反応式小テスト",
            "version": "1.0.0",
            "source": csv_path.name,
        },
        "categoryLabels": CATEGORY_LABELS,
        "reactions": reactions,
    }

    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {csv_path} -> {json_path} ({len(reactions)} reactions)")


def main() -> None:
    csv_path = Path(sys.argv[1]) if len(sys.argv) >= 2 else Path("reactions.csv")
    json_path = Path(sys.argv[2]) if len(sys.argv) >= 3 else Path("reactions.json")
    convert(csv_path, json_path)


if __name__ == "__main__":
    main()
