# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

a = {1, 2, 3}
b = {1, 3, 4, 5}
a_b_uniao = a | b # União
a_b_inter = a & b # intersecção
a_b_dif = a - b # diferença (exclusividade do set da esquerda)
a_b_sim = a ^ b # items exclusivos de ambos
print(a_b_uniao)
print(a_b_inter)
print(a_b_dif)
print(a_b_sim)