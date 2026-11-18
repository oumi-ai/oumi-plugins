# Oumi plugins

Official plugins that connect AI agents to the [Oumi platform](https://platform.oumi.ai).

| Plugin | What it does |
| --- | --- |
| [`oumi-platform`](plugins/oumi-platform) | Connects your agent to the Oumi MCP server at `https://api.oumi.ai/mcp`. Work in your Oumi projects as yourself: inspect datasets, models, evaluations, and deployments; prepare datasets; and run training, evaluation, and deployment jobs you approve. |

You sign in with your own Oumi account, and every action uses your existing Oumi permissions. The plugin holds no credentials.

## Install

### Claude Code

```bash
claude plugin marketplace add oumi-ai/oumi-plugins
claude plugin install oumi-platform@oumi
```

Start a session and ask Claude to list your Oumi organizations. Claude Code opens a browser window for you to sign in to Oumi the first time.

### Codex

```bash
codex plugin marketplace add oumi-ai/oumi-plugins
codex plugin add oumi-platform@oumi
```

### Claude and ChatGPT apps

Add a custom connector with the server URL `https://api.oumi.ai/mcp`, then sign in to Oumi:

- **Claude:** Settings → Connectors → Add custom connector.
- **ChatGPT:** Plugins → **+** → Add custom MCP server, with OAuth authentication.

### Any other MCP client

Use these settings in any client that supports remote MCP servers with OAuth:

| Setting | Value |
| --- | --- |
| Transport | Streamable HTTP |
| URL | `https://api.oumi.ai/mcp` |
| Authentication | OAuth 2.1 with dynamic client registration. Leave the client ID and secret empty. |

For a client that reads a JSON config, the entry looks like this:

```json
{
  "mcpServers": {
    "oumi-platform": {
      "type": "http",
      "url": "https://api.oumi.ai/mcp"
    }
  }
}
```

## Try it

- "List my Oumi organizations and projects."
- "Summarize the datasets in my Oumi project."
- "Show the recent evaluations in my project and compare their scores."

Jobs that cost money, such as training, evaluation, and deployments, run only when you ask for them, and they use your organization's Oumi billing.

## Repository layout

| Path | Purpose |
| --- | --- |
| `.claude-plugin/marketplace.json` | Claude Code marketplace |
| `.agents/plugins/marketplace.json` | Codex marketplace |
| `plugins/oumi-platform/` | The plugin: `plugin.json` and `mcp.json` (portable format), `.claude-plugin/` and `.mcp.json` (Claude Code), `.codex-plugin/` (older Codex versions) |

## Support

- Documentation: [docs.oumi.ai](https://docs.oumi.ai)
- Bugs and feature requests: [open an issue](https://github.com/oumi-ai/oumi-plugins/issues)
- Security issues: see [SECURITY.md](SECURITY.md)
- [Privacy policy](https://oumi.ai/privacy-policy) · [Terms of service](https://oumi.ai/terms-of-service)

## License

[Apache 2.0](LICENSE)
