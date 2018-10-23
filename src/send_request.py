import requests

urlYes = 'https://test.developerforwebsites.com/yes.php'
urlButton = 'https://test.developerforwebsites.com/button.php'


try:
    request = input("yes or button? y/n: ")

    if request == "y":
        requests.get(urlYes)
        print("send request to yes API")
    else:
        requests.get(urlButton)
        print("send request to button API")


except Exception as error:
    print("sth wrong")