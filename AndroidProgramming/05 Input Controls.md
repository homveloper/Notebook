05 Input Controls
===

# 1. Overview

안드로이드에서 사용자들로 부터 입력을 받는 방법은 다양합니다. 앞서 학습한 EditText가 있습니다. 또는 선택 버튼을 통해서 사용자들의 입력을 받을 수도 있습니다. 설정 창에서는 설정 값들을 조절하도록 하여 입력을 받을 수도 있습니다. 입력을 받는 목록은 다음 같이 있습니다.

- EditText
- SeekBar
- CheckBox
- RadioButton
- Switch
- Spinner

# 2. View focus

View는 입력 제어를 포함하여 모든 UI 요소들이 있는 가장 기본적인 클래스입니다. View Focus에서 Focus란 사용자의 입력을 받고 있는 View를 의미합니다. 즉 하나의 View만이 Focus를 받을 수 있습니다. Focus를 받는 방식은 다양하게 있습니다.

- 사용자의 터치
- 입력창을 작성한 이후 다음, 종료, 저장 버튼등을 누를 때
- focus를 받을 만한 어느 View에 requestFocus()를 호출

## 2.1 Clickable과 Focusable

Clickable이란 클릭이나 탭하면서 View가 반응하는 것이다. Focusable은 입력을 받아들이면서 View가 반응하는 것 이다.

## 2.2 다음 Focus의 위치는 ?

터치를 한 가장 최상단 부터 Focus를 받게 되며 그 이동은 왼쪽에서 오른쪽, 위에서 아래로 이동하게됩니다. 직접적인 제어로 사용자가 Focus를 할수 있습니다. UI가 자연스럽게 Focus될 수 있도록 화면을 설계하는 것이 중요합니다.

``` XML
android:id="@+id/top"
android:focusable="true"
android:nextFocusDown="@+id/bottom"
```

# 3. Freeform text and numbers

EditText는 여러줄의 입력을 받을 수 있습니다. 숫자, 추천단어, 엔터를 이용한 여러줄 입력등을 지원합니다. 이러한 다양한 유형의 입력 방법은 "inputType"을 통해 지정할 수 있습니다.

EditText View를 위해 EditText 객체를 가져오는 방법은 다음과 같습니다.

```java
EditText simpleEditText = findViewById(R.id.edit_simple);

// EditText's text to string
String value = simpleEditText.getText().toString();
```

# 4. providing choices

안드로이드에서는 UI에 다양한 선택방법을 제공하고 있습니다. UI의 선택방식은 다음과 같습니다.

- CheckBox
    
- RadioButton
  
- ToggleButton
  
- Spinners
  Spinner는 XML layout을 통해 생성할 수 있습니다. Spinner에 목록을 정의하는 방법은 배열을 이용하면 됩니다. Spinner의 목록 중 특정 항목을 선택하면 onItemSelectedListener()를 이용해 해당 View를 파악할 수 있습니다. 생선된 Spinner에 adapter를 지정합니다.

  > adapter는 상호호환적이지 않은 인터페이스들을 연결시켜주는 역할을 합니다.


  ``` XML
  <Spinner
    android:id="@+id/label_spinner"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content">
  </Spinner>
  ```

  안드로이드에서는 대부분의 데이터를 XML파일로 두어 사용할 것을 권장하고 있습니다. Spinner의 목록도 XML 파일로 저장하여 사용합니다.

    ```XML
    <string-array name="labels_array">
        <item>Home</item>
        <item>Work</item>
        <item>Mobile</item>
        <item>Other</item>
    </string-array>
    ```

    Spinner의 객체를 생성하여 Listner를 지정하는 방법은 다음과 같습니다.

    ```Java
    // In OnCreate()

    Spinner spinner = (Spinner) findViewById(R.id.label_spinner);
    if(spinner != null){
        spinner.setOnItemsSelectedListener(this);
    }
    ```

    이제 생성된 Spinner에 ArrayAdapter를 이용하여 앞서 만든 string-array를 지정합니다.

    ```Java
    ArrayAdapter<CharSequence> adapter = ArrayAdapter.createFromResource(this, R.array.labels_array, android.R.layout.simple_spinner_item);
    ```
    
    android.R.layout은 안드로이드가 미리 지정한 layout를 가져오는 것 입니다.

    앞서 Spinner 객체를 생성하면서 listner에 this로 지정하였습니다. 이는 AdapterView.onItemSelectedListner를 의미하는 것으로 implements를 하여야 합니다.

    ```Java
    public void onItemSelected(AdapterView<?> adapterView, View view, int pos, long id){
        String spinner_item = adapterView.getItemAtPostion(pos).toString();
    }

    public void onNothingSelected(AdapterView<?> adapterView){
        // Do something
    }
    ```

# 5. input control 예제

