09 Preference

===

안드로이드에서 특정한 설정 값들을 저장할 수 있는 방법이다.
안드로이드에서 데이터를 저장할 수 있는 클래스들을 제공하고 있다.

- Shared Preferences : private primitive data in key-value pairs
- Internal Storage : priate data in device memory
- External Storage : public data on device or external storage
- SQLite Databases : structured data in a private database
- Content Providers : store privately and make available publicly

# 1. Shared Preference

I/O를 위한 데이터를 key-value 쌍으로 장치 저장소에 파일로 저장합니다. SharedPreference 클래스는 I/O 와 그 데이터를 관리하기 위한 API를 제공하고 있습니다.

데이터의 저장은 onPause()에서 불러오기는 onCreate()에서 수행하면 됩니다.

## 1.1 SharedPreference 와 SavedInstanceState

SavedInstanceState 또한 데이터를 저장하는 기능을 공통적으로 제공하지만, 둘과의 차이점이 있습니다.

|SharedPreference|SavedInstanceState|
|:---|:---| 
|- 비록 앱이 종료, 재실행 또는 장치가 재부팅 되어도 사용자와 데이터간의 연결을 유지합니다.|- 동일한 사용자 연결에 있는 activity instance 사이에 데이터 상태를 보존합니다.|
|- 사용자 정의 설정이나 게임의 점수 기록과 같은 데이터는 기록됩니다.|- 현재 activity와 선택된 tab과 같은 사용자와 앱간의 연결은 기록되지 않습니다.|
|-사용자의 설정들을 저장할때 사용합니다.|- 장치가 회전한 이후 상태를 재설정할때 사용합니다.|

## 1.2 SharedPreference 생성

앱마다 SharedPreferce는 하나만 사용됩니다.

```Java
@Override
protected void onPause() {
   super.onPause();
   SharedPreferences.Editor preferencesEditor =     
       mPreferences.edit();

   preferencesEditor.putInt("count", mCount);
   preferencesEditor.putInt("color", mCurrentColor);
   preferencesEditor.apply();
}
```

## 1.3 데이터 가져오기

```Java
// do code in onCreate()

mPreferences = getSharedPreferences(sharedPrefFile, MODE_PRIVATE);
if (savedInstanceState != null) {
    mCount = mPreferences.getInt("count", 1);
    mShowCount.setText(String.format("%s", mCount));

    mCurrentColor = mPreferences.getInt("color", mCurrentColor);
    mShowCount.setBackgroundColor(mCurrentColor);

    mNewText = mPreferences.getString("text", "");
} else { … }
```

## 1.4 데이터 제거하기

```Java
SharedPreferences.Editor preferencesEditor = mPreferences.edit();
preferencesEditor.clear();
preferencesEditor.apply();
```

## 1.5 데이터의 변화 감지

1. Implement interface SharedPreference OnSharedPreferenceChangeListener 
2. Register listener with   registerOnSharedPreferenceChangeListener()
3. Register and unregister listener in onResume() and onPause() 
4. Implement on onSharedPreferenceChanged() callback

```Java
public class SettingsActivity extends AppCompatActivity
    implements OnSharedPreferenceChangeListener { ...
    
    public void onSharedPreferenceChanged(
        SharedPreferences sharedPreferences, String key) {
        if (key.equals(MY_KEY)) {
            // Do something
        }
    }
}
```

## 1.6 전체 코드

```Java
public class MainActivity extends AppCompatActivity {

    TextView txtCount;
    int count = 0;
    int color;

    final String COUNT_KEY = "count";
    final String COLOR_KEY = "color";

    SharedPreferences preferences;
    String sharedPrefile = "com.example.SharedPreference";


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtCount = findViewById(R.id.txt_count);

        // default background color
        color = Color.TRANSPARENT;

        preferences = getSharedPreferences(sharedPrefile, MODE_PRIVATE);

        count = preferences.getInt(COUNT_KEY, 0);
        txtCount.setText(String.format("%s",count));
        color = preferences.getInt(COLOR_KEY, color);
        txtCount.setBackgroundColor(color);
    }

    public void changeBackgroundColor(View view){
        int color = ((ColorDrawable)view.getBackground()).getColor();
        txtCount.setBackgroundColor(color);
        this.color = color;
    }

    public void countUp(View view){
        count++;
        txtCount.setText(String.format("%s",count));
    }

    public void reset(View view){

        //reset count
        count = 0;
        txtCount.setText(String.format("%s",count));

        //reset color
        color = Color.TRANSPARENT;
        txtCount.setBackgroundColor(color);

        // clear preference
        SharedPreferences.Editor preferencesEditor =  preferences.edit();
        preferencesEditor.clear();
        preferencesEditor.apply();
    }

    @Override
    protected void onPause() {
        super.onPause();
        SharedPreferences.Editor preferencesEditor =
                preferences.edit();

        preferencesEditor.putInt("count", count);
        preferencesEditor.putInt("color", color);
        preferencesEditor.apply();
    }
}
```
