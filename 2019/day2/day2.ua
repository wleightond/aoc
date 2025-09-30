Op     ← ⨂1_2_99⊢
Instr  ← ⨬(↙₄|↙₄|↙₁)⊸Op◡˜↘
Args   ← ⊏↙₂↘₁
Insert ← ⍜⊙⊡ ⊙◌
Store ← Insert ⊙(⊏3)

Add ← Store /+ ◡Args
Mul ← Store /× ◡Args

Step ← (
  Instr
  ⨬(⊙(+4)Add|⊙(+4)Mul|˙⍤0)⊸Op
)
Run      ← ⊙◌◌⍢(⍣⊙Step¬|∘) 1 ⊙0
GetProg  ← ⊜⋕ ⊸≠@,
WithArgs ← Insert⊙1⊙(Insert⊙2)

&fras "input.txt"
GetProg
⟜□

Run WithArgs 12 2
&p ⊏0

⊞(⊟₃) ⊸∘ ⇡100
≡≡(⊏ 0 Run WithArgs ∩°□ ⊙⊙°□ °⊟₃ °¤)
&p +×100 °⊟°¤⊚= 19690720
