"""Constants for the systemair integration."""

from typing import Final
from enum import IntEnum, Enum


# DOMAIN = "systemair"
DEVICE_DEFAULT_NAME = "SystemAir"
SAVE_VTR = "save_vtr"

UPDATE_ON_READ = True
DEFAULT_TEMPERATURE = 20

class REG_TYPE(IntEnum):
    INPUT=1
    HOLDING=2

class FAN_MODES(IntEnum):
    OFF=1
    LOW=2   
    NORMAL=3
    HIGH=4


SA_OPERATION_MODE_AUTO = "auto"
SA_OPERATION_MODE_MANUAL = "manual"
SA_OPERATION_MODE_CROWDED = "crowded"
SA_OPERATION_MODE_REFRESH = "refresh"
SA_OPERATION_MODE_FIREPLACE = "fireplace"
SA_OPERATION_MODE_HOLIDAY = "holiday"
SA_OPERATION_MODE_IDLE = "idle"
SA_OPERATION_MODE_OFF = "off"

USER_MODES = {
    0: SA_OPERATION_MODE_AUTO,
    1: SA_OPERATION_MODE_MANUAL,
    2: SA_OPERATION_MODE_CROWDED,
    3: SA_OPERATION_MODE_REFRESH,
    4: SA_OPERATION_MODE_FIREPLACE,
    5: SA_OPERATION_MODE_IDLE,
    6: SA_OPERATION_MODE_HOLIDAY,
}
REVERSED_USER_MODES = {v: k for k, v in USER_MODES.items()}

ATTR_HUMIDITY: Final = "humidity"