import allure
from allure_commons.types import Severity
from selene import browser, have, by
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Somebody")
@allure.feature("QA-2025 Поргужение в Allure")
@allure.story("GURU-10 Отображение даты релиза")
@allure.link("https://github.com", name="Testing")
@allure.title('Проверка даты релиза (только selene)')
def test_github():
    browser.open("https://github.com")
    browser.driver.fullscreen_window()
    s('.search-input').click()
    s('#query-builder-test').send_keys("eroshenkoam/allure-example").press_enter()

    s(by.link_text("eroshenkoam/allure-example")).click()

    s('#repo-content-pjax-container').should(have.text('Oct 28, 2020'))
