09 AsyncTask
===

# 1. AsyncTask

AsyncTask는 다음과 같은 상황에서 사용하면 좋습니다.

- 짧거나 중단 불가능한 작업
- UI 또는 사용자에게 다시 보고할 필요가 없는 태스크
- 완료되지 않은 상태로 둘 수 있는 낮은 우선 순위 태스크

![alt](img/AsyncTask%20process.png)

# 2. AsyncTask 생성

1. Subclass AsyncTask
2. Provide data type sent to doInBackground()
3. Provide data type of progress units for onProgressUpdate()
4. Provide data type of result for onPostExecute()


private class MyAsyncTask 
    extends AsyncTask<URL, Integer, Bitmap> {...}

![alt](img/AsyncTask%20paremeter.png)

# 3. AsyncTask의 한계

- 장치의 설정이 바뀌면 Activity는 제거되므로 AsyncTask를 더 이상 Activity에 연결할 수 없습니다.
- 구성 사항이 변경 되때 마다 새로운 AsyncTask가 생성됩니다.
- AsyncTask가 제거되지 않고 남아 메모리 부족이나, 충돌을 야기합니다.