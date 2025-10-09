









import sys
sys.path.append('.')

import bin.normalize as nm

def test_python_version():
    assert sys.version_info.major == 3
    assert sys.version_info.minor in [12, 13]

def test_os():
	response = nm.os_system()
	assert response == "Linux"
