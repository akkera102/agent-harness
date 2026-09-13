from pathlib import Path

OLD = b"abcdefg"
NEW = b"akkera102"


def main() -> None:
    html_files = sorted(Path.cwd().glob("*.html"))
    total = 0

    for path in html_files:
        data = path.read_bytes()
        count = data.count(OLD)

        if count:
            path.write_bytes(data.replace(OLD, NEW))

        print(f"{path.name}: {count}")
        total += count

    print(f"TOTAL: {total}")


if __name__ == "__main__":
    main()
