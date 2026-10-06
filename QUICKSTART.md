# 10-minute quickstart

Use this when you want the minimum useful adoption rather than the full template.

You can bootstrap the files automatically:

```bash
python3 scripts/init_foundation.py ../my-game \
  --slug my-game \
  --title "My Game" \
  --runtime browser \
  --implementation-root src
```

## Step 1 — identify the project

Create `.game/project.json` with:

- slug/title;
- current phase/milestone/build number;
- runtime;
- implementation root;
- release/artifact roots.

## Step 2 — create one validation command

Examples:

- browser: `npm run validate`
- Godot: `bash scripts/validate-production.sh`
- Unity: a project-local script that runs compile/editmode/playmode/build checks as appropriate

The foundation does not care about the command name; it cares that one documented entry point exists.

## Step 3 — add repository instructions

Use `AGENTS.template.md` as a starting point and merge it with existing project instructions.

## Step 4 — add minimal docs

Start with:

- `docs/ARCHITECTURE.md`
- `docs/BUILD_AND_TESTING.md`
- `docs/DEPLOYMENT.md` if deployment already exists

## Step 5 — create one release record

Record the current build, known issues and what should be manually tested.

## Step 6 — grow only when needed

Add formal playtests, task records, ADRs, performance budgets and additional documents once the project complexity justifies them.

Finally run:

```bash
python3 scripts/validate_foundation.py ../my-game
```
