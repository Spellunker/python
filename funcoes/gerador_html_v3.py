#!/usr/bin/python3
def tag_bloco(conteudo, classe="success", inline=False):
    tag = "span" if inline else "div"
    return f"<{tag} class='{classe}'>{conteudo}</{tag}>"


def tag_list(*items):
    lista = "".join(f"<li>{item}</li>" for item in items)
    return f"<ul>{lista}</ul>"


if __name__ == "__main__":
    # Testes (assertions)
    print(tag_bloco("bloco"))
    print(tag_bloco("inline e classe", "info", True))
    print(tag_bloco("inline", inline=True))
    print(tag_bloco(inline=True, conteudo="inline"))
    print(tag_bloco("Falhou", classe="error"))
    print(tag_bloco(tag_list("item 1", "item 2"), classe="info"))
