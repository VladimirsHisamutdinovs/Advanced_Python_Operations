
def celsius_to_farenheit(temp):
    return (temp * 9/5) + 32

def farenheit_to_celcius(temp):
    return (temp-32) * 5/9


def main():
    cel_temps = [0, 15, 30, 45]
    far_temps = [24, 32, 55, 218]


    print(list(map(farenheit_to_celcius, far_temps)))
    print(list(map(celsius_to_farenheit, cel_temps)))

    print(list(map(lambda t: (t-32) * 5/9, far_temps)))
    print(list(map(lambda t: (t * 9/5) + 32, cel_temps)))


if __name__ == "__main__":
    main()