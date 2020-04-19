import requests, json

# URL = "http://127.0.0.1:8000/emulator/"

# if argv[1] == 'GET':
#     r = requests.get(url=URL+sys.argv[2])
#     data = r.json();
#     print(data);

# elif sys.argv[1] == 'POST':
#     data = {'name':sys.argv[3],
#             'description':sys.argv[4]}
#     r = requests.post(url=URL+sys.argv[2], data=data)
#     print(r.text)

class HardwareLibrary:
    """
    Class initializer
    throws:
        ValueError: if the definition given is invalid
    """
    def __init__(self, definition: str, emulatorURL: str):
        # save emulator URL
        self.emulatorURL = emulatorURL

        # deal with device definition
        if not self.isValidDefinition(definition):
            raise ValueError
        else:
            #loading definition
            defn = json.loads(definition)

            #saving definition
            self.deviceName = defn["deviceName"]
            self.hardware = defn["hardware"]

            #initialize value and validity for caching
            for hrdw in self.hardware:
                if self.hardware[hrdw]["valueType"] == "integer":
                    self.hardware[hrdw]["value"] = -1
                elif self.hardware[hrdw]["valueType"] == "float":
                    self.hardware[hrdw]["value"] = -0.1
                else:
                    self.hardware[hrdw]["value"] = False
                
                self.hardware[hrdw]["valid"] = False
    
    """
    Repr method
    returns:
        the representation of the class in json format
    """
    def __repr__(self):
        return '{"deviceName":{},"hardware":{}'.format(self.deviceName, self.hardware)

    """
    Str method
    returns:
        a pretty printed string format of the class
    """
    def __str__(self):
        return 'DeviceName:\n\t{}\nHardware:\n\t{}'.format(self.deviceName, self.hardware)

    """
    isValidDefinition
    desc:
        checks to see if the following hardware definition is met,
        hardware definition should contain following and nothing else
    defn:
        deviceName: str
        hardware: dict
            <<hardwareName>>: dict
                hardwareType: str (actuator, sensor)
                pin: int
                valueType: str (integer, boolean, float)
    returns:
        True: if the definition is valid
        False: otherwise
    """
    @staticmethod
    def isValidDefinition(definition: str):
        defn = json.loads(definition)

        deviceKeys = ["deviceName", "hardware"]
        hardwareKeys = ["hardwareType", "pin", "valueType"]
        hardwareTypes = ["sensor", "actuator"]
        valueTypes = ["integer", "boolean", "float"]

        # checking keys in definition
        for key in defn.keys():
            if key not in deviceKeys:
                return False
                
        for key in deviceKeys:
            if key not in defn.keys():
                return False

        # checking keys in each hardware instance
        hardware = defn["hardware"]
        for hrdw in hardware.values():
            for key in hrdw.keys():
                if key not in hardwareKeys:
                    return False
            
            for key in hardwareKeys:
                if key not in hrdw.keys():
                    return False

            if (hrdw["hardwareType"] not in hardwareTypes
                or hrdw["valueType"] not in valueTypes):
                return False

        return True

    """
    Change Value Method
    desc:
        changes the value of an actuator hardware and invalidates the hardware
    throws:
        Exception if the value cannot be changed
    """
    def changeValue(self, hardware, value):
        pass

    """
    Check Value Method
    desc:
        checks the value of the hardware given
    returns:
        the value of the hardware provided
    throws:
        Error if the value is invalid
        ValueError if the hardware given does not exist
    """
    def checkValue(self, hardware):
        pass

    """
    Check Validity Method
    desc:
        checks the validity of the hardware value given
    returns:
        True if the value is valid
        False otherwise
    Throws
    """
    def checkValidity(self, hardware):
        pass

    """
    Send