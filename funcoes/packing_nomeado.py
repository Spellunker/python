# **kwargs
def resultado_f1(**podium):
    for place, pilot in podium.items():
        print(f"{place} -> {pilot}")


if __name__ == "__main__":
    resultado_f1(primeiro="L. Hamilton",
                segundo="M. Verstappen",
                terceiro="S. Vettel",)
