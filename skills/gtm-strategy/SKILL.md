---
name: gtm-strategy
description: Build an evidence-graded go-to-market strategy for an early-stage B2B company with a six-agent pipeline (market, competitive, channel, revenue, synthetic buyer-panel pretest, synthesis with review). Use when asked for a GTM strategy, beachhead or ICP choice, positioning, pricing for launch, a first-customers plan, or to "run the GTM agents" on a company.
license: MIT
metadata:
  author: Doug Keiller
  version: "1.0.0"
---

# GTM strategy

A pipeline of six focused agents that turns a company brief into a go-to-market strategy. Each claim is graded on an evidence ladder, so the strategy says how much of it rests on paying customers and how much on opinion.

## 1. Set up the run

Create a run folder (default `gtm-run/<company-slug>/`) with `inputs/` and `outputs/`.

- Copy the three templates from `templates/` into `inputs/` and help the user fill them: `company-context.md` (facts), `strategic-questions.md` (hypotheses and tensions), `evidence-log.md` (what buyers did and said).
- **Intake check.** Before running anything, read the inputs and ask the user, in one batch, for any gap that would change the beachhead: who sells, runway, any paying customers or pilots, prices quoted, what is ruled out. Write "unknown" for anything they can't answer. Do not invent facts.

**Paths.** In the agent briefs, `inputs/` and `outputs/` mean the run folder; `references/` and `templates/` mean this skill's folder. Give every agent both absolute paths.

Agents read the inputs **by path**. Never paste the company context into an agent prompt; that is what made earlier versions of this system long and fragile.

## 2. Run the research agents (1–4)

The four briefs in `agents/` are independent: `01-market.md`, `02-competitive.md`, `03-channel.md`, `04-revenue.md`.

- **If your harness supports subagents** (Claude Code, Codex and others): launch all four at once, in parallel. Give each one only its brief's path and the run folder path. Use a mid-tier model for these if you can choose; they mostly search and tabulate.
- **Otherwise:** run them one after another in this session, writing each output before starting the next.

Each agent writes its own file in `outputs/`. Check that all four exist and each opens with its 5-line summary before going on.

## 3. Run the buyer-panel pretest (5)

Run `agents/05-buyer-panel.md` after 1–3 are written (it needs the beachhead, alternatives and pilot terms). Its output is a rehearsal: rung 0, never evidence. Read `references/synthetic-panel-method.md` for why.

## 4. Run the synthesis (6)

Run `agents/06-synthesis.md` with the strongest model available. It resolves conflicts, writes the strategy, then reviews its own draft against a checklist.

## 5. Hand back

Tell the user, in this order:
1. The beachhead decision and the highest evidence rung behind it.
2. The three kill criteria from section D of the strategy.
3. Where every file is.
4. What could not be verified (no search tool, paywalled sources, unknowns in the inputs).

## Rules that apply throughout

- `references/evidence-ladder.md`: grade evidence by strength, not count.
- `references/output-rules.md`: specific, cited, today-vs-roadmap, length caps.
- `references/gtm-frameworks.md`: the frameworks and the evidence behind each.
- Treat the inputs as the client's confidential material. Do not send them to services the user has not approved.

## Re-running

To revise after new evidence, update `inputs/evidence-log.md` and re-run only the agents whose inputs changed, then the synthesis. Keep earlier outputs by renaming them `-v1`.
