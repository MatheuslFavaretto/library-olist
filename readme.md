## Documentação do Projeto: Library Management System

    desafio olist(https://olist.com/)




classDiagram
  class Book {
    + id: integer
    + name: string
    + edition: integer
    + publication_year: date
    + authors: list
    + cadastrar(name: string, edition: integer, publication_year: date, authors: list): type
    + validar(): boolean
  }

  class Author {
    + id: integer
    + name: string
    + validar(): boolean
  }

  Book "1" *-- "*" Author
