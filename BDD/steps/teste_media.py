from behave import given, when, then

@given('eu tenho dois números flutuantes: 5 e 7 : {num1:f} e {num2:f}')
def step_impl(context, num1, num2):
    context.num1 = num1
    context.num2 = num2

@when('eu somo os dois números flutuantes e divido por dois')
def step_impl(context):
    context.resultado = (context.num1 + context.num2)/2

@then('o resultado deve ser {resultado:f}')
def step_impl(context, resultado):
    assert context.resultado == resultado, f"Resultado incorreto. Esperado: {resultado}. Obtido: {context.resultado}"