Goal: extract change-of-control clauses from contracts with regex + post-filters.
Inputs: plain-text contracts.
Method:
  1) Scan for keywords: "change of control", "change in control", "control of", "acquires more than", "50% or more".
  2) Capture surrounding sentences (±1).
  3) Heuristics: require verbs like "shall", "terminat", "consent", "notice", or % thresholds.
Output: JSON lines with file, match, span, sentence.
Limitations: regex misses paraphrases; add LLM reranker later.
