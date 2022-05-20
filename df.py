def hello(name,age):
    year=2022-age
    print("Welcome to Akirachix")
    # return
    return f"Hello {name} you were born in {year}"

def greeting(name, age):
    year=2022-age
    return f"Hello {name} you were born in {year}"


def my_country(country="Uganda", student="Verite"):
    return f"Hello you are a {student} from {country}"
    

my_country() 
my_country(country="Kenya")

def greet_multiple(*names):
    print(names)

    for name in names:
        print("hello {name}")

def sum(*numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum

def multiply(*numbers):
    multiplication=1
    for num in numbers:
        multiplication+=num
        return multiply


def greet_multiple(**kwags):
    print(kwags)
    print(kwags.keys())
    print(kwags.values())

def greet_multiple(**kwags):
    print(kwags)
    print(kwags.keys())
    print(kwags.values())
    keys=kwags.keys()
    if 'country' in kwags:
        print(f"Hello {kwags['name']} you are from {kwags['country']} ")
    if 'age' in kwags:
        year=2022-kwags['age']
        print(f"Hello {kwags['name']} you are from {kwags['country']} you were born in {year} ")
    elif not kwags:
        print(f"Hello Anonymous")


def sum_and_greet(*args,**kwags):
    sum=0
    for num in args:
        sum+=num
    keys=kwags.keys()
    if "name" in keys:
        print(f"Hello {kwags['name']} the answer is {sum}")
    elif "country" in keys:
        print(f"Hello   {kwags['country']} the answer is{sum}")
    elif not kwags:
        print(f"Hello Anonymous the answer is  {sum}")

