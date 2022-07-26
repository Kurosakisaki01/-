from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def is_login(email: str, password: str):
    # * ユーザーネームとパスワードを入力
    driver.find_element_by_name("email").send_keys(email)
    sleep(1)
    driver.find_element_by_name("password").send_keys(password + "\n")
    sleep(5)

    # * 人気の投稿を非表示
    driver.find_element_by_class_name("Box__nav__a.Box__nav__item--link").click()
    sleep(5)
    driver.find_element_by_class_name("Switch__wrapper").click()
    sleep(5)
    driver.get(yay_timeline)
    sleep(5)


def like_loop():
    # like counter
    liked_count = 0

    # ? auto like start
    while True:
        try:
            # * いいねpathの取得
            like_elements = driver.find_elements_by_class_name("Heart__path")
            for like_element in like_elements:
                if like_element.get_dom_attribute("class") == "Heart__path":
                    # * いいねしていない投稿の判定
                    if like_element.is_enabled:
                        like_element.click()
                        liked_count += 1
                        print(f"\r合計いいね数: {liked_count}", end="")
                        sleep(2.5)

                    else:  # ! いいね済みの投稿になったら再取得
                        print("break")
                        break

        except Exception as e:
            print(e, "error")

        finally:
            driver.get(yay_timeline)
            sleep(20)
            driver.execute_script("window.scrollTo(0, 0);")
            sleep(20)


if __name__ == "__main__":
    # * user_info
    email = str(input("email: "))
    password = str(input("password: "))

    # * URL
    yay_login = "https://yay.space/login"
    yay_timeline = "https://yay.space/timeline"

    # * ChromeDriverのオプション

    # * enable-automation：ブラウザ起動時のテスト実行警告を非表示
    # * enable-logging：DevToolsのログを出力しない

    options = webdriver.ChromeOptions()

    # *ヘッドレスモードで起動(ヘッドレスの場合は21行目の＃を削除)
    # chrome_options.add_argument('--headless')

    # *enable-automation：ブラウザ起動時のテスト実行警告を非表示
    # *enable-logging：DevToolsのログを出力しない
    options.add_experimental_option(
        "excludeSwitches", ["enable-automation", "enable-logging"]
    )

    # ?webdriver
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.set_window_size(600, 1000)

    # * login start
    driver.get(yay_login)
    driver.implicitly_wait(60)
    is_login(email=email, password=password)
    # ?loop start
    like_loop()