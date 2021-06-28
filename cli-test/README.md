
https://blog.esciencecenter.nl/testing-shell-commands-from-python-2a2ec87ebf71

# bats-core
https://github.com/bats-core/bats-core

```
brew install bats-core
brew install parallel
```

# pytest

https://docs.pytest.org/en/6.2.x/

https://docs.pytest.org/en/latest/reference/plugin_list.html#plugin-list

```
conda create --name clitest python=3.7
conda activate clitest
pip install pytest
pip install pytest-shell
```

# robot

brew install geckodriver 
conda create --name robot python=3.7
conda activate robot
git clone https://github.com/robotframework/WebDemo
cd WebDemo
pip install -r requirements.txt

python demoapp/server.py

robot login_tests/valid_login.robot

