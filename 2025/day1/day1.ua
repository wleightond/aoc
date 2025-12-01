PREP ← (
  ⍜⊜∘≡⋅"-" ⊸⦷ "L"
  ⍜⊜∘≡⋅"+" ⊸⦷ "R"
  ⊜⋕ ⊸≠ @\n
)
COUNT ← /+ =0 ◿100 \+ ⊂50

TD ← "L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82"

PREP TD
COUNT
⍤. =3

UNFURL ← (
  ≡□
  ⊂□[]
  /⍜∩°□(
    ⊂⊙(×⍥1⊃⌵±)
  )
  °□
)

UNFURL PREP TD
COUNT
⍤. =6

PREP &fras "../../inputs/2025/day1.txt"
⊃UNFURL∘
∩COUNT
∩&p
