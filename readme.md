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
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/280544213-0090f339-5242-44cf-902a-5afe6caccedb.png" alt="/authors"></td>
        <td><img src="https://github-production-user-asset-6210df.s3.amazonaws.com/116848225/280544313-d4d4a325-58f9-4b42-bd4e-dd609ff7efaa.png" alt="/books"></td>
        <td><img src="https://private-user-images.githubusercontent.com/116848225/280543173-c00ea24c-da7a-48e3-a21a-4436968c23fe.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTkyMDU1MjAsIm5iZiI6MTY5OTIwNTIyMCwicGF0aCI6Ii8xMTY4NDgyMjUvMjgwNTQzMTczLWMwMGVhMjRjLWRhN2EtNDhlMy1hMjFhLTQ0MzY5NjhjMjNmZS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMxMTA1JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMTEwNVQxNzI3MDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT01NmRkM2U0OGJhYzk1NzU5NzExMTg2YWRiYTQ1ZTc1NzQwYmIzNGFhZDA5ZTdlYzgwZDBjNzgyNTgxMzJmZTg4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.GQzsDEmcDGa_4BEvgk1nuz2KGdyvV2qWcwXivtA_57U" alt="Um livro pode ter muitos authores"></td>
    </tr>
    <tr>






Link do desafio: https://github.com/olist/work-at-olist#1-receive-a-csv-with-authors-and-import-to-database
