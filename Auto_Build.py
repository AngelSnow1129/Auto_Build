# This workflow will install Python dependencies, run tests and lint with a single version of Python
# For more information see: https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python

name: Auto Build
on:
  push:
  schedule:
    #  8 个小时
    - cron: "* */8 * * *"

permissions:
  contents: read

jobs:
  bot:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3
    - name: Set up Python 3.10
      uses: actions/setup-python@v3
      with:
        python-version: "3.10"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install flake8 pytest
        if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
    - name: Lint with flake8
      run: |
        # stop the build if there are Python syntax errors or undefined names
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
    - name: Test with pytest
      run: |
        pytest
        
    - name: Auto Build
      env:
          sI: ${{secrets.sI }} 
          bI: ${{secrets.bI }} 
          bN: ${{secrets.bN}} 
          aT: ${{secrets.aT}} 
          text: file://text.txt

      run: 
          python Auto_Build.py
