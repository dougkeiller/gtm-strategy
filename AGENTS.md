# For agent harnesses other than Claude Code

The skill lives in `plugin/skills/gtm-strategy/` and follows the open Agent Skills format (a folder with `SKILL.md`). To use it:

- **Codex, Gemini CLI, Cursor, OpenCode and others that read `.agents/skills/`:** copy or symlink `plugin/skills/gtm-strategy` into `.agents/skills/` in your project (or `~/.agents/skills/` for all projects).
- **GitHub Copilot in VS Code:** copy it into `.github/skills/`.
- **Any chat assistant without skill support:** paste `SKILL.md` as instructions, then paste each file from `agents/` in order, attaching the files it says to read.

Where the harness has no subagents, the skill runs the six agents one after another in a single session.
