import webbrowser

url = 'vineelvk2015.simplesite.com'

# Open URL in new browser window
#webbrowser.open_new(url) # opens in default browser

# Opens in firefox browser
webbrowser.get('firefox').open_new(url)

# Open URL in a new tab
#webbrowser.get('default').open_new_tab(url) # opens in default browser

# Opens in safari browser
#webbrowser.get('firefox').open_new_tab(url)
