---
target: wireframes/case.html
total_score: 27
max_score: 36
na_heuristics: 9
p0_count: 0
p1_count: 2
target_identity: "file:C:\\Users\\Oleksii Tsybin\\Projects\\SkinHub\\wireframes\\case.html"
target_fingerprint: "sha256:c97564d628fc277636da8befe25f4838f25df37a4a3f050009552a0acd895e36"
target_path: "C:\\Users\\Oleksii Tsybin\\Projects\\SkinHub\\wireframes\\case.html"
timestamp: 2026-10-03T17-29-17Z
slug: wireframes-case-html
---
Method: dual-agent (A: design review · B: detector + browser)

| # | Heuristic | Score | Key issue |
|---|---|---|---|
| 1 | System status | 3 | Roulette wait has no progress cue |
| 2 | Real world | 4 | Native CS2 language |
| 3 | User control | 3 | Demo/Real absent in state D |
| 4 | Consistency | 2 | Real · $2.00 in B; label "B, C, D" for four states; bar widths ≠ labels (fixed) |
| 5 | Error prevention | 3 | No confirm on real open |
| 6 | Recognition | 3 | Seeds unexplained |
| 7 | Flexibility | 4 | Fast mode, x1–x10, hotkeys |
| 8 | Minimalist | 2 | State D: five actions, two lime buttons |
| 9 | Error recovery | n/a | No error states drawn |
| 10 | Help | 3 | How it works link had no href (fixed) |
| Total | | 27/36 | Good (75%) |

Priority issues:
- [P1] Pins shared the product lime → fixed: pins and note numbers neutral white.
- [P1] State notes far from their phones → not fixed: structure is frozen by the brief.
- [P2] Left pins covered headings → fixed: moved into the bezel.
- [P2] Data inconsistencies → bar widths fixed; Real · $2.00 and section label left (text frozen).
- [P2] Win moment underpowered → fixed: image 220px, price --fs-5xl.

Detector: 164 CLI findings; 46 low-contrast are false positives (tokens not resolved statically; 0/402 failures in browser); nested-cards and ai-color-palette are false positives (device frames, rarity tints); reel text overflow true (widened, long names still ellipsized); small text in 340px mockups expected.
