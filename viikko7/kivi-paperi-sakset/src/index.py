from kps import KPS


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if (len(vastaus) == 1) and ("a" in vastaus or "b" in vastaus or "c" in vastaus):
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )

            peli = KPS(vastaus)
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
