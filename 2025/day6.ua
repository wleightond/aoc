PREPA ← (
  ⊃⊣↘₋₁
  ⊙(⍉≡⊜⋕ ⊸≠ @ )
  ⊜□ ⊸≠ @ 
  ⊢⍉≡◇=@*
)
PREPB ← ⊜□ ¬≡/× ⊸≡(=@ )⍉
PARSE ← ≡(
  ⟜(□⊜⋕ ⊸≠ @ ◇/$"_ _"⍚≡↘₋₁)
  =@*◇⊣◇⊢
)
APP ← ⨬(◇/+|◇/×)

["123 328  51 64 "
 " 45 64  387 23 "
 "  6 98  215 314"
 "*   +   *   +  "]

PREPA⟜PREPB
˙⍤ =4277556 /+ APP
˙⍤ =3263827 /+ APP PARSE

&fras "inputs/2025/day6.txt"
⊜∘ ⊸≠ @\n
PREPA⟜PREPB
&p /+ APP
&p /+ APP PARSE
