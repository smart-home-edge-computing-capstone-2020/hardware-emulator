import requests, json, copy

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

                self.createHardware(hrdw)


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
    Create Hardware Function (DO NOT USE)
    desc:
        creates the hardware on the web app
    """
    def createHardware(self, hardware):
        serial = copy.deepcopy(self.hardware[hardware])
        serial["hardwareType"] = serial["hardwareType"][0]
        serial["valueType"] = serial["valueType"][0]
        serial["deviceName"] = self.deviceName
        serial["hardwareName"] = hardware
        serial["valueInteger"] = -1
        serial["valueBoolean"] = False
        serial["valueFloat"] = -0.1
        serial.pop("value")

        r = requests.post(  url=self.emulatorURL+"create/",
                            headers = {'Content-Type': 'application/json'},
                            data=json.dumps(serial))


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
        ValueError if hardware isn't valid or value cannot be changed
    """
    def changeValue(self, hardware, value):
        if (hardware not in self.hardware.keys()
            or "actuator" not in self.hardware[hardware]["hardwareType"]):
            raise ValueError
        
        if type(value) == type(self.hardware[hardware]["value"]):
            self.hardware[hardware]["value"] = value
            self.sendValue(hardware, value)
        else:
            raise ValueError

    """
    Send Value Method
    desc:
        a helper function for sending a value to the web app
    """
    def sendValue(self, hardwareName, value):
        data = {"value": value}

        r = requests.post(  url=self.emulatorURL+"value/"+self.deviceName+"/"+hardwareName,
                            headers = {'Content-Type': 'application/json'},
                            json = data)


    """
    Poll Value Method
    desc:
        polls the value of the hardware through the hardware
    returns:
        the value of the hardware given
    throws:
        ValueError if the hardware given does not exist
    """
    def pollValue(self, hardwareName):
        if hardwareName not in self.hardware.keys():
            raise ValueError

        r = requests.get(url=self.emulatorURL+"value/"+self.deviceName+"/"+hardwareName)

        return r.json()["value"]

        #To be continued
