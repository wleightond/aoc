PREP    ← ≡◇⊜⋕ ⊸≠@- ⊙≡⋕ ∩(⊜□⊸≠@\n) °$"_\n\n_"
FREE    ← /+ >0 /+ ⍉ ˜⊞(× ⊃(≤⊙⊢) (≥⊙⊣))
CONT    ← × ⊃(≥⊢) (≤⊣)
RNGCONT ← >0 + ⊃(CONT⊙⊢) (CONT⊙⊣)
OVERLAP ← >0 + ⊃RNGCONT ˜RNGCONT
MERGE   ← ⊟ ⊙↥↧ ⊃∩/↧ ∩/↥ ∩°□
OTHERS  ← ⊚¬⤚∊ ⊙(⇡⊸⧻)⊢
RECOMB  ← ⊂ ⍜⊙¤≡⊡ ⊃⊙⋅∘⋅□
ROUND ← (
  ⊸˙⊞◇OVERLAP
  >0⊸⧻ ⊚ ↧¬˙⊞≤ ⇡⊸⧻
  ⨬(◌|RECOMB⊸⊙(/MERGE ⍜⊙¤≡⊡)OTHERS)
)
COLLAPSE ← ◌⍢(⊸ROUND⊙◌|¬◡⍜∩□=) ≡□⊙[]
FRESH    ← /+ +₁ ≡◇/- COLLAPSE
INPUT    ← PREP &fras "inputs/2025/day5.txt"
TDR      ← [3_5 10_14 16_20 12_18]
TDN      ← [1 5 8 11 17 32]

˙⍤ =3 FREE TDR TDN
˙⍤ =14 FRESH TDR

&p FREE INPUT
&p FRESH ⍆⊙◌ INPUT
