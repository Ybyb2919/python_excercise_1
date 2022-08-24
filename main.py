from collections import namedtuple

City = namedtuple("City", "name country population")
Country = namedtuple("Country", "name population")

cities = []
countries = []

def get_population(City):
    return City.population

def get_country(City):
    return City.country

def get_country_population(Country):
    return Country.population

def create_city_list():
    with open('cities_of_the_world.csv', 'r', encoding='utf-8') as f:
        line = f.readline()
        parameters = line.replace("\"", "").split(",")
        while line is not open and line != '':
            line = f.readline()
            parameters = line.replace("\"", "|")
            parameters = parameters.replace("|,|", "~")
            parameters=parameters.replace("|", "").split("~")

            try:
                city = City(name = parameters[0], country=parameters[4], population=parameters[9])
                if (city.population == ""):
                    temp_population = 0
                else:
                    temp_population = (float)(city.population)
                    temp_population = (int)(temp_population)
                temp_city = City(name=city.name, country=city.country, population=temp_population)
                cities.append(temp_city)
            except IndexError:
                print("wtf")

    return cities

def count_country_popluation(list, i):
    country_pop = 0
    while(i+1 < len(list) and list[i].country == list[i+1].country):
        country_pop += list[i].population
        i += 1
    country_pop += list[i].population
    return country_pop

def create_country_list(cities_countries_sorted):
    i=0
    while i < len(cities_countries_sorted):
        while (cities_countries_sorted[i-1].country == cities_countries_sorted[i].country):
            if (i+1 < len(cities_countries_sorted)):
                i += 1
            else:
                break
        new_country = Country(name=cities_countries_sorted[i].country, population=count_country_popluation(cities_countries_sorted, i))
        i += 1
        countries.append(new_country)
    return countries



def ten_biggest_countries(cities, x):
    cities_countries_sorted = sorted(cities, key=get_country)
    countries = create_country_list(cities_countries_sorted)
    countries_sorted = sorted(countries, key=get_country_population)
    for i in range(x):
        print(countries_sorted.pop())



def ten_biggest_cities(cities, x):
    cities_sorted = sorted(cities, key=lambda cities:cities.population)
    for i in range(x):
        print(cities_sorted.pop())

if __name__  == '__main__':
    cities = create_city_list()
    # choose what assignment to execute:
    ten_biggest_cities(cities, 10)
    # ten_biggest_countries(cities, 10)




