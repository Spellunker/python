#!/usr/bin/python3
def tag(tag, *args, **kwargs):
    print(f"<{tag} {kwargs}></{tag}>")


if __name__ == "__main__":
    print(
        tag("p",
            tag("span", "Curso de python 3, por "),
            tag("strong", "Juracy Filho", id="jf"),
            tag("span", "e"),
            tag("strong", "Leonardo Leitão", id="ll"),
            tag("span", "."),
            html_class="alert"
            )
    )
