PrepA ← (
  ⊃⊣↘₋₁
  ⊙(⍉≡⊜⋕ ⊸≠ @ )
  ⊜□ ⊸≠ @ 
  ⊢⍉≡◇=@*
)
PrepB ← ⊜□ ¬≡/× ⊸≡(=@ )⍉
Parse ← ≡(
  ⟜(□⊜⋕ ⊸≠ @ ◇/$"_ _"⍚≡↘₋₁)
  =@*◇⊣◇⊢
)
Calc ← ⨬(◇/+|◇/×)

["123 328  51 64 "
 " 45 64  387 23 "
 "  6 98  215 314"
 "*   +   *   +  "]

PrepA⟜PrepB
˙⍤ =4277556 /+ Calc
˙⍤ =3263827 /+ Calc Parse

&fras "inputs/2025/day6.txt"
⊜∘ ⊸≠ @\n
PrepA⟜PrepB
&p /+ Calc
&p /+ Calc Parse
