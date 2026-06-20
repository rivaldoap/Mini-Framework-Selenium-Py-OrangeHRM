import pytest
# Import fungsi start_browser dari file driver_factory Anda
# Sesuaikan jalurnya jika driver_factory ada di dalam folder Utils (misal: from Utils.driver_factory import ...)
from Utils.driver_factory import start_browser

@pytest.fixture(scope="function")
def driver():
    """Fixture Pytest yang menggunakan driver_factory kustom Anda"""
    print("\n[Setup] Menyalakan browser melalui Driver Factory...")
    
    # Memanggil fungsi milik Anda
    _driver = start_browser()
    
    # Berikan driver yang sudah aktif ke file TestCase
    yield _driver
    
    # Teardown: Otomatis menutup browser setelah test selesai
    print("\n[Teardown] Menutup browser...")
    _driver.quit()