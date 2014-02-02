Install the environment
---

    apt-get install python-virtualenv
    virtualenv virtualenv
    source virtualenv/bin/activate
    pip install pyserial

Using the library
---

    cd scpi
    python
    >>> import scpi.devices
    >>> p = scpi.devices.Auto_SCPI('/dev/ttyUSB0')
    >>> print p # return valid device type
    >>> p.oU = 5     # set 5V output
    >>> p.oI = 0.5   # set 0.5A output
    >>> o.oO = True  # enable output
