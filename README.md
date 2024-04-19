# Recursos
• Aplicação biblioteca: https://bibliotecalusofona.pythonanywhere.com/
• Código: https://github.com/ULHTPW/bibliotecalusofona/tree/main/biblioteca
• Aplicação admin (usr:admin, pwd:admin): https://bibliotecalusofona.pythonanywhere.com/admin/

Passos para Criação da Aplicação

1. Analisar a modelação em [models.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/models.py)
2. Ver dados na aplicação [admin](https://bibliotecalusofona.pythonanywhere.com/admin) (usr:admin, pwd:admin)
3. Analisar como [admin.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/admin.py) configura a visualização das tabelas, em particular o uso de ordering, list_display, list_filter, inlines
4. Criar [layout.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/templates/biblioteca/layout.html), para herança de templates.
5. Em views, [importar](https://github.com/ULHT-PW/bibliotecalusofona/blob/ed89e9b8fbd2ead9b8e704be424c8c8c5da3b30a/biblioteca/views.py) os modelos Autor e Livro para poder inserir dados
5. Página de autores:
    1. Para listar autores, criar a view index_view
    1. Criar template index.html que liste autores
    1. Criar caminho para a view index_view em urls.py
1. Página de um autor
    1. Para apresentar informação de um autor, criar a view autor_view
    1. Criar template autor.html, que apresente todas as informações do autor, incluindo seu retrato e lista de livros. 
    1. Criar templatetag para ordenar os livros pelo ano de publicação. Usar filtro livros_ordenados no template.
    1. Criar caminho para a view autor_view em urls.py
    1. Inserir, na lista de autores, um link no autor, para a respetiva página do autor
1. Página de géneros:
    1. Para listar géneros, criar a view géneros_view, onde cria a lista de géneros 
    1. Criar template generos.html que liste os géneros
    1. Criar caminho generos para a view generos_view, em urls.py
1. Página de género:
    1. Para apresentar lista dos livros de um género, criar a view genero_view
    1. Criar template genero.html, que apresente livros de um género. 
    1. Criar caminho genero para a view genero_view, em urls.py
    1. Inserir, na lista de géneros, um link no genero, para a página do género
1. Incluir, no template layout.html, menu com links para as páginas autores e géneros.
