# features/steps/savings_investments_steps.py
from behave import *
from pages.savings_investments_page import SavingsAndInvestmentsPage

@given("IC, Acceder a la página de Bancoppel")
def step_impl(context):
    context.driver.get("https://www.bancoppel.com/")
    context.page = SavingsAndInvestmentsPage(context.driver)  # Inicializa la página aquí
    context.page.check_and_reload(3)

@when("Navegar a la opción Inversión Creciente")
def step_impl(context):
    context.page.click_close_popup()
    context.page.click_ahorro()
    context.page.click_inversion_creciente()

@when('Seleccionar la opción Simulador e ingresar "{monto}", seleccionar Calcular')
def step_impl(context, monto):
    context.page.enter_monto(monto)
    context.page.click_calcular()

@then("muestra la cotización de la inversión")
def step_impl(context):
    print("Cotización:", context.page.get_result())