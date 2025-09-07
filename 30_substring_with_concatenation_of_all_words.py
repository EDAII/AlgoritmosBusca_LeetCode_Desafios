''' 
30. Substring with Concatenation of All Words: https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt

A solução apresentada utiliza tabela hash para contar ocorrências de palavras e a técnica de janela deslizante para encontrar substrings válidas. 
'''

from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # Verifica se a string 's' ou a lista 'words' está vazia
        if not s or not words:
            return []

        '''
        'w' é o comprimento de cada palavra na lista 'words'.
        Todas as palavras dessa lista têm o mesmo comprimento, então pegamos o comprimento da primeira palavra.
        'k' é o número total de palavras na lista 'words'.
        'total' é o comprimento total que a substring concatenada deve ter.
        'n' é o comprimento da string 's'.
        '''
        w = len(words[0])       
        k = len(words)       
        total = w * k
        n = len(s)

        # Verifica se a string 's' é menor que o comprimento total necessário.
        if n < total:
            return []

        # 'need' é um dicionário que conta quantas vezes cada palavra aparece na lista 'words'.
        need = {}
        for wd in words:
            need[wd] = need.get(wd, 0) + 1

        # 'res' é a lista que armazenará os índices iniciais das substrings concatenadas encontradas.
        res: List[int] = []

        '''
        Aqui percorremos a string 's' com diferentes offsets (0 ... w-1) para garantir que todas as possíveis posições iniciais sejam consideradas.
        'seen' é um dicionário que conta quantas vezes cada palavra foi vista na janela atual.
        'count' é o número de palavras vistas na janela atual.
        '''
        for offset in range(w):
            left = offset
            right = offset
            seen = {}   
            count = 0     

            # Desliza a janela pela string 's' em incrementos do tamanho da palavra 'w'. Pega letra por letra.
            while right + w <= n:
                word = s[right:right + w]
                right += w

                if word in need:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # Se a palavra foi vista mais vezes do que o necessário, move a janela para a direita.
                    while seen[word] > need[word]:
                        left_word = s[left:left + w]
                        seen[left_word] -= 1
                        if seen[left_word] == 0:
                            del seen[left_word]
                        left += w
                        count -= 1

                    # Se o número de palavras vistas é igual ao número total de palavras, adiciona o índice inicial à lista de resultados.
                    if count == k:
                        res.append(left)

                        left_word = s[left:left + w]
                        seen[left_word] -= 1
                        if seen[left_word] == 0:
                            del seen[left_word]
                        left += w
                        count -= 1
                else:
                    # Se a palavra não está na lista 'words', reseta a janela.
                    seen.clear()
                    count = 0
                    left = right

        return res

