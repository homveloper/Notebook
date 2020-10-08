05 MFC Programming

# 1. MFC

## MFC의 역사

MFC는 윈도우 응용 프로그램 개발을 위해 만든 C++ class library입니다. MFC역사는 오래되었습니다. 1992년 MFC 1.0 버전이 나왔으며 Win16을 지원했습니다. MFC 2.0 버전은 **Document/View Model**을 도입합니다.  MFC 4.0 부터 컴퓨터와 인터넷의 발달로 인터넷이 지원되었으며 ActiveX 그리고 DAO를 지원하게 되었습니다. MFC 6.0에서 DAO는 ADO로 변경되었으며 추후에는 OLEDB로 넘어가게 됩니다. WTL은 HTML와 XML을 기반하여 GUI를 개발하는 라이브러리입니다.

|   year   | dev. tools          |   MFC    |    Library     | Special Spec.                      |
| :------: | :------------------ | :------: | :------------: | :--------------------------------- |
|   1992   | MS-C 7.0            |   1.0    |                | Win16 지원                         |
|   1993   | Visual C++ 1.0      |   2.0    |   mfc250.dll   | **Document/View Model 도입**       |
|   1994   | Visual C++ 2.0      |   3.0    |   mfc30.dll    | Win32 지원                         |
|   1995   | Visual C++ 4.0      |   4.0    |   mfc42.dll    | DAO, ActiveX, Internet 지원        |
| **1998** | **Visual C++ 6.0**  | **6.0**  |   mfc42.dll    | OLEDB, (DAO → )ADO, ChtmlView, ... |
|   2002   | Visual C++ .NET     |   7.0    |   mfc70.dll    | Native-Code generator              |
|   2005   | Visual C++ 2005     |   8.0    |   mfc80.dll    | Win64 지원                         |
|   2008   | Visual C++ 2008     |   9.0    |   mfc90.dll    |
| **2010** | **Visual C++ 2010** | **10.0** | **mfc100.dll** | STL, ATL, WTL 지원                 |
|   2012   | Visual C++ 2012     |   11.0   |   mfc110.dll   |
|   2013   | Visual C++ 2013     |   12.0   |   mfc120.dll   |
|   2015   | Visual C++ 2015     |   14.0   |   mfc140.dll   |
|   2017   | Visual C++ 2017     |   14.0   |   mfc140.dll   |
|   2019   | Visual C++ 2019     |   14.0   |   mfc140.dll   |

MFC는 미리 만들어진 함수를 모은 클래스 그리고 그 클래스가 모인 컴포넌트를 이용하여 어플리케이션을 제작하게 됩니다. 기업에서는 함수를 작성하여 컴포넌트를 개발하여 제품으로 판매하는 곳도 있으며, 어플리케이션을 제작하여 상업적인 서비스를 제공하는 곳도 있습니다.

API와 MFC 어플리케이션에대해 좀더 자세히 다뤄보겠습니다. MFC는 Windwos에서 제공하는 라이브러리가 아닌 Visual C++에서 제공하는 라이브러리에 국한되 있습니다. 그렇다고 해서 API보다 작은 규모가 아니라 오히려 더 많은 라이브러리를 제공합니다.

mfc140d.dll에서 d는 debug모드에서 사용되는 라이브러리이며, mfc140.dll은 release모드에서 사용되는 라이브러리 입니다. u는 상업적 목적으로 사용되는 어플리케이션에서 사용할 수 있는 라이브러리입니다. msvcrt.dll에서 crt는 런타임을 의미하며 런타임 라이브러리가 있습니다.

| vs.                  | API | MFC |
| -------------------- | --- | --- |
| provider             | Windows    | Visual C++    |
| based                | Function    |    Class |
| runtime<br>libraries | kernal32.dll<br>gid32.dll<br>user32.dll    | mfc140.dll, mfc140d.dll<br>mfcm140.dll, mfcm140d.dll<br>mfc140u.dll, mfc140ud.dll<br>mfc140u.dll, mfc140ud.dll<br>mfc140kor.dll<br>msvcrt.dll, msvcr120.dll    |
| language             | C(.c)    | C++(.cpp)    |
| resource             |   .rc (.res, .resx)    |.rc (.res, .resx)    |
| tools                |  Project Template   |  AppWizrd<br>ClassWizard<br>ActiveX Control Wizard   |
| dev. model           |  -   | Document/View model    |


# 2. MFC Hierarchy

# 3. Global functions

# 4. Naming conventions

# 5. MFC Applications

# 6. Classes

