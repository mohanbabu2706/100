import inspect
#just in case you want to use the name of the decorator instead of difference calculator
#But in that case if the function decorated more than once the collected differende will be overwritten

import time
#Demo purpose only,the diffenrence will be generated from time

from functools import wraps


def collect_data_and_calculate_difference(data_collector,differnce_calculator):
    """Returns difference of data collected before and after the decorated function,
    plus the original return value of the decorated function. Return type:dict.
    Keys:
        -function name of the decorated function
        -name of the difference calculator function
    Valuels:
        -the original return value of decorated function
        -difference calculated by difference_calculator functions
    Parameters:function to collect data, and create difference from collected data

    Created:2017
    Author:George Fischhof
    """
    current_decorator_function_name = inspect.currentframe().f_code.co_name
    #just in case you want to use it

    def function_wrapper_because_of_parameters(decorated_function):
        difference_calculator_name = difference_calculator.__name__
        decorated_function_name = decorated_function.__name__

        i_am_the_first_decorator = not hasattr(decorated_function, '__wrapped__')

        @wraps(decorated_function)
        def wrapper(*args,**kwargs) -> dict:
            result_dict = dict()

            before = data_collector()
            original_result = decorated_function(*args,**kwargs)
            after = data_collector()

            my_collection = difference_calculator(before=before,after=after)

            i_am_not_first_decorator_but_first_is_similar_to_me = (
                not i_am_the_first_decorator
                and isinstance(original_result,dict)
                and (decorated_function_name in original_result)
            )

            if i_am_not_first_decorator_but_first_is_similar_to_me:
                original_result[difference_calculator_name] = my_collection
                return original_result
            else:
                result_dict[decorated_function_name] = original_result
                result_dict[difference_calculator_name] = my_collection
                return result_dict

        return wrapper
    return function_wrapper_because_of_parameters


#usage


def collect_data_of_data_series_a():
    time.sleep(0.5)
    return time.time()

def collect_data_or_data_series_b():
    time.sleep(0.5)
    return time.time()

def calculate_difference_on_data_series_b(before,after):
    return after - before

def calculate_difference_on_data_series_a(before,after):
    return after-before


@collect_data_and_calculate_difference(
    data_collector = collect_data_or_data_series_a,
    difference_calculator = calculate_difference_on_data_series_a)
@collect_data_and_calculate_difference(
    data_collector = collect_data_or_data_series_b,
    differnce_calculator = calculate_difference_on_data_series_b)
def do_something_that_changes_the_collected_data():
    return 'result of decorated function....'


print(do_something_that_changes_the_collected_data())
#result dict:
#{'calculate_difference_on_data_series_a':1.5010299682617188,
#'do_something_that_changes_the_collected_data':'result of decorated function....'.
#'calculate_difference_on_data_series_b':0,50016236045564}

        

    
