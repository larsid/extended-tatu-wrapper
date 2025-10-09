package extended.tatu.wrapper.model;

import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.Optional;

/**
 *
 * @author Uellington Damasceno
 */
public class Device {

    protected final String id;
    protected final double latitude;
    protected final double longitude;
    private int hashcode;
    protected List<Sensor> sensors;
    
    public Device(String id, double latitude, double longitude, List<Sensor> sensors) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = latitude;
        this.sensors = sensors;
        this.hashcode = -1;
    }

    public String getId() {
        return this.id;
    }

    public double getLatitude() {
        return this.latitude;
    }

    public double getLongitude() {
        return this.longitude;
    }

    public List<Sensor> getSensors() {
        return Collections.unmodifiableList(sensors);
    }
    
    public Optional<Sensor> getSensorBySensorId(String sensorId) {
        return this.sensors.stream()
                .filter(sensor -> sensor.getId().equals(sensorId))
                .findAny();
    }

    @Override
    public int hashCode() {
        if (this.hashcode == -1) {
            hashcode = 97 * hashcode + Objects.hashCode(this.id);
            hashcode = 97 * hashcode + (int) (Double.doubleToLongBits(this.latitude) ^ (Double.doubleToLongBits(this.latitude) >>> 32));
            hashcode = 97 * hashcode + (int) (Double.doubleToLongBits(this.longitude) ^ (Double.doubleToLongBits(this.longitude) >>> 32));
        }
        return this.hashcode;
    }

    @Override
    public boolean equals(Object object) {
        return (object instanceof Device) && ((Device) object).hashCode() == this.hashCode();
    }

}
