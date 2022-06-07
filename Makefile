# Install poetry
install_poetry:
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

# Run pytest
test:
	poetry run pytest tests

# Run main code
main:
	poetry run python src/main.py

# Install pyenv
install_pyenv:
	sudo apt -y update
	sudo apt -y upgrade
	sudo apt install \
  	build-essential libssl-dev zlib1g-dev \
  	libbz2-dev libreadline-dev libsqlite3-dev curl llvm \
  	libncursesw5-dev tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev \
  	libopencv-dev git
	git clone https://github.com/pyenv/pyenv.git ~/.pyenv
	echo 'eval "$$(pyenv init -)"' >> ~/.bashrc