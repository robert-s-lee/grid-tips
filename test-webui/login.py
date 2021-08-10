from playwright.sync_api import sync_playwright
def run(playwright):
    browser = playwright.firefox.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://platform.grid.ai/
    page.goto("https://platform.grid.ai/")
    # Go to https://platform.grid.ai/#/
    page.goto("https://platform.grid.ai/#/")
    # Go to https://platform.grid.ai/#/landing
    page.goto("https://platform.grid.ai/#/landing")
    # Click img[alt="Google"]
    # with page.expect_navigation(url="https://accounts.google.com/o/oauth2/auth/identifier?after_auth_default_redirect=%2F&scope=profile%20email&redirect_uri=https%3A%2F%2Fplatform.grid.ai%2Foauth&client_id=438065754791-at0f2q42fr7dvnbggs2uj5l275enre7p.apps.googleusercontent.com&response_type=code&flowName=GeneralOAuthFlow"):
    with page.expect_navigation():
        page.click("img[alt=\"Google\"]")
    # assert page.url == "https://accounts.google.com/o/oauth2/auth?after_auth_default_redirect=%2F&scope=profile+email&redirect_uri=https%3A%2F%2Fplatform.grid.ai%2Foauth&client_id=438065754791-at0f2q42fr7dvnbggs2uj5l275enre7p.apps.googleusercontent.com&response_type=code"
    # Click [aria-label="Email or phone"]
    page.click("[aria-label=\"Email or phone\"]")
    # Fill [aria-label="Email or phone"]
    page.fill("[aria-label=\"Email or phone\"]", "sangkyulee@gmail.com")
    # Click button:has-text("Next")
    # with page.expect_navigation(url="https://accounts.google.com/signin/v2/challenge/pwd?after_auth_default_redirect=%2F&scope=profile%20email&redirect_uri=https%3A%2F%2Fplatform.grid.ai%2Foauth&client_id=438065754791-at0f2q42fr7dvnbggs2uj5l275enre7p.apps.googleusercontent.com&response_type=code&flowName=GeneralOAuthFlow&cid=1&navigationDirection=forward&TL=AM3QAYYfygCHv4k-6WHieGyWtrKg5mRX7giwapTh0EhJuENQIay3DUxcYYp8OU5k"):
    with page.expect_navigation():
        page.click("button:has-text(\"Next\")")
    # Click [aria-label="Enter your password"]
    page.click("[aria-label=\"Enter your password\"]")
    # Fill [aria-label="Enter your password"]
    page.fill("[aria-label=\"Enter your password\"]", "Spm3mw5cgSpm3mw5cr")
    # Click button:has-text("Next")
    page.click("button:has-text(\"Next\")")
    # assert page.url == "https://accounts.google.com/signin/v2/challenge/pwd?after_auth_default_redirect=%2F&scope=profile%20email&redirect_uri=https%3A%2F%2Fplatform.grid.ai%2Foauth&client_id=438065754791-at0f2q42fr7dvnbggs2uj5l275enre7p.apps.googleusercontent.com&response_type=code&flowName=GeneralOAuthFlow&cid=1&navigationDirection=forward&TL=AM3QAYYfygCHv4k-6WHieGyWtrKg5mRX7giwapTh0EhJuENQIay3DUxcYYp8OU5k"
    # Fill [aria-label="Enter your password"]
    page.fill("[aria-label=\"Enter your password\"]", "Spm3mw5cgSpm3mw5co")
    # Click button:has-text("Next")
    # with page.expect_navigation(url="https://platform.grid.ai/#/"):
    with page.expect_navigation():
        page.click("button:has-text(\"Next\")")
    # assert page.url == "https://accounts.google.com/signin/v2/challenge/pwd?after_auth_default_redirect=%2F&scope=profile%20email&redirect_uri=https%3A%2F%2Fplatform.grid.ai%2Foauth&client_id=438065754791-at0f2q42fr7dvnbggs2uj5l275enre7p.apps.googleusercontent.com&response_type=code&flowName=GeneralOAuthFlow&cid=1&navigationDirection=forward&TL=AM3QAYYfygCHv4k-6WHieGyWtrKg5mRX7giwapTh0EhJuENQIay3DUxcYYp8OU5k"
    # Go to https://platform.grid.ai/#/dashboard
    page.goto("https://platform.grid.ai/#/dashboard")
    # ---------------------
    context.storage_state(path="auth.json")
    context.close()
    browser.close()
with sync_playwright() as playwright:
    run(playwright)