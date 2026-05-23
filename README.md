# agent-bench-bootstrap

Reusable OpenClaw skill for creating or refreshing bench agents from a 7-file operating pack.

This skill is designed for cases where one OpenClaw installation needs to generate a new agent inside a different OpenClaw installation, using a proven operating pack such as:
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `AGENTS.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `TOOLS.md`

## Install on another OpenClaw workspace

Option A, clone directly into the target workspace skills directory:

```bash
git clone https://github.com/fruteroclub/agent-bench-bootstrap.git ~/.openclaw/workspace/skills/agent-bench-bootstrap
```

Then start a new OpenClaw session in that installation. The skill will be available to the main agent.

Option B, use the packaged artifact from this repo:
- download `agent-bench-bootstrap.skill`
- unpack it into `~/.openclaw/workspace/skills/agent-bench-bootstrap/`

## Recommended operator flow

1. Install this repo into the target OpenClaw workspace.
2. Start a new session with the target installation's main agent.
3. Provide the 7 generated files for the new agent.
4. Ask the main agent to use `agent-bench-bootstrap` to create a new agent, for example a CMO, inside its local OpenClaw installation.
5. Have the main agent validate the rollout before finishing.

## Suggested prompt for the receiving agent

```text
Install and use the `agent-bench-bootstrap` skill from this repository. I am providing a 7-file operating pack for a new CMO agent. Create the new agent inside this OpenClaw installation, preserve the source pack as the authority, back up any conflicting live files before overwrite, and validate the final bootstrap.
```

## Repo contents

- `SKILL.md`
- `references/file-contract.md`
- `references/playbook.md`
- `scripts/validate_agent_bootstrap.py`
- `agent-bench-bootstrap.skill`

## Validation

The validator script can be run with:

```bash
python3 scripts/validate_agent_bootstrap.py <target-agent-directory>
```
