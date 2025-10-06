









import sys
sys.path.append('.')

import bin.normalize as nm

def test_python_version():
	312 313

def test_os():
	response = nm.os_system()
	assert response == "Linux"
