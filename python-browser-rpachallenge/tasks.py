from robocorp import browser, excel, http
from robocorp.tasks import task


@task
def solve_challenge():
    """Solve the RPA challenge"""
    browser.configure(
        browser_engine="chromium",
        screenshot="only-on-failure",
        headless=False,
    )

    http.download("https://rpachallenge.com/assets/downloadFiles/challenge.xlsx")

    page = browser.goto("https://rpachallenge.com/")
    page.click("button:text('Start')")
    fill_the_forms()
    collect_the_results()

def fill_the_forms():
    worksheet = excel.open_workbook("challenge.xlsx").worksheet("Sheet1")
    for row in worksheet.as_table(header=True):
        fill_and_submit_form(row)

def collect_the_results():
    element = browser.page().locator("css=div.congratulations")
    browser.screenshot(element)


def fill_and_submit_form(row):
    page = browser.page()
    page.fill("//input[@ng-reflect-name='labelFirstName']", str(row["First Name"]))
    page.fill("//input[@ng-reflect-name='labelLastName']", str(row["Last Name"]))
    page.fill("//input[@ng-reflect-name='labelCompanyName']", str(row["Company Name"]))
    page.fill("//input[@ng-reflect-name='labelRole']", str(row["Role in Company"]))
    page.fill("//input[@ng-reflect-name='labelAddress']", str(row["Address"]))
    page.fill("//input[@ng-reflect-name='labelEmail']", str(row["Email"]))
    page.fill("//input[@ng-reflect-name='labelPhone']", str(row["Phone Number"]))
    page.click("input:text('Submit')")
