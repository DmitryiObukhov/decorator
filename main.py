from funcs.admin import is_admin
from funcs.catch import catch_errors


@is_admin  # 1
def show_customer_receipt(user_type: str):
    print("function pass as it should be")


try:
    show_customer_receipt(user_type='user')
except ValueError as res:
    print(res)

show_customer_receipt(user_type='admin')


@catch_errors  # 2
def some_function_with_risky_operation(data):
    print(data['key'])


some_function_with_risky_operation({'foo': 'bar'})
some_function_with_risky_operation({'key': 'bar'})
