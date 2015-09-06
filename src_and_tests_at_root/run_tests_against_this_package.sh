src_path='./src'
export PYTHONPATH="${src_path}:${PYTHONPATH}"
python -m unittest discover -p '*.py' test
