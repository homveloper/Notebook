01 Windows Programming 개요
===

# 1. 윈도우즈 프로그래밍 개념

윈도우즈 프로그래밍이란 **사용자가 발생시키는 이벤트에 대한 메시지를 처리**하는 과정이다. 

이는 메시지 기반(Message Driven)프로그래밍 방식이며 이벤트 기반(Event Drivent)프로그래밍으로도 부른다.

여기서 이벤트는 운영체제가 식별한 것이며, 운영체제는 프로그램으로 이를 전달합니다.

윈도우즈 프로그래밍은 Win32, Win64 SDK나 MFC, .NET, GUI등으로 다양하게 구현할 수 있다.

# 2. Win32 & Win32 API

- Win32 : 32bits windows OS platform
- Win32 API : 32bits windows programming을 위해 제공되는 C언어 Library. Windows 7 기준 2151개의 함수를 제공한다. 

## 특징

- 32bit 데이터 처리 (XP는 Win64 API 지원)
- 32bit 선형 메모리 관리
- 선점형 멀티태스킹, 멀티스레딩
- 객체지향 그래픽 환경
- 장치 독립적 입출력
- 사건 중심 처리

# 3. Windwos Programming 특징

- GUI

    사용자 명령을 받아들이는 부분이 그래픽 요소 이다. 예를 들어 버튼 누르기, 메뉴 선택등이 있다.

- 일관된 UI

    버전이 올라가도 UI 레이아웃이 일관된 형태를 유지한다. 이는 프로그램의 기본 골격이 동일하다고 볼 수 있다. 새로운 프로그램이라도 익숙한 메뉴 형태이기에 빠르게 습득할 수 있다.

- 이벤트 기반 구조(Event-Driven Structure)

    Window(창)는 Application과 Windows OS 사이에 메시지를 교환함으로써 다중작업이 가능하다.

    ```c++
    typedef struct tagMSG{
        HWND hwnd;      // 메시지를 받은 윈도우
        UINT message;   // 메시지 식별자
        WPARAM wParam;  // 메시지 정보
        LPARAM lParam;  // 메시지 정보
        DWORD time;     // 메시지 발생 시간
        POINT pt;       // 메시지 발생시 커서 좌표
    } MSG, *PMSG;
    ```

    > 참고 : [tagMSG](https://docs.microsoft.com/en-us/windows/win32/api/winuser/ns-winuser-msg)

    tagMSG 구조체의 멤버 변수중 HWND(Handle Winodw )