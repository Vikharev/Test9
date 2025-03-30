import allure
from allure_commons.types import Severity
from selene import browser, have, by
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Somebody")
@allure.feature("QA-2025 Поргужение в Allure")
@allure.story("GURU-10 Отображение даты релиза")
@allure.link("https://github.com", name="Testing")
@allure.title('Проверка даты релиза (шаги через with)')
def test_check_release_date():
    with allure.step('Открытие браузера'):
        browser.open("https://github.com")

    with allure.step('Переход в полноэкранный режим'):
        browser.driver.fullscreen_window()

    with allure.step('Открытие строки поиска'):
        s('.search-input').click()

    with allure.step('Ввод "eroshenkoam/allure-example" в поисковую строку'):
        s('#query-builder-test').send_keys("eroshenkoam/allure-example").press_enter()

    with allure.step('Переход в репозиторий "eroshenkoam/allure-example"'):
        s(by.link_text("eroshenkoam/allure-example")).click()

    with allure.step('Проверка даты публикации релиза'):
        s('#repo-content-pjax-container').should(have.text('Oct 28, 2020'))


