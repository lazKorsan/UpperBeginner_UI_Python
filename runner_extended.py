import subprocess
import os
import sys

# Rapor klasörü kontrolü
if not os.path.exists("reports"):
    os.makedirs("reports")

def run_behave_comprehensive(tag_name="@coursesSteps"):
    print(f"--- {tag_name} Testleri Başlatılıyor (Rapor + Canlı Log) ---")

    # Komut Analizi:
    # --no-capture: Print çıktılarını terminalde gösterir.
    # --no-capture-stderr: Hata çıktılarını yakalamaz, terminale basar.
    # --format behave_html_formatter:HTMLFormatter: HTML raporu oluşturur.
    # --format allure_behave.formatter:AllureFormatter: Allure sonuçlarını oluşturur.
    # --format pretty: Terminalde renkli çıktı verir.
    command = (
        f"behave --tags={tag_name} --no-capture --no-capture-stderr "
        "--format behave_html_formatter:HTMLFormatter --outfile reports/behave_report.html "
        "--format allure_behave.formatter:AllureFormatter --outfile reports/allure_results "
        "--format pretty"
    )

    try:
        subprocess.run(command, shell=True, check=True)
        print("\n[BAŞARILI] Testler bitti ve raporlar 'reports/' klasöründe güncellendi.")
    except subprocess.CalledProcessError:
        print("\n[HATA] Testler sırasında bir sorun oluştu veya testler başarısız oldu.")
        sys.exit(1)

if __name__ == "__main__":
    # Projenizdeki geçerli tag ile çalıştırılıyor
    run_behave_comprehensive("@coursesSteps")
