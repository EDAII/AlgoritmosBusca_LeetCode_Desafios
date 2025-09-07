''' 
2156. Find Substring With Given Hash Value: https://leetcode.com/problems/find-substring-with-given-hash-value/description/
Exercício resolvido por Ester Flores e Eduardo Schuindt

A solução apresentada utiliza função hash  para contar ocorrências de palavras e a técnica de janela deslizante para encontrar substrings válidas. 
'''

class Solution:
    def subStrHash(
        self, s: str, potencia: int, modulo: int, k: int, valor_hash_alvo: int
    ) -> str:

        hash_atual = 0
        comprimento_string = len(s)
        potencia_k_menos_1 = 1

        # Passo 1: Começa calculando o hash da última substring.
        for i in range(comprimento_string - 1, comprimento_string - 1 - k, -1):
            valor_char = ord(s[i]) - ord("a") + 1
            hash_atual = (hash_atual * potencia + valor_char) % modulo
            if i != comprimento_string - k:
                potencia_k_menos_1 = (potencia_k_menos_1 * potencia) % modulo

        posicao_resultado = -1
        if hash_atual == valor_hash_alvo:
            posicao_resultado = comprimento_string - k

        # Passos 2: Desliza o espaço para a esquerda, atualizando o hash
        # de forma eficiente (remove o char da direita, adiciona o da esquerda).
        for i in range(comprimento_string - 1 - k, -1, -1):
            valor_char_removido = ord(s[i + k]) - ord("a") + 1
            valor_novo_char = ord(s[i]) - ord("a") + 1
            
            hash_atual = (
                (hash_atual - valor_char_removido * potencia_k_menos_1) * potencia + valor_novo_char
            ) % modulo

            # Passos 3: Compara o hash com o alvo e salva a posição. A última
            # posição salva será a resposta, pois é a primeira na ordem da string.
            if hash_atual == valor_hash_alvo:
                posicao_resultado = i

        return s[posicao_resultado : posicao_resultado + k]