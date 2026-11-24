# gtm-strategy

An open-source agent skill that builds a go-to-market strategy for an early-stage B2B company, and says how much of that strategy rests on evidence.

It runs six focused agents:

| # | Agent | Produces |
|---|---|---|
| 1 | Market and customer discovery | Segment scoring, beachhead, ICP, user vs budget holder vs blocker, bottom-up sizing |
| 2 | Competitive landscape | Alternatives (incl. the status quo), competitor map, positioning maps, 7 Powers |
| 3 | Channel and first customers | Motion sequencing, first-ten-customers plan, paid-pilot terms, scaling gates |
| 4 | Pricing and unit economics | Revenue model, price-before-product plan, bear/base/bull economics, sensitivity |
| 5 | Synthetic buyer panel | A **pretest**: AI plays the buying roles to surface objections and interview questions |
| 6 | Synthesis and review | Conflict resolution, binding beachhead, positioning, 90-day tests with kill criteria, self-review |

Agents 1–4 run in parallel where the harness supports subagents. Agent 5 needs 1–3, and agent 6 needs all five.

## What makes it different

- **An evidence ladder.** Every claim about buyers is graded from rung 0 (AI or founder belief) up to rung 5 (a paying customer). The strategy has to say up front if its beachhead rests on opinion. Fifty interviews are still opinions; a paid pilot is evidence. See [`references/evidence-ladder.md`](plugin/skills/gtm-strategy/references/evidence-ladder.md).
- **Price before product.** Pilots default to paid. Willingness-to-pay talk produces ranges, not proof.
- **Synthetic customers, used honestly.** Recent research shows LLM "synthetic consumers" can reproduce the ranking of consumer survey results, but are weak on individual buyers and on price. None of that research tested B2B buyers. So the panel is a rehearsal that produces better discovery questions, never market evidence. See [`references/synthetic-panel-method.md`](plugin/skills/gtm-strategy/references/synthetic-panel-method.md).
- **Sourced frameworks.** Each framework the agents use is listed with what its source supports and how strong that support is. See [`references/gtm-frameworks.md`](plugin/skills/gtm-strategy/references/gtm-frameworks.md).
- **Lean prompts.** Company facts live in one input file that every agent reads by path, instead of being pasted into every prompt.

## Install

**Claude Code (plugin):**
```
/plugin marketplace add dougkeiller/gtm-strategy
/plugin install gtm-strategy@gtm-strategy
```

**Other harnesses** (Codex, Gemini CLI, Cursor, Copilot and others): see [AGENTS.md](AGENTS.md).

## Use

Ask: "Run the GTM strategy skill on my company." The skill copies three templates into `gtm-run/<company>/inputs/`, asks for any missing facts, runs the agents and writes everything to `gtm-run/<company>/outputs/`.

Inputs:
- `company-context.md`: facts about the company, product, customers and constraints
- `strategic-questions.md`: the hypotheses and tensions you want tested
- `evidence-log.md`: what buyers actually did and said

A worked input set for a fictional company is in [`examples/fieldnote/`](examples/fieldnote/).

## Limits

- The agents can only be as current as the web search your harness provides. Without search, market facts are marked unverified.
- Outputs are drafts for a human strategist to challenge, not decisions.
- The synthetic panel is untested on B2B buyers, so treat it as a brainstorming aid.

## License

MIT
