from django import template

register = template.Library()  #registar o filtro

@register.filter(name='plural_comentarios')  #registar o filtro
def plural_comentarios(num_comentarios):  #função do filtro comentarios
    try:
        num_comentarios = int(num_comentarios)  #convertendo para inteiro
        #verificando se ha comentarios ou não
        if num_comentarios == 0:
            return f'Nenhum comentario'
        elif num_comentarios == 1:
            return f'{num_comentarios} comentario'
        else:
            return f'{num_comentarios} comentario(s)'

    except:
        return f'{num_comentarios} comentario(s)'