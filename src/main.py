from src.Gem import Gem


def main():
    Rubin = Gem("Rubin", 10000, "USA", 5.25, 200, 1900)
    Emerald = Gem("Emerald", 12500, "Canada")
    Diamond = Gem()
    gem = [Rubin, Emerald, Diamond]
    [print(count_of_object) for count_of_object in gem]


if __name__ =="__main__":
    main()
