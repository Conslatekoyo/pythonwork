

# def sum_and_greet(*args,**kwags):
#     sum=0
#     for num in args:
#         sum+=num
#     keys=kwags.keys()
#     if "name" in keys:
#         print(f"Hello {kwags['name']} the answer is {sum}")
#     elif "country" in keys:
#         print(f"Hello   {kwags['country']} the answer is{sum}")
#     elif not kwags:
#         print(f"Hello Anonymous the answer is  {sum}")

# def practice_of_args(*args):
#     sum=0
#     for x in args:
#         sum+=x
#     print(f"Hello my lucky number is{sum}")

def practice_of_kwargs(**kwargs):
    if 'name' in kwargs.keys():
        print(f"Hello my name is{kwargs['name']}")
    elif 'school' in kwargs.keys():
        print(f"Hello my name is {kwargs['name']} and my school is {kwargs['school']}")
    else:
        print('Hello Anonymous?')

def practice_of_kwargsargs():
    
    
