# Tutorial: criação de web app em Django com views, templates e urls.

### Recursos
* Aplicação biblioteca: https://bibliotecalusofona.pythonanywhere.com/
* Código: https://github.com/ULHTPW/bibliotecalusofona/tree/main/biblioteca
* Aplicação admin (usr:admin, pwd:admin): https://bibliotecalusofona.pythonanywhere.com/admin/

### Passos já realizados
Considera-se que:
* já foi feita a modelação dos dados da aplicação em [models.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/models.py)
* existem disponiveis na [pasta json](https://github.com/ULHT-PW/bibliotecalusofona/tree/main/biblioteca/json) dados para alimentar a base de dados
* foram carregados dados disponiveis em JSON, usando um [script](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/loader.py)  

### Passos para criação da aplicação
1. Analisar a modelação em [models.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/models.py)
2. Ver dados na aplicação [admin](https://bibliotecalusofona.pythonanywhere.com/admin) (usr:admin, pwd:admin)
3. Analisar como [admin.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/admin.py) configura a visualização das tabelas, em particular o uso de ordering, list_display, list_filter, inlines
4. Criar [layout.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/templates/biblioteca/layout.html), para herança de templates.
5. Em views, [importar](https://github.com/ULHT-PW/bibliotecalusofona/blob/ed89e9b8fbd2ead9b8e704be424c8c8c5da3b30a/biblioteca/views.py) os modelos Autor e Livro para poder inserir dados
5. Página de autores:
    1. Para listar autores, criar a view [index_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py)
    1. Criar template [index.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/index.html) que liste autores
    1. Criar caminho para a view index_view em [urls.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py)
1. Página de um autor
    1. Para apresentar informação de um autor, criar a view [autor_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py)
    1. Criar template [autor.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html), que apresente todas as informações do autor, incluindo seu [retrato](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html) e lista de livros. 
    1. Criar [templatetag](https://github.com/ULHT-PW/bibliotecalusofona/blob/main/biblioteca/templatetags/biblioteca_extras.py) para ordenar os livros pelo ano de publicação. Usar filtro [livros_ordenados](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html) no template.
    1. Criar caminho para a view autor_view em [urls.py](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py)
    1. Inserir, na lista de autores, um [link no autor](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/index.html), para a respetiva página do autor
1. Página de géneros:
    1. Para listar géneros, criar a view [generos_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py), onde cria a [lista de géneros](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py) 
    1. Criar template [generos.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/generos.html) que liste os géneros
    1. Criar [caminho generos](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py) para a view generos_view, em urls.py
1. Página de género:
    1. Para apresentar [lista](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py) dos livros de um género, criar a view [genero_view](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/views.py)
    1. Criar template [genero.html](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/autor.html), que apresente livros de um género. 
    1. Criar [caminho genero](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/urls.py) para a view genero_view, em urls.py
    1. Inserir, na lista de géneros, um [link no genero](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/generos.html), para a página do género
1. Incluir, no template layout.html, [menu com links](https://github.com/ULHT-PW/bibliotecalusofona/blob/4a6800349d89af51cf9c4365d1f9f2f58d581820/biblioteca/templates/biblioteca/layout.html) para as páginas autores e géneros.
