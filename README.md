## 🧐 Sobre

O projeto Ting consiste em um programa que simule um algoritmo de indexação de documentos similar ao do Google. O programa deverá ser capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa foi desenvolvido em dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
  #### Nesse módulo eu:
  - Implementei uma fila para armazenar os arquivos que serão lidos
  - Implementei uma função txt_importer dentro do módulo file_management capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.
  - Implementei a função process no módulo file_process. Essa função deverá ser capaz de transformar o conteúdo da lista gerada pela função txt_importer em um dicionário que será armazenado dentro da Queue.
  - Implementei uma função remove dentro do módulo file_process capaz de remover o primeiro arquivo processado.
  - Implementei uma função file_metadata dentro do módulo file_process capaz de apresentar as informações superficiais de um arquivo processado.
  - Implementei os testes para a classe PriorityQueue capaz de armazenar arquivos pequenos de forma prioritária
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.
  #### Nesse módulo eu:
  - Implementei uma função exists_word, dentro do módulo word_search, que verifique a existência de uma palavra em todos os arquivos processados.
  - Implementei uma função search_by_word dentro do módulo word_search, que busque uma palavra em todos os arquivos processados.
  
## Principais tecnologias utilizadas:
- Python

## Contribuição:

Criei as funções dos arquivos que estão dentro da pasta ting_file_management e ting_word_searches, o restante dos arquivos forma criados pela Trybe
