from HardwareLibrary import HardwareDefinition as HD

"""
Tests for HardwareDefinition Class
    - pass valid device
    - fail invalid main key
    - fail invalid hardware key
    - fail invalid hardwareType
    - fail invalid valueType
"""
# valid device
validDefn = '''{    "deviceName": "validDevice",
                    "hardware": {
                        "validHardware1": {
                            "hardwareType": "actuator",
                            "pin": 1,
                            "valueType": "integer"
                        },
                        "validHardware2": {
                            "hardwareType": "sensor",
                            "pin": 2,
                            "valueType": "float"
                        }
                    }
                }'''
# testing invalid main key
invalidDefn1 =  '''{    "deviceName": "validDevice",
                        "badkey": "bad",
                        "hardware": {
                            "validHardware1": {
                                "hardwareType": "actuator",
                                "pin": 1,
                                "valueType": "integer"
                            },
                            "validHardware2": {
                            "hardwareType": "sensor",
                            "pin": 2,
                            "valueType": "float"
                            }
                        }
                    }'''
# testing invalid hardware key
invalidDefn2 =  '''{    "deviceName": "validDevice",
                        "hardware": {
                            "validHardware1": {
                                "hardwareType": "actuator",
                                "pin": 1,
                                "valueType": "integer"
                            },
                            "invalidHardware2": {
                            "hardwareType": "sensor",
                            "badkey": "bad",
                            "pin": 2,
                            "valueType": "float"
                            }
                        }
                    }'''
# testing invalid hardwareType
invalidDefn3 =  '''{    "deviceName": "validDevice",
                        "hardware": {
                            "validHardware1": {
                                "hardwareType": "actuator",
                                "pin": 1,
                                "valueType": "integer"
                            },
                            "validHardware2": {
                            "hardwareType": "bad",
                            "pin": 2,
                            "valueType": "float"
                            }
                        }
                    }'''
# testing invalid valueType
invalidDefn4 =  '''{    "name": "validDevice",
                        "hardware": {
                            "validHardware1": {
                                "hardwareType": "actuator",
                                "pin": 1,
                                "valueType": "integer"
                            },
                            "validHardware2": {
                            "hardwareType": "sensor",
                            "pin": 2,
                            "valueType": "bad"
                            }
                        }
                    }'''

# Tests
print("Testing HardwareDefinition Class:")

print("\tisValidDefinition: ", end = '')
assert HD.isValidDefinition(validDefn) == True, "validDefn"
assert HD.isValidDefinition(invalidDefn1) == False, "invalidDefn1"
assert HD.isValidDefinition(invalidDefn2) == False, "invalidDefn2"
assert HD.isValidDefinition(invalidDefn3) == False, "invalidDefn3"
assert HD.isValidDefinition(invalidDefn4) == False, "invalidDefn4"
print("pass")

print("\t__init__: ")
validDefinition = HD(validDefn)

try:
    invalidDefinition = HD(invalidDefn1)
except:
    print("\t\tpassed invalid1")
    pass

try:
    invalidDefinition = HD(invalidDefn2)
except:
    print("\t\tpassed invalid2")
    pass

try:
    invalidDefinition = HD(invalidDefn3)
except:
    print("\t\tpassed invalid3")
    pass

try:
    invalidDefinition = HD(invalidDefn4)
except:
    print("\t\tpassed invalid4")
    pass

print("\t\tpassed all")