''' 
2476. Closest Nodes Queries in a Binary Search Tree: https://leetcode.com/problems/closest-nodes-queries-in-a-binary-search-tree/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt

Nesse exercícios utilizamos a abordagem de percurso em ordem (in-order traversal) para obter os valores da árvore em ordem crescente.
'''

from typing import Optional, List

# Definição para um nó na árvore binária.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestNodes(self, root: Optional['TreeNode'], queries: List[int]) -> List[List[int]]:
        '''
        Aqui acontece o percurso em ordem (in-order traversal).
        Para isso definimos uma pilha (stack) que vai armazenar os nós da árvore (esquerda, nó, direita).
        Em BST, esse percurso resulta em uma lista crescente de valores.
        '''
        values: List[int] = []
        stack: List['TreeNode'] = []
        node = root

        '''
        Enquanto houver nós na pilha ou o nó atual não for nulo, continuamos o percurso.
        Primeiro, percorremos a subárvore esquerda, empurrando os nós para a pilha.
        '''
        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            # Quando não há mais nós à esquerda, desempilhamos o nó e adicionamos seu valor à lista.
            node = stack.pop()
            values.append(node.val)

            # Em seginda, percorremos a subárvore direita.
            node = node.right

        '''
        Para cada consulta, usamos busca binária.
        Procuramos o índice do primeiro elemento >= q.
        Se index < len(values), então values[index] é o valor mínimo >= q.
        Se index > 0, não existe elemento >= q, maxi = -1.
        Para mini:
        - Se values[index] == q, então mini = q.
        - Se index > 0, então mini = values[index - 1].
        - Senão, não existe elemento < q, então mini = -1.
        '''
        answers: List[List[int]] = []

        for q in queries:
            mini = -1
            maxi = -1

            # Busca binária para encontrar o índice do primeiro elemento >= q
            low, high = 0, len(values) - 1
            index = len(values)

            while low <= high:
                mid = (low + high) // 2
                if values[mid] >= q:
                    index = mid
                    high = mid - 1
                else:
                    low = mid + 1

            # Define maxi
            if index < len(values):
                maxi = values[index]
            # Define mini
            if index < len(values) and values[index] == q:
                mini = q
            elif index > 0:
                mini = values[index - 1]
            
            answers.append([mini, maxi])

        return answers
