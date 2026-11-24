# Synthetic panel method and its limits

Why the buyer panel is a pretest and not a substitute for talking to buyers. All findings below come from consumer or general-population studies; **none tested B2B buyers or buying committees**, so transfer to B2B is unvalidated.

## What the research supports

| Finding | Source |
|---|---|
| Free-text answers mapped to a rating scale reproduced the *ranking* of 57 consumer product concepts at about 90% of human test–retest reliability. Asking the model for a number directly collapsed answers to the midpoint. | Maier et al. 2025, arXiv 2510.08338 |
| With no persona detail the distribution looked right but ranking accuracy fell to about 50%: a good-looking distribution alone proves nothing. | Maier et al. 2025 |
| Reported "twin accuracy" ranges from near-perfect to near-chance depending on what is measured; aggregate matches can hide zero person-level differentiation. Ungrounded willingness-to-pay estimates have been off threefold, with wrong signs. | Netzer & Sambandam 2026, arXiv 2609.13995 |
| Personas built from descriptions (demographics, personality) recovered 7–12% of human test–retest at the individual level; adding the person's past behaviour raised this to 28%. | Pourtaheri & Zareei 2026, arXiv 2610.03998 |
| AI-moderated interviews found more customer needs per dollar than human or static interviews; richer interviews did not make digital twins more accurate. | Deng, Liu, Toubia & Jain 2026, arXiv 2609.29143 |
| Human–AI hybrids beat either alone for qualitative work; synthetic quantitative data gets direction right but variance, correlations and levels wrong. | Arora, Chakraborty & Nishimura 2025, *Journal of Marketing* 89(2) |
| Synthetic samples matched means but flipped the sign on about a third of differing coefficients and shifted with prompt wording and over time. | Bisbee et al. 2024, *Political Analysis* 32(4) |
| LLMs failed to reproduce human distributions on a novel game; results were brittle to language, role and model version. | Gao et al. 2025, *PNAS* |

## Rules the panel follows

1. **Free text first, rating second, in a separate pass.** The published method maps text to ratings with embeddings; a prompt-only skill cannot, so a second pass rates each answer against the fixed anchors below. The paper's comparable "follow-up rating" method scored lower than embeddings (about 85% vs 90% of test–retest), so treat ratings as coarse.
2. **Ground in behaviour.** Use real evidence-log entries for each role wherever they exist; mark ungrounded personas.
3. **Report rankings and themes, never levels.** No price points, no purchase-probability numbers, no subgroup differences.
4. **Vary the prompt.** Run the key reaction twice with reworded stimuli; report only findings that survive both.
5. **Always rung 0.** Output becomes discovery questions.

## Anchor scale for the rating pass
Rate each free-text reaction against the closest statement:
1. "This isn't a problem worth my time." 
2. "Interesting, but I wouldn't change how we do this."
3. "I'd take a meeting to learn more."
4. "I'd agree to a pilot if the terms were right."
5. "I'd push to get this approved."
