Run test script: pytest -v test_simple.py
    - v => verbose

Run specifc test group: pytest -v test_grouping.py -m <test group name>
Run specifc test group (logic): pytest -v test_grouping.py -m 'not <test group name>'

Run specifc test: pytest -v test_simple.py -k test_true