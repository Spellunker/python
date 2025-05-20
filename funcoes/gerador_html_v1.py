#!/usr/bin/python3


def tag_bloco(text, classe="success"):
    return f"<div class='{classe}'>{text}</div>"


if __name__ == "__main__":
    # Testes (assertions)
    assert tag_bloco("Successfully included!") == \
        "<div class='success'>Successfully included!</div>"
    assert tag_bloco("Impossible exclusion!", "error") == \
        "<div class='error'>Impossible exclusion!</div>"
    print(tag_bloco("bloco"))
