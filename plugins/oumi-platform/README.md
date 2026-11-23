# Oumi Platform

Connects your agent to the Oumi MCP server at `https://api.oumi.ai/mcp`, so it can work in your Oumi projects as you.

## What it can do

- Inspect projects, datasets, models, evaluations, evaluators, recipes, deployments, monitors, and operations
- Upload, sample, merge, and version datasets
- Set up evaluators and training recipes
- Run training, evaluation, deployment, and synthesis jobs you approve, and stop them

## Sign-in and permissions

You sign in to Oumi in your browser once per agent. In Claude Code, run `/mcp`, select **oumi-platform**, and choose **Authenticate**; the Oumi tools load after you sign in. Other agents ask you to sign in the first time they use a tool. Every call runs with your Oumi account's permissions, so the agent sees only what you can see. Jobs that cost money use your organization's Oumi billing.

## Install

In Claude Code:

```bash
claude plugin marketplace add oumi-ai/oumi-plugins
claude plugin install oumi-platform@oumi
```

For Codex and other agents, see the [repository README](../../README.md#install).

## Privacy

See Oumi's [privacy policy](https://oumi.ai/privacy-policy) and [terms of service](https://oumi.ai/terms-of-service).
