"""Check that the plugin manifests and marketplaces agree.

Run from the repository root: python3 scripts/check_plugins.py
Exits non-zero and lists every problem it finds.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SERVER_URL = "https://api.oumi.ai/mcp"


def load(path: Path) -> dict:
    with path.open() as f:
        return json.load(f)


def main() -> int:
    problems: list[str] = []
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts:
            continue
        try:
            load(path)
        except json.JSONDecodeError as error:
            problems.append(f"{path.relative_to(ROOT)}: invalid JSON ({error})")
    if problems:
        print("\n".join(problems))
        return 1

    claude_market = load(ROOT / ".claude-plugin/marketplace.json")
    codex_market = load(ROOT / ".agents/plugins/marketplace.json")
    claude_entries = {p["name"]: p for p in claude_market["plugins"]}
    codex_entries = {p["name"]: p for p in codex_market["plugins"]}
    if claude_entries.keys() != codex_entries.keys():
        problems.append("The Claude Code and Codex marketplaces list different plugins")

    for name, entry in claude_entries.items():
        plugin_dir = ROOT / entry["source"]
        codex_source = codex_entries.get(name, {}).get("source", {})
        if (ROOT / codex_source.get("path", "")).resolve() != plugin_dir.resolve():
            problems.append(f"{name}: marketplaces point at different folders")

        manifests = {
            "plugin.json": load(plugin_dir / "plugin.json"),
            ".claude-plugin/plugin.json": load(plugin_dir / ".claude-plugin/plugin.json"),
            ".codex-plugin/plugin.json": load(plugin_dir / ".codex-plugin/plugin.json"),
        }
        for field in ("name", "version", "description"):
            values = {path: manifest.get(field) for path, manifest in manifests.items()}
            if len(set(values.values())) != 1:
                problems.append(f"{name}: '{field}' differs between manifests: {values}")
        if manifests["plugin.json"]["name"] != name:
            problems.append(f"{name}: manifest name doesn't match the marketplace entry")
        if entry.get("version") != manifests["plugin.json"]["version"]:
            problems.append(f"{name}: marketplace version doesn't match the manifests")

        for config in ("mcp.json", ".mcp.json"):
            servers = load(plugin_dir / config)["mcpServers"]
            urls = {server.get("url") for server in servers.values()}
            if urls != {SERVER_URL}:
                problems.append(f"{name}/{config}: server URL must be {SERVER_URL}, found {sorted(map(str, urls))}")

    if problems:
        print("\n".join(problems))
        return 1
    print(f"OK: {len(claude_entries)} plugin(s) checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
