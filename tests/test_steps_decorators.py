import allure
from allure_commons.types import Severity
from selene import browser, have, by
from selene.support.shared.jquery_style import s


@allure.step('Открытие браузера')
def open_browser():
    browser.open("https://github.com")


@allure.step('Переход в полноэкранный режим')
def set_fullscreen_window():
    browser.driver.fullscreen_window()


@allure.step('Открытие строки поиска')
def click_search_input():
    s('.search-input').click()


@allure.step('Ввод "eroshenkoam/allure-example" в поисковую строку')
def do_search():
    s('#query-builder-test').send_keys("eroshenkoam/allure-example").press_enter()


@allure.step('Переход в репозиторий "eroshenkoam/allure-example"')
def go_to_repo():
    s(by.link_text("eroshenkoam/allure-example")).click()


@allure.step('Проверка даты публикации релиза')
def check_release_date():
    s('#repo-content-pjax-container').should(have.text('Oct 28, 2020'))


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.label("owner", "Somebody")
@allure.feature("QA-2025 Поргужение в Allure")
@allure.story("GURU-10 Отображение даты релиза")
@allure.link("https://github.com", name="Testing")
@allure.title('Проверка даты релиза (шаги в декораторах)')
def test_check_release_date():
    open_browser()
    set_fullscreen_window()
    click_search_input()
    do_search()
    go_to_repo()
    check_release_date()
