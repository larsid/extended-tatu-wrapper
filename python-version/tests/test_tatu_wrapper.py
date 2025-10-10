import json

import pytest

from extended_tatu_wrapper import Device, Sensor
from extended_tatu_wrapper.enums import ExtendedTATUMethods
from extended_tatu_wrapper.models.tatu_message import TATUMessage
from extended_tatu_wrapper.utils import device_wrapper, extended_tatu_wrapper, sensor_wrapper, tatu_wrapper


def test_build_and_parse_flow_message():
    message = tatu_wrapper.build_tatu_flow_info_message("sensor-1", 5, 10)
    assert message.startswith("FLOW INFO sensor-1")
    timestamp = tatu_wrapper.get_message_timestamp(message)
    assert isinstance(timestamp, int) and timestamp > 0


def test_build_get_response():
    response = tatu_wrapper.build_get_message_response("device-1", "sensor-1", "42")
    parsed = json.loads(response)
    assert parsed["METHOD"] == "GET"
    assert parsed["BODY"]["sensor-1"] == "42"


def test_tatu_message_from_payload():
    response = tatu_wrapper.build_get_message_response("device-1", "sensor-1", "42")
    message = TATUMessage(response)
    assert message.method == ExtendedTATUMethods.GET
    assert message.is_response
    assert message.target == "sensor-1"


def test_device_and_sensor_serialisation():
    sensor = Sensor(id="temperature", type="float", collection_time=5, publishing_time=10)
    device = Device.from_iterable(id="device-1", latitude=1.0, longitude=2.0, sensors=[sensor])

    device_json = device_wrapper.to_json(device)
    recreated_device = device_wrapper.to_device(device_json)
    assert recreated_device.id == device.id
    assert recreated_device.get_sensor_by_id("temperature") is not None


def test_extended_wrapper_connect_message():
    sensor = Sensor(id="humidity", type="float", collection_time=5, publishing_time=10)
    device = Device.from_iterable(id="device-1", latitude=1.0, longitude=2.0, sensors=[sensor])
    message = extended_tatu_wrapper.build_connect_message(device, ip="127.0.0.1", timeout=30)
    assert message.startswith("CONNECT VALUE BROKER")
    payload = json.loads(message.split(" ", maxsplit=3)[3])
    assert payload["HEADER"]["SOURCE_IP"] == "127.0.0.1"
    assert payload["DEVICE"]["id"] == "device-1"


def test_invalid_sensor_delta_bounds():
    with pytest.raises(ValueError):
        Sensor(id="invalid", type="float", collection_time=1, publishing_time=1, min_value=10, max_value=0)
