









import sys
sys.path.append('.')

import bin.normalize as nm

def test_python_version():
	response = nm.python_version()
	assert response == "3.12.3"

def test_os():
	response = nm.os_system()
	assert response == "Linux"
