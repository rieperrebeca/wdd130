file_name = "life-expectancy.csv"

with open(file_name) as file:
    next(file)

    overall_min = 9999
    overall_max = -9999
    min_country = ""
    min_year = 0
    max_country = ""
    max_year = 0

    data = []

