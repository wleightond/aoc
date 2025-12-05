PREP ← (
  °$"_\n\n_"
  ∩(⊜□⊸≠@\n)
  ≡◇⊜⋕⊸≠@-⊙≡⋕
)
FREE    ← /+>0/+⍉ ˜⊞(×⊃(≤⊙⊢)(≥⊙⊣))
CONT    ← ×⊃(≥⊢)(≤⊣)
RCONT   ← >0+⊃(CONT⊙⊢)(CONT⊙⊣)
OVERLAP ← >0+⊃RCONT˜RCONT
COMB    ← ⊟⊙↥↧⊃∩/↧∩/↥∩°□
ROUND ← (
  ⊸˙⊞◇OVERLAP
  ⊚↧¬˙⊞≤⇡⊸⧻
  >0⊸⧻
  ⨬(◌
  | ⊚¬⤚∊⊙(⇡⊸⧻)⊢
    ⊸⊙(/COMB⍜⊙¤≡⊡)
    ⊃⊙⋅∘⋅□
    ⍜⊙¤≡⊡
    ⊂)
)
FRESH ← (
  ≡□⊙[]
  ◌⍢(⊸ROUND⊙◌|¬◡⍜∩□=)
  +1≡◇/-
  /+
)
INPUT ← PREP &fras "inputs/2025/day5.txt"
TDA ← [[3 5]
       [10 14]
       [16 20]
       [12 18]]
TDB ← [1
       5
       8
       11
       17
       32]

˙⍤ =3 FREE TDA TDB
˙⍤ =14 FRESH TDA

&p FREE INPUT
&p FRESH INPUT
