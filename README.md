# Testing Identifier


## Especificação do Programa Identifier


O programa Identifier determina se um identificador é válido. Um identificador válido deve começar com uma letra e conter apenas letras ou dígitos. Além disso, deve ter no mínimo um caractere e no máximo seis caracteres de comprimento.


## Metodos usados para definir os dados de teste:

Parcionamento em classe de equivalencia e análise de valor limite

## Criterios particionamento em classe de equivalência e análise de valor limit:
1. Maior ou igual a 1.
2. Menor ou igual a 6
3. Inicia com letra      
4. Não inicia com letra
5. Contém apenas letras ou digitios    
6. Contém caracteres diferentes de letras e digitos


## Plano de testes:

|    ID     | Modulo    |  Roteiro| Resultado   | 
|-----------|-----------|---------|---------------------|
| 1      | Identifier      |  "b" | valid            |
| 2      | Identifier      |   "a19763"  | valid            |
| 3      | Identifier     |  ""  | invalid            |
| 4      | Identifier     |  "4"  | invalid            |
| 5      | Identifier     |  "c123546" | invalid            |
| 6      | Identifier     |  b*&34 | invalid            |








