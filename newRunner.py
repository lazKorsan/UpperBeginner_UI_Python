import subprocess
import sys


def run_behave_tests():
    command = "behave --tags=@coursesSteps"
    print(">>> @coursesSteps etiketli testler baslatiliyor")

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print("❌ Testler calisirken hata olustu")
        sys.exit(1)


if __name__ == "__main__":
    run_behave_tests()
