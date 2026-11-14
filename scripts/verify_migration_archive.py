"""Verify preserved GitHub source files without running historical coursework."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

def verify(path: Path) -> dict[str, int]:
    archive = json.loads(path.read_text(encoding="utf-8"))
    commits = {item["sha"]: item for item in archive["commits"]}
    trees = archive["trees"]
    blobs = archive["blobs"]
    for sha, blob in blobs.items():
        data = blob["content"].encode("utf-8")
        actual = hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()
        if actual != sha:
            raise ValueError(f"{path.name}: blob mismatch {sha}")
    for sha, commit in commits.items():
        if commit["commit"]["tree"]["sha"] not in trees:
            raise ValueError(f"{path.name}: missing tree for {sha}")
        for parent in commit["parents"]:
            if parent["sha"] not in commits:
                raise ValueError(f"{path.name}: missing parent {parent['sha']}")
    for tree in trees.values():
        if tree.get("truncated"):
            raise ValueError(f"{path.name}: truncated tree")
        for entry in tree["tree"]:
            if entry["type"] == "blob":
                if entry["sha"] not in blobs:
                    raise ValueError(f"{path.name}: missing blob {entry['sha']}")
                size = len(blobs[entry["sha"]]["content"].encode("utf-8"))
                if size != entry["size"]:
                    raise ValueError(f"{path.name}: blob size mismatch {entry['path']}")
    for ref in archive["refs"]:
        if ref["object"]["type"] == "commit" and ref["object"]["sha"] not in commits:
            raise ValueError(f"{path.name}: missing ref {ref['ref']}")
    return {"commits": len(commits), "trees": len(trees), "blobs": len(blobs)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archives", nargs="+", type=Path)
    args = parser.parse_args()
    for archive_path in args.archives:
        print(archive_path.name, json.dumps(verify(archive_path), sort_keys=True))
