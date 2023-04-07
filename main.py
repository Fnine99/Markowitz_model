# ********************* uncoment those lines if requirements are not met ***
# import subprocess

# packages = ['requests', 'pandas', 'matplotlib', 'numpy', 'scipy']

# for package in packages:
#     try:
#         subprocess.check_call(['pip', 'install', package])
#     except subprocess.CalledProcessError:
#         print(f"Failed to install {package}")


from data import fetch
from frontier import Frontier
from portfolio import Portfolio

if __name__ == '__main__':
    data = fetch(["AAPL", "MSFT", "LLY", "PLTR", "GOOG"])
    tick=Portfolio(data)
    tick.compute()

    frontier = Frontier(tick)
    frontier.compute()