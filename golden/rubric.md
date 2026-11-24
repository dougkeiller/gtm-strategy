# Golden-set rubric

Run the skill on `examples/fieldnote/` and check the outputs against these items. Each is pass / fail, judged by reading the output; `check.py` automates the ones a text search can settle and flags the rest for a human.

## A. Parity with the original five-agent system (nothing lost)

| # | Check | File |
|---|---|---|
| A1 | Segment scoring table with numeric scores | 01 |
| A2 | TAM / SAM / SOM with arithmetic shown | 01 |
| A3 | Two buyer personas with objections and responses | 01 |
| A4 | Competitor profiles across tiers | 02 |
| A5 | Two positioning maps (2×2) | 02 |
| A6 | 7 Powers moat analysis | 02 |
| A7 | Motion rating table | 03 |
| A8 | Month-by-month 12-month plan | 03 |
| A9 | Bear / base / bull unit economics | 04 |
| A10 | Sensitivity on three assumptions at ±50% | 04 |
| A11 | Conflict-resolution table | 06 |
| A12 | Positioning statement in the "For… who… is the… unlike… because" form | 06 |
| A13 | 90-day plan and decision gates | 06 |
| A14 | One-page executive brief | 06 |

## B. New best practices (from the verified research)

| # | Check | File |
|---|---|---|
| B1 | Evidence rung stated for the beachhead, in the opening summary | 01, 06 |
| B2 | User, budget holder and blocker separated | 01 |
| B3 | Repeatable case study paragraph | 01 |
| B4 | Competitive alternatives include the status quo / manual workaround, listed first | 02 |
| B5 | Founder-led personal selling before mass-media marketing | 03 |
| B6 | Pilot terms paid by default (or a stated reason for free) | 03, 06 |
| B7 | A gate before the first sales hire, tied to repeatability | 03, 06 |
| B8 | Willingness to pay reported as a range, with a paid commitment as the test | 04 |
| B9 | Buyer panel opens with the rung-0 label and reports no price points | 05 |
| B10 | Discovery questions written as past-behaviour questions | 05 or 06 |
| B11 | Kill criteria for 3–5 hypotheses | 06 |
| B12 | Roadmap features (Fieldnote: warranty drafting, integrations) not treated as available | all |

## C. Efficiency (measured, not judged)

| # | Measure | Original system | This version |
|---|---|---|---|
| C1 | Prompt words across all agent files | ~35,000 (five prompts of ~7,000, mostly repeated context) | ~4,900 for the whole skill |
| C2 | Manual copy-paste steps between agents | 4 (paste each output into the synthesis prompt) | 0 (agents read files by path) |
| C3 | Research agents run in parallel | Described, but run by hand | Yes, where the harness has subagents |
