import os

LINE = "1%. Tell the group chat I died doing what I loved: ignoring the low battery warning."


def write_entry(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
