#everything found on https://playwright.dev/python/docs
from playwright.sync_api import sync_playwright, Playwright


def main():
#   placeholder
    action = ""
#   launch an empty browser (headless allows the browser to be seen)
    browsers = sync_playwright().start().chromium.launch(headless=False)
#   Open a page on chromium
    page = browsers.new_page()

#   Navigate to coolmathgames
    page.goto('https://www.coolmathgames.com/login')
#   fill username/password ---- had to find the input name via inspect/f12 for each textbox
    page.fill('input#edit-name', 'testing898')
    page.fill('input#edit-pass', '?!!U?)9v$cQ2vJ-') #randomly generated password, I just made this account
#   click the submit button ---- usually button[type=submit]
    page.click('input[type=submit]')



    while action != "quit":

#       navigate to 'run' game
        def run(action):

            print("Showcases the ability for playwright to click through a webpage to navigate.")

#           navigate to a base page
            page.goto('https://www.coolmathgames.com/login')
#           find text, click on text
            page.get_by_text('All Games').click()
#           click on something labeled with a[...]
            page.click('a[href="/1-complete-game-list/n-r"]')
            page.click('a[href="/0-run"]')
#           pass is required as the browser would assume the job is done and stop the program
            pass

#       navigate to the world's hardest game
        def whg(action):

            print("A simple navigation option - compared to navigating to 'run'")
            page.goto('https://www.coolmathgames.com/0-worlds-hardest-game')
            pass

#       navigate to all games location
        def all_games(action):

            print("If you want to go to all games")
            page.goto('https://www.coolmathgames.com/1-complete-game-list')
            pass

#       test for ability to use controls in games
        def run_start(action):

            for i in range(0,50):
#               press space on page
                page.keyboard.press('Space')
#               pause
                page.wait_for_timeout(1000)
            pass

#       navigate to home page
        def home_run(action):

            page.goto('https://www.coolmathgames.com/')
            pass

#       print help function
        def print_help(action):

            print("\t'whg': Open 'World's Hardest Game'")
            print("\t'home': Open home page")
            print("\t'start': Run this when you are in a game and want to continuously jump 100 times.")
            print("\t'all':")
            print("\t'run': Navigate to the widely famous game called 'run'")
            print("\t'quit': quit program")
            pass

#       run each action
        def action_run(action):
            if action == "help":
                print_help(action)
            if action == "run":
                run(action)
            if action =="home":
                home_run(action)
            if action == "start":
                run_start(action)
            if action == "whg":
                whg(action)
            if action == "all":
                all_games(action)

#       ask for input to determine the action requested
        action = input("What action would you like to take? ('help' for options): \u001b[1m").strip().lower()
        print("\u001b[0m")
        action_run(action)










main()
