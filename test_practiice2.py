from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestHotelPlanisphere:
    """HOTEL PLANISPHERE のE2Eテスト"""

    def setup_method(self):
        options = Options()

        # CircleCIなど画面のない環境で実行するための設定
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

        # 実行環境に合うChromeDriverを自動取得する
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()

    def test_open_top_page(self):
        """トップページが表示できることを確認する"""
        self.driver.get("https://hotel-example-site.takeyaqa.dev/ja/")

        assert "HOTEL PLANISPHERE" in self.driver.title

        heading = self.driver.find_element(By.TAG_NAME, "h1")
        assert "HOTEL PLANISPHERE" in heading.text
