Prep    ← ≡◇⊜⋕ ⊸≠@- ⊙≡⋕ ∩(⊜□⊸≠@\n) °$"_\n\n_"
Free    ← /+ >0 /+ ⍉ ˜⊞(× ⊃(≤⊙⊢) (≥⊙⊣))
Cont    ← × ⊃(≥⊢) (≤⊣)
RngCont ← >0 + ⊃(Cont⊙⊢) (Cont⊙⊣)
Overlap ← >0 + ⊃RngCont ˜RngCont
Merge   ← ⊟ ⊙↥↧ ⊃∩/↧ ∩/↥ ∩°□
Others  ← ⊚¬⤚∊ ⊙(⇡⊸⧻)⊢
Recomb  ← ⊂ ⍜⊙¤≡⊡ ⊃⊙⋅∘⋅□
Round ← (
  ⊸˙⊞◇Overlap
  >0⊸⧻ ⊚ ↧¬˙⊞≤ ⇡⊸⧻
  ⨬(◌|Recomb⊸⊙(/Merge ⍜⊙¤≡⊡)Others)
)
Collapse ← ◌⍢(⊸Round⊙◌|¬◡⍜∩□=) ≡□⊙[]
Fresh    ← /+ +₁ ≡◇/- Collapse
Input    ← Prep &fras "inputs/2025/day5.txt"
TDR      ← [3_5 10_14 16_20 12_18]
TDN      ← [1 5 8 11 17 32]

˙⍤ =3 Free TDR TDN
˙⍤ =14 Fresh TDR

&p Free Input
&p Fresh ⍆⊙◌ Input
