from app.utils.gerador import new_name
from app.negocio import existing_name
from app.negocio.backend import add_name


def main():
    while True:
        name = new_name()
        if not existing_name(name):
            add_name(name)
            break
    
    print(f"New name created: {name}")


if __name__ == "__main__":
    main()
