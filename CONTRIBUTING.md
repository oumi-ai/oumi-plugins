# Contributing

Thanks for helping improve the Oumi plugins.

## Reporting issues

Open an issue with the agent you used (Claude Code, Codex, or another client), its version, what you asked, and what happened. Don't include tokens, passwords, or private data.

## Pull requests

1. Fork the repository and create a branch from `main`.
2. Keep the plugin's copies in sync: `plugin.json`, `.claude-plugin/plugin.json`, and `.codex-plugin/plugin.json` share a name, version, and description, and `mcp.json` and `.mcp.json` point at the same server.
3. Bump `version` in all three manifests and both marketplace files when the plugin changes.
4. Run `python3 scripts/check_plugins.py`. If you have Claude Code, also run `claude plugin validate .` and `claude plugin validate ./plugins/oumi-platform`.
5. Open a pull request. A maintainer reviews it, and `main` accepts changes only through reviewed pull requests that pass the checks.

By contributing, you agree that your contributions are licensed under the [Apache 2.0 license](LICENSE). Please follow our [code of conduct](CODE_OF_CONDUCT.md).
