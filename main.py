import time
from venv.user import login, password
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def get_data(url):
    programming_languages = {
        "Python": ".py",
        "Java": '.java',
        "JavaScript": '.js',
        "SQL": ".sql",
    }

    s = Service(r"chromedriver\chromedriver.exe")
    driver = webdriver.Chrome(service=s)
    driver.maximize_window()
    try:
        driver.get(url=url)

        input_email = driver.find_element(By.ID, "user_email")
        input_email.send_keys(login)

        input_password = driver.find_element(By.ID, "user_password")
        input_password.send_keys(password)

        # Жмякаем на кнопку Войти
        sign_in = driver.find_elements(By.TAG_NAME, "button")
        sign_in[1].click()

        # Переходим на страничку с решениями заданий
        driver.get(url="https://www.codewars.com/users/ilya_09/completed_solutions")

        # Скролим страницу до самого низа
        while driver.find_element(By.TAG_NAME, 'div'):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            divs = driver.find_element(By.TAG_NAME, 'div').text
            if 'Loading more items...' not in divs:
                print("Докрутка страницы закончена")
                break
            else:
                continue

        # Собираем все блоки
        all_info = driver.find_elements(By.CLASS_NAME, "list-item-solutions")

        # Проходим по каждому блоку
        for block in all_info:
            try:
                kyu, name = block.find_element(By.CLASS_NAME, "item-title").text.split("\n")
                symbols = '\\/:*?".<>|'
                for symbol in symbols:
                    if symbol in name:
                        name = name.replace(symbol, "")

            except Exception as _e:
                print("Не найдена kyu или Название задания")
                continue

            languages = block.find_elements(By.TAG_NAME, "h6")
            codes = block.find_elements(By.CLASS_NAME, "mb-5px")

            # Начинаем добавлять все наши данные

            if not os.path.exists(kyu):
                os.mkdir(kyu)

            if not os.path.exists(kyu + "\\" + name):
                os.mkdir(kyu + "\\" + name)

            for n in range(len(languages)):
                language = languages[n].text[:-1]
                if not os.path.exists(kyu + "\\" + name + "\\" + language):
                    os.mkdir(kyu + "\\" + name + "\\" + language)

                code = codes[n].text

                with open(fr"{kyu}\{name}\{language}\{name}{programming_languages[language]}", "w",
                          encoding='utf-8') as file:
                    file.write(code)

    except Exception as _ex:
        print(_ex)
    finally:
        driver.close()
        driver.quit()


def main():
    get_data("https://www.codewars.com/users/sign_in")


if __name__ == "__main__":
    main()
