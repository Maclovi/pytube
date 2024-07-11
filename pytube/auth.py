from pathlib import Path


def is_auth() -> bool:
    return Path("pytube/__cache__").exists()
