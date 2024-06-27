import webbrowser

brave_path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
brave_browser = webbrowser.get('brave')