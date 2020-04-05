TextView
===

TextView는 View의 하위 클래스로 여러줄의 텍스트를 나타낸다.
HTML의 <b>와 <i>태그만 사용할 수 있다. 

```
<TextView
    android:id="@+id/textView"
    android:layout_width="215dp"
    android:layout_height="110dp"
    android:text="@string/hello_world" // string을 resource 파일로 관리하면 다양한 언어에 대해 유지보수가 간단하다.
    app:layout_constraintBottom_toBottomOf="parent"
    app:layout_constraintEnd_toEndOf="parent"
    app:layout_constraintHorizontal_bias="0.258"
    app:layout_constraintStart_toStartOf="parent"
    app:layout_constraintTop_toTopOf="parent"
    app:layout_constraintVertical_bias="0.062" />
```

