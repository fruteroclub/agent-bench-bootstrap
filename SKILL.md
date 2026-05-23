---
name: agent-bench-bootstrap
description: Bootstrap or refresh OpenClaw bench agents from a provided 7-file operating pack. Use when an agent needs to create, upgrade, or replicate another agent on the same or a separate OpenClaw installation using files like SOUL.md, IDENTITY.md, USER.md, AGENTS.md, MEMORY.md, HEARTBEAT.md, and TOOLS.md. Triggers include requests to generate a new agent, apply a reference bootstrap pack, clone a proven agent pattern onto another install, or validate that a bench-agent rollout preserved the required operating contract.
---

# Agent Bench Bootstrap

Bootstrap a target OpenClaw agent from a supplied operating pack. Treat the source files as the authority, keep the rollout reversible, and validate the result before declaring success.

## Quick workflow

1. Read `references/file-contract.md` to confirm the required file set and optional outputs.
2. Read `references/playbook.md` and follow the rollout sequence.
3. If a target path is provided, inspect the live target before writing.
4. If the source pack is incomplete or ambiguous, stop and ask only for the missing blocker.
5. If repeated validation is needed, run `scripts/validate_agent_bootstrap.py <target-dir>`.

## Operating rules

- Prefer applying a provided 7-file pack over rewriting the agent from scratch.
- Preserve continuity when the source pack represents an existing persona family. Do not accidentally create a disconnected persona unless the user explicitly wants that.
- Treat overwrite of live agent files as reversible but sensitive. Create a dated backup before replacement unless the user explicitly says not to.
- Preserve installation-specific details only when they do not conflict with the new operating model.
- Do not invent current facts, tool policies, or org details that are not present in the provided files.
- Keep communication concise and diff-oriented.
- Validate before finishing. At minimum check required files, missing files, and forbidden punctuation or style constraints that the source pack imposes.

## Default rollout sequence

### 1. Intake

Confirm:
- target agent id or folder name
- source directory containing the 7 files
- whether this is a net-new agent or an update to an existing one
- whether optional `README.md` and `IMPLEMENTATION-PLAN.md` should also be generated

### 2. Inspect

Inspect both sides before writing:
- source pack contents
- target directory existence and current files
- any local-only notes worth preserving

### 3. Backup

If the target already exists, create a dated backup copy before overwrite.

### 4. Apply

Copy the source files into the target agent directory:
- `SOUL.md`
- `IDENTITY.md`
- `USER.md`
- `AGENTS.md`
- `MEMORY.md`
- `HEARTBEAT.md`
- `TOOLS.md`

Generate optional `README.md` and `IMPLEMENTATION-PLAN.md` only if the user wants them or the installation pattern clearly benefits from them.

### 5. Validate

Run the validator script or equivalent checks. Confirm:
- all required files exist
- no unexpected missing files remain
- no forbidden em dashes if the pack forbids them
- the target agent identity matches the requested role
- the result preserved continuity and specialization

### 6. Summarize

Return:
- outcome: created, updated, or blocked
- files applied
- local details preserved, if any
- validation result
- next action for the operator, if any

## When to stop and ask

Ask one concise question only when a non-retrievable blocker exists, such as:
- source file set is missing one of the seven required files
- target path or agent id is unknown
- the user has not approved overwrite of a live custom agent and the change would replace nontrivial local work

## Output shape

Use a short implementation summary with:
- recommendation
- what changed
- what was preserved
- validation result
- blocker, if any
