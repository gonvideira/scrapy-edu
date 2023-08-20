from datetime import date

CAR_TYPE = 'city-car'
PAGE = 1
KM_MIN = 500
KM_MAX = 125000
PRICE_MIN = 500
PRICE_MAX = 100000
NUMBER_YEARS = 5

url_current_year = date.today().year
url_beginning_year = url_current_year - NUMBER_YEARS + 1

url = (
    "https://www.standvirtual.com/graphql?operationName=listingScreen&variables="
    "%7B%22click2BuyExperimentId%22%3A%22%22%2C%22click2BuyExperimentVariant%22%3A%22"
    "%22%2C%22experiments%22%3A%5B%7B%22key%22%3A%22MCTA-900%22%2C%22variant%22%3A%22a"
    "%22%7D%2C%7B%22key%22%3A%22MCTA-1028%22%2C%22variant%22%3A%22a%22%7D%2C%7B%22"
    "key%22%3A%22MCTA-1029%22%2C%22variant%22%3A%22a%22%7D%5D%2C%22filters%22%3A%5B%7B%22"
    F"name%22%3A%22filter_enum_body_type%22%2C%22value%22%3A%22{CAR_TYPE}%22%7D%2C%7B%22name%22%3A%22" # city car
    f"filter_float_first_registration_year%3Ato%22%2C%22value%22%3A%22{url_current_year}%22%7D%2C%7B%22name%22%3A%22" # current year
    f"filter_float_mileage%3Afrom%22%2C%22value%22%3A%22{KM_MIN}%22%7D%2C%7B%22name%22%3A%22" # kms min
    f"filter_float_mileage%3Ato%22%2C%22value%22%3A%22{KM_MAX}%22%7D%2C%7B%22name%22%3A%22" # kms max
    f"filter_float_price%3Afrom%22%2C%22value%22%3A%22{PRICE_MIN}%22%7D%2C%7B%22name%22%3A%22" # price min
    f"filter_float_price%3Ato%22%2C%22value%22%3A%22{PRICE_MAX}%22%7D%5D%2C%22includeClick2Buy%22%3Afalse%2C%22" # price max
    "includeFiltersCounters%22%3Afalse%2C%22includePriceEvaluation%22%3Atrue%2C%22includePromotedAds%22%3Atrue%2C%22"
    "includeRatings%22%3Afalse%2C%22includeSortOptions%22%3Atrue%2C%22maxAge%22%3A60%2C%22"
    f"page%22%3A{PAGE}%2C%22parameters%22%3A%5B%22origin%22%2C%22make%22%2C%22version%22%2C%22" # page
    "model%22%2C%22engine_code%22%2C%22fuel_type%22%2C%22first_registration_month%22%2C%22first_registration_year%22%2C%22"
    f"mileage%22%2C%22engine_power%22%5D%2C%22searchTerms%22%3A%5B%22carros%22%2C%22desde-{url_beginning_year}%22%5D%7D&" # first year
    "extensions=%7B%22persistedQuery%22%3A%7B%22sha256Hash%22%3A%2250e3cc18dfb6ea5468e45630696e2e5bd35e7"
    "bc8acc7555bc32419ddececae32%22%2C%22version%22%3A1%7D%7D"
    )

print(url)
