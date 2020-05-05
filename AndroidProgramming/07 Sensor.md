07 Sensor
===

# 1. 센서의 유형과 종류

## 1.1 Motion Sensors

장치의 움직임을 측정한다. 안드로이드에서는 다양한 종류의 센서를 지원합니다.

- 가속도 센서
- 중력 센서
- 자이로 센서
- 회전 센서

## 1.2 Enviromental Sensors

## 1.3 Position Sensors

장치의 물리적인 위치를 측정한다.

- 자기 센서
- 근접 센서

## 1.4 센서의 타입

- 하드웨어 기반 센서 : 

    조도 센서, 근접 센서, 가속도 센서, 지자기 센서

- 소프트웨어 기반 센서 : 하드웨어 기반 센서로 측정된 값들을 응용한다.

    선형 가속도 센서, 회전 센서

## 1.5 센서의 유무

장치에 따라 센서의 유뮤는 다양합니다. 대부분의 장치에서는 가속도 센서와 지자기 센서를 내장하고 있습니다.

# 2. Emulating Sensors

Android Emulator에서는 가상 센서를 지원합니다. 가속도 센서와 다른 추가적인 센서들을 지원합니다.

# 3. 안드로이드 센서 프레임워크

## 3.1 SensorManager

다양한 센서들의 접근과 상태를 확인할 수 있는 클래스입니다. 센서들의 이벤트 리스너를 등록하거나 해제할 수 있습니다. 

## 3.2 Sensor

## 3.3 SensorEvent

## 3.4 SensorEventLinstner

센서에 새로운 데이터가 들어오거나 정확도가 바뀔때 이벤트 리스너가 발생합니다.

## 3.5 Sensor Class Types

- TYPE_ACCELEROMETER


## 3.6 Using Sensors

1. 장치에서 어떤 센서를 사용할지 결정합니다.
2. 개별적인 센서의 능력을 결정합니다. 예를들어 최대범위, 소모전력, 해상도가 있습니다.
3. 센서 이벤트 리스너를 등록합니다.
4. RAW 센서 데이터를 획득합니다.
5. 센서 이벤트 리스너를 해제합니다.

센서는 전력소모를 하므로 필요하지 않은 상황에서는 해제를 해야합니다.

# 4. 센서의 능력

```Java
mSensorManager = (SensorManager)getSystemService(Context.SENSOR_SERVICE);
List<Sensor> deviceSensors = mSensorManager.getSensorList(Sensor.TYPE_ALL);
```

지자기 센서의 사용

# 5. 센서의 설정

Google Play filter에서 사용할 센서를 설정할 수 있습니다.

# 6. 센서의 이벤트

센서 이벤트 리스너는 onCreate(), onResume(), or onPause()에서 등록하는 것이 아닌 onStart()나 OnStop()에서 등록을 권장하고 있습니다.

# 7. 코드

```Java
package com.example.mysensorlist;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.os.Bundle;
import android.widget.TextView;

import java.util.List;

public class MainActivity extends AppCompatActivity implements SensorEventListener {

    private SensorManager sensorManager;
    private Sensor mLight;

    @Override
    public final void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        sensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        mLight = sensorManager.getDefaultSensor(Sensor.TYPE_LIGHT);

        List<Sensor> sensorList = sensorManager.getSensorList(Sensor.TYPE_ALL);

        StringBuilder sensorsText = new StringBuilder();

        for(Sensor sensor : sensorList){
            sensorsText.append(sensor.getName()).append("\n");
        }

        TextView sensorTextView = findViewById(R.id.textView);
        sensorTextView.setText(sensorsText);
    }

    @Override
    public final void onAccuracyChanged(Sensor sensor, int accuracy) {
        // Do something here if sensor accuracy changes.
    }

    @Override
    public final void onSensorChanged(SensorEvent event) {
        // The light sensor returns a single value.
        // Many sensors return 3 values, one for each axis.
        float lux = event.values[0];
        // Do something with this sensor value.
    }

    @Override
    protected void onResume() {
        super.onResume();
        sensorManager.registerListener(this, mLight, SensorManager.SENSOR_DELAY_NORMAL);
    }

    @Override
    protected void onPause() {
        super.onPause();
        sensorManager.unregisterListener(this);
    }
}
```