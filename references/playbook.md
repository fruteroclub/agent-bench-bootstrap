# Playbook

## Goal

Create or refresh a target OpenClaw agent from a proven operating pack while preserving reversibility and verifying the final state.

## Recommended sequence

### 1. Confirm inputs

Collect or infer:
- target agent name or folder
- target installation path
- source pack path
- create vs update
- whether overwrite is approved
- whether `README.md` and `IMPLEMENTATION-PLAN.md` should be created

If any of the seven required files are missing, stop and ask for the missing file.

### 2. Inspect current state

Check whether the target directory already exists.

If it exists, inspect:
- current bootstrap files
- any local-only notes
- signs the agent has been customized beyond the standard pack

If it does not exist, create the directory and apply the pack as a net-new agent.

## 3. Decide preservation policy

Preserve a local detail only if all are true:
- it exists only in the live target
- it is still useful on this installation
- it does not conflict with the incoming pack
- preserving it will not blur the role or authority of the new agent

Otherwise prefer the source pack.

## 4. Back up before overwrite

When updating an existing agent, create a dated backup directory before replacing files.

Suggested pattern:
- `<target>/backups/YYYY-MM-DD-<agent>-pre-bootstrap-update/`

## 5. Apply files

Copy the seven required files into the target directory.

Generate optional helper files only when asked:
- `README.md`
- `IMPLEMENTATION-PLAN.md`

If generating `IMPLEMENTATION-PLAN.md`, include:
- goal
- target path
- files to update
- implementation principles
- execution sequence
- validation checklist

## 6. Validate

Minimum checks:
- all seven files exist
- all seven files are non-empty
- no em dashes if prohibited by the pack
- target identity and role match the requested agent
- no obvious path mistakes or cross-agent leakage

Useful extra checks:
- grep for the wrong role name in the new pack
- ensure the counterpart name in `USER.md` is still correct
- ensure entity distinctions are preserved in `MEMORY.md` and `AGENTS.md`

## 7. Report

Return a short, operator-grade summary:
- outcome
- backup path, if created
- files written
- local details preserved
- validation findings
- follow-up, if any

## Default decision rules

Recommend update-in-place when the target agent already exists and the new pack is intended to replace its bootstrap.

Recommend net-new creation when the target role or installation path does not already exist.

Recommend pause when:
- overwrite would destroy meaningful local work without backup or approval
- the source pack is incomplete
- the user has not specified which installation path to modify
