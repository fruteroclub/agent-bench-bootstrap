#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

REQUIRED_FILES = [
    "SOUL.md",
    "IDENTITY.md",
    "USER.md",
    "AGENTS.md",
    "MEMORY.md",
    "HEARTBEAT.md",
    "TOOLS.md",
]

EM_DASH = "—"


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_agent_bootstrap.py <target-dir>")
        return 2

    target = Path(sys.argv[1]).expanduser().resolve()
    errors: list[str] = []
    warnings: list[str] = []

    if not target.exists() or not target.is_dir():
        print(f"ERROR: target directory not found: {target}")
        return 1

    print(f"Validating {target}")

    for name in REQUIRED_FILES:
        path = target / name
        if not path.exists():
            errors.append(f"missing required file: {name}")
            continue
        if path.stat().st_size == 0:
            errors.append(f"empty required file: {name}")
            continue

        text = path.read_text(encoding="utf-8", errors="replace")
        if EM_DASH in text:
            warnings.append(f"contains em dash: {name}")

    identity_path = target / "IDENTITY.md"
    if identity_path.exists() and identity_path.stat().st_size > 0:
        identity_text = identity_path.read_text(encoding="utf-8", errors="replace")
        if "## Current operating role" not in identity_text:
            warnings.append("IDENTITY.md missing '## Current operating role' heading")
        if "## Mandate" not in identity_text:
            warnings.append("IDENTITY.md missing '## Mandate' heading")

    user_path = target / "USER.md"
    if user_path.exists() and user_path.stat().st_size > 0:
        user_text = user_path.read_text(encoding="utf-8", errors="replace")
        if "## Primary counterpart" not in user_text:
            warnings.append("USER.md missing '## Primary counterpart' heading")

    if errors:
        print("\nErrors:")
        for error in errors:
            print(f"- {error}")

    if warnings:
        print("\nWarnings:")
        for warning in warnings:
            print(f"- {warning}")

    if errors:
        print("\nResult: FAIL")
        return 1

    print("\nResult: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
