from selene import browser, have, command

browser.config.browser_name = "firefox"
browser.config.hold_browser_open = True
browser.open("https://demoqa.com/automation-practice-form")
browser.element("#firstName").type("Nikita")
browser.element("#lastName").type("Zhuravlev")
browser.element("#userEmail").type("nikitazhuravlevqa@gmail.com")
browser.element(".custom-control-label").click()
browser.element("#userNumber").type("0123456789")
browser.element("#dateOfBirthInput").perform(command.js.scroll_into_view).click()
browser.element(".react-datepicker__month-select").type("April")
browser.element(".react-datepicker__year-select").type("1997")
browser.element(".react-datepicker__day--002").click()
# browser.element("#subjectsContainer").type("English")
# # browser.all("custom-control-input").element_by(have.text("Sports")).click()
# browser.element("#CurrentAddress").perform(command.js.scroll_into_view).type("Polotsk")