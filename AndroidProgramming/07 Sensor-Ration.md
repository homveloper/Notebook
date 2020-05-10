07 Sensor-Ration
===

# 코드

```Java
package com.example.sensor_rotation;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.view.Display;
import android.view.Surface;
import android.view.Window;
import android.view.WindowManager;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    SensorManager sensorManager;

    Sensor sensorAccelerometer;
    Sensor sensorMagnetometer;

    float[] accelerometerData = new float[3];
    float[] magnetometerData = new float[3];

    TextView textSensorAzimuth;
    TextView textSensorRoll;
    TextView textSensorPitch;

    Display display;

    //오차 보정
    static final float VALUE_DRIFT = 0.05f;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textSensorAzimuth = findViewById(R.id.value_azmiuth);
        textSensorPitch = findViewById(R.id.value_pitch);
        textSensorRoll = findViewById(R.id.value_roll);

        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);

        sensorAccelerometer = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        sensorMagnetometer = sensorManager.getDefaultSensor(Sensor.TYPE_MAGNETIC_FIELD);

        WindowManager wm = (WindowManager) getSystemService(WINDOW_SERVICE);
        display = wm.getDefaultDisplay();
    }

    @Override
    protected void onStart() {
        super.onStart();

        if (sensorAccelerometer != null)
            sensorManager.registerListener(this, sensorAccelerometer, sensorManager.SENSOR_DELAY_NORMAL);

        if (sensorMagnetometer != null)
            sensorManager.registerListener(this, sensorMagnetometer, sensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    protected void onStop() {
        super.onStop();
        sensorManager.unregisterListener(this);
    }

    @Override
    public void onSensorChanged(SensorEvent event) {
        int sensorType = event.sensor.getType();

        switch (sensorType) {
            case Sensor.TYPE_ACCELEROMETER:
                accelerometerData = event.values.clone();
                break;
            case Sensor.TYPE_MAGNETIC_FIELD:
                magnetometerData = event.values.clone();
                break;
            default:
                return;
        }

        float[] rotationMatrix = new float[9];
        boolean rotationOK = sensorManager.getRotationMatrix(rotationMatrix, null, accelerometerData, magnetometerData);

        float[] rotationMatrixAdjusted = new float[9];
        switch (display.getRotation()) {
            case Surface.ROTATION_0:
                rotationMatrixAdjusted = rotationMatrix.clone();
                break;
            case Surface.ROTATION_90:
                SensorManager.remapCoordinateSystem(rotationMatrix,SensorManager.AXIS_Y,SensorManager.AXIS_MINUS_X,rotationMatrixAdjusted);
                break;
            case Surface.ROTATION_180:
                SensorManager.remapCoordinateSystem(rotationMatrix,SensorManager.AXIS_MINUS_X,SensorManager.AXIS_MINUS_Y,rotationMatrixAdjusted);
                break;
            case Surface.ROTATION_270:
                SensorManager.remapCoordinateSystem(rotationMatrix,SensorManager.AXIS_MINUS_Y,SensorManager.AXIS_X,rotationMatrixAdjusted);
                break;
        }

        float orientationValues[] = new float[3];
        if(rotationOK){
            SensorManager.getOrientation(rotationMatrixAdjusted,orientationValues);
        }

        float azimuth = orientationValues[0];
        float pitch = orientationValues[1];
        float roll = orientationValues[2];

        // 약간의 오차 보정
        if(Math.abs(pitch) < VALUE_DRIFT)
            pitch = 0;
        if(Math.abs(roll) < VALUE_DRIFT)
            pitch = 0;

        textSensorAzimuth.setText(getResources().getString(R.string.value_azmiuth,azimuth));
        textSensorPitch.setText(getResources().getString(R.string.value_pitch,pitch));
        textSensorRoll.setText(getResources().getString(R.string.value_roll,roll));
    }

    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }
}

```