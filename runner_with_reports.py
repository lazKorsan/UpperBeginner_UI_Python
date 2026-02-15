import subprocess
import os
import sys

# Rapor klasörü kontrolü
if not os.path.exists("reports"):
    os.makedirs("reports")

def run_smoke_with_reporting(tag_name="@coursesSteps"):
    print(f"--- {tag_name} Tag'li Testler Raporlu Olarak Başlatılıyor ---")

    # Komut oluşturma
    # --format behave_html_formatter:HTMLFormatter: HTML raporu oluşturur.
    # --format allure_behave.formatter:AllureFormatter: Allure sonuçlarını oluşturur.
    # --outfile: Çıktı dosyalarının yerini belirtir.
    command = (
        f"behave --tags={tag_name} "
        "--format behave_html_formatter:HTMLFormatter --outfile reports/behave_report.html "
        "--format allure_behave.formatter:AllureFormatter --outfile reports/allure_results"
    )

    try:
        # Komutu çalıştır
        subprocess.run(command, shell=True, check=True)
        print("\n[BAŞARILI] Raporlar 'reports/' klasöründe oluşturuldu.")
    except subprocess.CalledProcessError as e:
        print(f"\n[HATA] Testler başarısız oldu veya yapılandırma hatası var: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Projenizdeki geçerli tag ile çalıştırılıyor
    run_smoke_with_reporting("@coursesSteps")
