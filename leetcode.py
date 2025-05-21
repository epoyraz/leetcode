#!/usr/bin/env python3
import json
import os
import sys


def save_ls_files(json_path, out_dir="."):
    """
    Reads a localStorage JSON export and writes files for each key
    that does NOT include 'updated-time':
      - filename = first part before the first underscore
      - extension = last part after the last underscore:
          python → .py, python3 → .py, pythondata → .py,
          javascript → .js, mysql → .sql, postgresql → .sql, otherwise raw suffix
      - file contents decoded from JSON escape sequences
    """
    # Load JSON
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        print(f"Error loading JSON file: {e}", file=sys.stderr)
        sys.exit(1)

    # Prepare output directory
    os.makedirs(out_dir, exist_ok=True)

    # Map language suffixes to file extensions
    ext_map = {
        "python": "py",
        "python3": "py",
        "pythondata": "py",
        "javascript": "js",
        "mysql": "sql",
        "postgresql": "sql",
    }

    # Iterate entries
    for key, raw in data.items():
        # Skip timestamp entries
        if "updated-time" in key:
            continue

        parts = key.split("_")
        if len(parts) < 2:
            continue

        name = parts[0]
        lang = parts[-1].lower()
        ext = ext_map.get(lang, lang)
        filename = os.path.join(out_dir, f"{name}.{ext}")

        # Strip surrounding quotes
        content = raw
        if content.startswith('"') and content.endswith('"'):
            content = content[1:-1]

        # Decode escape sequences into real characters
        try:
            content = bytes(content, "utf-8").decode("unicode_escape")
        except Exception as e:
            print(f"Warning: could not decode escapes in {key}: {e}", file=sys.stderr)

        # Write file
        with open(filename, 'w', encoding='utf-8') as out:
            out.write(content)

        print(f"Wrote {filename!r}")


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print(
            "Usage: python save_ls_files.py /path/to/localStorage.json [output_directory]",
            file=sys.stderr
        )
        sys.exit(1)

    json_file = sys.argv[1]
    out_dir = sys.argv[2] if len(sys.argv) == 3 else "."
    save_ls_files(json_file, out_dir)
