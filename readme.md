## Documentação do Projeto: Library Management System

    Desafio da empresa https://olist.com/

### Principais Tecnologias
 - **Django**
 - **Docker**
 - **Restframework (django)**

### que foi feito 
-    **Receber um arquivo CSV com autores e importá-lo para o banco de dados**
-    **Expor os dados dos autores em um endpoint**
-    **Operações de CRUD (Criar, Ler, Atualizar e Deletar) para livros**


```mermaid
classDiagram
  class Book {
    + id: integer
    + name: string
    + edition: integer
    + publication_year: date
    + authors: list
    + cadastrar(name: string, edition: integer, publication_year: date, authors: list): type
  }

  class Author {
    + id: integer
    + name: string
  }

  Book "1" *-- "*" Author
```



<table>
    <tr>
        <th>/authors</th>
        <th>/books</th>
        <th>Um livro pode ter muitos authores</th>
    </tr>
    <tr>
        <td><img src="https://github.com/MatheuslFavaretto/library-olist/assets/116848225/ca729aea-8861-48d9-9944-9a4dc86325f3" alt="/authors"></td>
        <td><img src="https://github.com/MatheuslFavaretto/library-olist/assets/116848225/0ae744c1-7296-4a6c-8b48-b79f139b9f62" alt="/books"></td>
        <td><img src="https://github.com/MatheuslFavaretto/library-olist/assets/116848225/c00ea24c-da7a-48e3-a21a-4436968c23fe" alt="Um livro pode ter muitos authores"></td>
    </tr>
    <tr>






Link do desafio: https://github.com/olist/work-at-olist#1-receive-a-csv-with-authors-and-import-to-database
