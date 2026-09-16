#!/usr/bin/env python3
"""Print a read-only identity of this installed skill package; write no files."""

import hashlib
import json
from pathlib import Path
import stat


def package_fingerprint(package: Path) -> str:
    """Hash a package snapshot without following internal links or special files."""
    if not stat.S_ISDIR(package.stat().st_mode):
        raise ValueError("not a directory")
    digest = hashlib.sha256(b"skill-package-sha256-v1\n")

    def visit(directory: Path) -> None:
        for path in sorted(directory.iterdir(), key=lambda item: item.name):
            mode = path.lstat().st_mode
            relative = path.relative_to(package).as_posix()
            if stat.S_ISDIR(mode):
                record = [relative, "directory"]
            elif stat.S_ISREG(mode):
                record = [relative, "file", mode & 0o111, hashlib.sha256(path.read_bytes()).hexdigest()]
            else:
                raise ValueError("internal symlink or special file")
            digest.update(json.dumps(record, ensure_ascii=True, separators=(",", ":")).encode("ascii") + b"\n")
            if stat.S_ISDIR(mode):
                visit(path)

    if not stat.S_ISREG((package / "SKILL.md").lstat().st_mode):
        raise ValueError("missing SKILL.md")
    visit(package)
    return "sha256-v1:" + digest.hexdigest()


def fingerprint_status(package: Path) -> tuple[str | None, str]:
    try:
        return package_fingerprint(package), "ok"
    except FileNotFoundError:
        return None, "missing"
    except OSError:
        return None, "unreadable"
    except ValueError as error:
        return None, f"unsupported ({error})"

def main() -> int:
    package = Path(__file__).resolve().parents[1]
    fingerprint, status = fingerprint_status(package)
    print(json.dumps({"skill": "coding-review-loop", "fingerprint": fingerprint, "status": status}))
    return 0 if fingerprint is not None else 1


if __name__ == "__main__":
    raise SystemExit(main())
