"""Text-search checks for the golden rubric. Usage: python3 check.py <run-folder>
Prints PASS / FAIL / REVIEW per item. REVIEW means a person must read the file."""
import re, sys, pathlib

out = pathlib.Path(sys.argv[1]) / "outputs"
f = {k: (out / n).read_text() if (out / n).exists() else "" for k, n in {
    "01": "01-market.md", "02": "02-competitive.md", "03": "03-channel.md",
    "04": "04-revenue.md", "05": "05-buyer-panel.md", "06": "06-gtm-strategy.md"}.items()}

def has(k, *pats):
    return all(re.search(p, f[k], re.I | re.S) for p in pats)

checks = {
 "A1 segment scoring": has("01", r"\|.*score", r"\|\s*\d"),
 "A2 TAM/SAM/SOM": has("01", r"TAM", r"SAM", r"SOM"),
 "A3 personas+objections": has("01", r"persona", r"objection"),
 "A4 competitor tiers": has("02", r"direct", r"indirect|adjacent"),
 "A5 positioning maps": has("02", r"2\s*[x×]\s*2|positioning map"),
 "A6 7 Powers": has("02", r"7 Powers|seven powers|counter-position"),
 "A7 motion table": has("03", r"\|.*feasib"),
 "A8 12-month plan": has("03", r"month\s*1|M1|month 12|12-month"),
 "A9 bear/base/bull": has("04", r"bear", r"base", r"bull"),
 "A10 sensitivity": has("04", r"sensitivity", r"50\s*%"),
 "A11 conflict table": has("06", r"\|\s*conflict"),
 "A12 positioning statement": has("06", r"\bfor\b.*\bwho\b.*\bunlike\b.*\bbecause\b"),
 "A13 90 days + gates": has("06", r"90", r"gate"),
 "A14 exec brief": has("06", r"executive brief"),
 "B1 rung stated": has("01", r"rung") and has("06", r"rung"),
 "B2 user/budget/blocker": has("01", r"budget holder", r"blocker"),
 "B3 case study": has("01", r"case study"),
 "B4 status quo alternative": has("02", r"status quo|do(ing)? nothing|manual|paper"),
 "B5 personal sales first": has("03", r"founder-led|personal sell"),
 "B6 paid pilot": has("03", r"paid pilot") or has("06", r"paid pilot"),
 "B7 sales-hire gate": has("03", r"(first|hire).{0,40}(sales|AE|rep)"),
 "B8 WTP range + commitment": has("04", r"range", r"(deposit|paid pilot|pre-order|LOI)"),
 "B9 panel rung-0, no prices": has("05", r"rung 0") and not re.search(r"(would pay|willing to pay)\s*(USD|\$)\s*\d", f["05"], re.I),
 "B10 past-behaviour questions": has("05", r"last time|tell me about") or has("06", r"last time|tell me about"),
 "B11 kill criteria": has("06", r"kill"),
}
for k, v in checks.items():
    print(("PASS " if v else "FAIL ") + k)
print("REVIEW B12 roadmap features not treated as available (read 06, sections B and E)")
print("REVIEW every PASS above is a keyword match; spot-read the sections")
missing = [k for k, v in f.items() if not v]
if missing:
    print("MISSING outputs:", missing)
