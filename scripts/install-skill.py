#!/usr/bin/env python3
"""List and install repo-tracked Codex skills."""

from __future__ import annotations

import argparse
import os
import re
import runpy
import shutil
import sys
from pathlib import Path

SKILL_NAME_RE = re.compile(r"^[a-z0-9-]+$")


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def runtime_root(override: str | None) -> Path:
    if override:
        return Path(override).expanduser()
    codex_home = os.environ.get("CODEX_HOME")
    base = Path(codex_home).expanduser() if codex_home else Path.home() / ".codex"
    return base / "skills"


def inspection_roots(override: str | None, name: str | None) -> list[Path]:
    if override:
        return [runtime_root(override)]
    candidates = [runtime_root(None), Path.home() / ".agents" / "skills", Path.home() / ".codex" / "skills"]
    roots = []
    for root in candidates:
        target = root / name if name else root
        if root not in roots and (target.exists() or target.is_symlink()):
            roots.append(root)
    return roots or [runtime_root(None)]


def tracked_skills(root: Path) -> list[str]:
    skills_dir = root / "skills"
    if not skills_dir.exists():
        return []
    return sorted(
        path.name
        for path in skills_dir.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def check_skill_name(name: str) -> None:
    if not SKILL_NAME_RE.fullmatch(name):
        raise SystemExit(f"Invalid skill name: {name!r}")


def install_status(name: str, source: Path, dest_root: Path) -> str:
    dest = dest_root / name
    if not dest.exists() and not dest.is_symlink():
        return "missing"
    if dest.is_symlink():
        target = dest.resolve(strict=False)
        if target == source.resolve(strict=False):
            return "installed: symlink to repo"
        return f"installed: symlink to {target}"
    if dest.is_dir() and (dest / "SKILL.md").is_file():
        return "installed: directory/copy"
    return "exists: not a skill directory"


# Reuse the standalone helper shipped with copied as well as linked skills.
_identity = runpy.run_path(str(repo_root() / "skills/coding-review-loop/scripts/skill_identity.py"))
fingerprint_status = _identity["fingerprint_status"]


def package_comparison(source: Path, dest: Path) -> tuple[str, str | None, str | None]:
    source_hash, source_state = fingerprint_status(source)
    runtime_hash, runtime_state = fingerprint_status(dest)
    if source_hash is None:
        state = f"repository {source_state}; runtime {runtime_state}"
    elif runtime_hash is None:
        state = f"runtime {runtime_state}"
    else:
        state = "matches repository" if source_hash == runtime_hash else "differs from repository"
    return state, source_hash, runtime_hash


def inspect_skill(root: Path, dest_root: Path, name: str) -> int:
    check_skill_name(name)
    source = root / "skills" / name
    state, source_hash, runtime_hash = package_comparison(source, dest_root / name)
    print(f"Skill: {name}")
    print(f"Runtime skills dir: {dest_root}")
    print(f"Status: {state}")
    print(f"Repository fingerprint: {source_hash or 'unavailable'}")
    print(f"Runtime fingerprint: {runtime_hash or 'unavailable'}")
    print("On-disk snapshot only; does not establish what a session loaded.")
    return 0 if source_hash is not None and runtime_hash is not None else 1


def list_skills(root: Path, dest_root: Path) -> int:
    names = tracked_skills(root)
    if not names:
        print("No tracked skills found.")
        return 1

    print(f"Runtime skills dir: {dest_root}")
    print()
    width = max(len("skill"), *(len(name) for name in names))
    print(f"{'skill'.ljust(width)}  status")
    print(f"{'-' * width}  ------")
    for name in names:
        source = root / "skills" / name
        state, _, _ = package_comparison(source, dest_root / name)
        try:
            location = install_status(name, source, dest_root)
        except OSError:
            location = "installation location unreadable"
        print(f"{name.ljust(width)}  {location}; {state}")

    if dest_root.exists():
        extras = sorted(
            path.name
            for path in dest_root.iterdir()
            if path.name not in names and (path.is_dir() or path.is_symlink())
        )
        if extras:
            print()
            print("Other runtime skills not tracked in this repo:")
            for name in extras:
                print(f"- {name}")
    return 0


def install_skill(root: Path, dest_root: Path, name: str, copy: bool, dry_run: bool) -> int:
    check_skill_name(name)
    source = root / "skills" / name
    dest = dest_root / name

    if not (source / "SKILL.md").is_file():
        print(f"Skill not found in repo: {name}", file=sys.stderr)
        return 1
    if dest.exists() or dest.is_symlink():
        print(f"Refusing to overwrite existing destination: {dest}", file=sys.stderr)
        print(f"Current status: {install_status(name, source, dest_root)}", file=sys.stderr)
        return 1

    mode = "copy" if copy else "symlink"
    print(f"Install {name}: {source} -> {dest} ({mode})")
    if dry_run:
        print("Dry run only; no files changed.")
        return 0

    dest_root.mkdir(parents=True, exist_ok=True)
    if copy:
        shutil.copytree(source, dest, symlinks=True)
    else:
        dest.symlink_to(source, target_is_directory=True)

    if not (dest / "SKILL.md").is_file():
        print(f"Install verification failed: {dest / 'SKILL.md'} missing", file=sys.stderr)
        return 1
    print("Installed and verified SKILL.md exists.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="List and install repo-tracked Codex skills.")
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument("--list", action="store_true", help="List tracked skills and local install status.")
    action.add_argument("--inspect", metavar="SKILL", help="Compare package fingerprints on disk (not session loading).")
    action.add_argument("--install", metavar="SKILL", help="Install one tracked skill by name.")
    parser.add_argument("--copy", action="store_true", help="Copy instead of symlinking when installing.")
    parser.add_argument("--dry-run", action="store_true", help="Show what would happen without changing files.")
    parser.add_argument("--runtime-root", help="Override runtime skills directory for testing or custom installs.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    dest_root = runtime_root(args.runtime_root)

    if args.list or args.inspect:
        if args.copy or args.dry_run:
            print("--copy and --dry-run are only meaningful with --install", file=sys.stderr)
            return 1
        if args.inspect:
            check_skill_name(args.inspect)
        results = []
        for location in inspection_roots(args.runtime_root, args.inspect):
            results.append(list_skills(root, location) if args.list else inspect_skill(root, location, args.inspect))
        return max(results)

    return install_skill(root, dest_root, args.install, args.copy, args.dry_run)


if __name__ == "__main__":
    raise SystemExit(main())
