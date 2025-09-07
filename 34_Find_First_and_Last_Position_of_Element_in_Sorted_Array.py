''' 
34. Find First and Last Position of Element in Sorted Array: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt

A solução apresentada utiliza busca binária usando o biect_left do python
'''

from typing import List
from bisect import bisect_left

class Solution:
    def searchRange(self, nums: List[int], alvo: int) -> List[int]:
       # Encontra a posição mais à esquerda onde o 'alvo' poderia ser inserido
        indice_esquerdo = bisect_left(nums, alvo)

        # Encontra a posição mais à esquerda onde ('alvo' + 1) poderia ser inserido.
        # Isso nos dá a posição logo após a última ocorrência do 'alvo'.
        indice_direito = bisect_left(nums, alvo + 1)

        # Se o indice_esquerdo for igual ao indice_direito, o 'alvo' não existe na lista.
        if indice_esquerdo == indice_direito:
            return [-1, -1]
        # Caso contrário, retorna o intervalo [indice_esquerdo, indice_direito - 1].
        else:
            return [indice_esquerdo, indice_direito - 1]