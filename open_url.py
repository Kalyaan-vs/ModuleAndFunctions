# import webbrowser
#
# chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe" %s'
# chrome = webbrowser.get(chrome_path)
# chrome.open("https://learnprogramming.academy/courses")

if __name__ == "__main__":
    import webbrowser

    # webbrowser.open("https://docs.python.org/3.10/library/webbrowser")

    # chrome = webbrowser.get(using="google-chrome")
    chrome = webbrowser.get(r"'C:\Program Files\Google\Chrome\Application\chrome.exe' %s")
    chrome.open("https://learnprogramming.academy/courses")