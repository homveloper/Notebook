# 3. MFC Hiararchy

## Application Architecture 클래스!!

> #include <afxwin.h>

프로그램의 뼈대를 이루는 클래스이며 다음과 같은 구조를 이룹니다. CWinApp, CDocument, CFrameWnd, CView가 핵심 클래스이며 꼭 알아두어야 합니다. 아래 구조는 AppWizard가 생성합니다. CDocument는 없어도 MFC가 실행됩니다.

- CObject : 거의 모든 MFC의 기반 클래스
  - CCmdTarget : 커맨드 메시지를 받는 기능 담당
    - **CWinApp** : **프로그램을 구동시키는 기능 담당**
    - **CDocument** : 데이터를 저장하고 처리하는 기능 담당
    - CWnd : 윈도우에 관련된 기능 담당
      - **CFrameWnd** : 윈도우의 프레임을 관리하는 기능 담당
      - **CView** : 데이터를 보여주는 기능 담당

## Window 클래스

> 참조. afxwin.h, afxdlgs.h, afxcmn.h

- CWnd
  - CFrameWnd
  - CView
  - CDialog
  - CSplitterWnd
  - CControlBar
  - CPropertySheet
  - CPropertyPage
  - COlePropertyPage
  - Other Controll Class : Button, EditBox, ComboBox

## 그래픽 클래스

> afxwin.h

## 데이터형 클래스

- CPoint : 2차원 좌표를 저장하기 위한 클래스
- CSize : x, y길이를 저장하기 위한 클래스
- CRect : 사각형의 좌표를 나타내는 클래스
- CString
- CTime
- CTimeSpan

## 파일 및 데이터베이스 클래스

- CFile
- CRecentFileList
- CDatabase
- CRecordset
- CDaoDatabase
- CDaoRecordset

## 인터넷 클래스

- CInternetSession
- CHttpConnection
- CFtpConnection
- CFileFind
- CHttpServer
- CHtmlStream

## OLE 클래스

## 오류처리 및 디버깅 클래스

## MFC Global Functions

> 참조. Afx(Application Framework)는 MFC의 기반


| Afx함수                | 기능                               |
| ---------------------- | ---------------------------------- |
| AfxAbort()             | 응용 프로그램을 종료               |
| AfxBeginThread()       | 스레드를 생성하고 시작             |
| AfxEndThread()         | 현재 스레드를 종룔                 |
| AfxMessageBox()        | 메시지 상자 표시                   |
| AfxGetApp()            | CWinApp 객체의 포인터 리턴         |
| AfxGetAppName()        | 응용 프로그램의 이름 리턴          |
| AfxGetInstanceHandle() | 응용 프로그램의 인스턴스 핸들 리턴 |
| AfxGetMainWnd()        | 메인 프레임 차에 대한 포인터 리턴  |
| AfxRegisterWndClass()  | 사용자 정의 WndClass 등록          |
