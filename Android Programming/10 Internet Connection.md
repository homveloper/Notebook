10 Internet Connection
===

# 1. 인터넷 연결 과정

1. Add permissions to Android Manifest

    ```XML
    <uses-permission android:name="android.permission.INTERNET"/>
    ```

2. Check Network Connection

    ```XML
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
    ```

    ```Java
    ConnectivityManager connMgr = (ConnectivityManager)getSystemService(Context.CONNECTIVITY_SERVICE);

    // 네트워크 상태
    NetworkInfo networkInfo = connMgr.getActiveNetworkInfo();

    if (networkInfo != null && networkInfo.isConnected()) {
        // Create background thread to connect and get data
        new DownloadWebpageTask().execute(stringUrl);
    } else {
        textView.setText("No network connection available.");
    }

    // wifi 또는 mobile(celluler)
    NetworkInfo networkInfo = connMgr.getNetworkInfo(ConnectivityManager.TYPE_WIFI);
    boolean isWifiConn = networkInfo.isConnected();

    networkInfo = connMgr.getNetworkInfo(ConnectivityManager.TYPE_MOBILE);
    boolean isMobileConn = networkInfo.isConnected();

    ```

3. Create Worker Thread
    
    ```Java
    
    ```

4. Implement background task
    1. Create URI(Uniform Resource Identifier)

        - file:// 
        - http:// and https://
        - content://

        ```Java
        // Google Books API
        final String BASE_URL = "https://www.googleapis.com/books/v1/volumes?";    
        final String QUERY_PARAM = "q"; 
        final String MAX_RESULTS = "maxResults"; 
        final String PRINT_TYPE = "printType"; 

        Uri builtURI = Uri.parse(BASE_URL).buildUpon()
                        .appendQueryParameter(QUERY_PARAM, "pride+prejudice")
                        .appendQueryParameter(MAX_RESULTS, "10")
                        .appendQueryParameter(PRINT_TYPE, "books")
                        .build();

        URL requestURL = new URL(builtURI.toString());

        ```

    2. Make HTTP Connection, Connect and GET Data
        HttpURLConnection 객체를 이용합니다.

        ```Java
        try{
            HttpURLConnection conn = (HttpURLConnection) requestURL.openConnection();

                    conn.setReadTimeout(10000 /* milliseconds */);
                    conn.setConnectTimeout(15000 /* milliseconds */);
                    conn.setRequestMethod("GET");
                    conn.setDoInput(true);

            conn.connect();

            int response = conn.getResponseCode();

            InputStream is = conn.getInputStream();
            String contentAsString = convertIsToString(is, len);

            return contentAsString;
        }catch(Exception e){
            //code
        }finally {
            conn.disconnect();
                if (is != null) {
                    is.close();
                }
        }

                public String convertIsToString(InputStream stream, int len) 
            throws IOException, UnsupportedEncodingException {
            
            Reader reader = null;
            reader = new InputStreamReader(stream, "UTF-8");
            char[] buffer = new char[len];
            reader.read(buffer);
            return new String(buffer);
        }

        public String convertIsToString(InputStream stream, int len) 
            throws IOException, UnsupportedEncodingException {
            
            Reader reader = null;
            reader = new InputStreamReader(stream, "UTF-8");
            char[] buffer = new char[len];
            reader.read(buffer);
            return new String(buffer);

            //use BufferedReader

            // StringBuilder builder = new StringBuilder();
            // BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));

            // String line;
            // while ((line = reader.readLine()) != null) {
            //     builder.append(line + "\n");
            // }
            // if (builder.length() == 0) {
            //     return null;
            // }
            // resultString = builder.toString();
        }
        ```

    또는 Connection library를 이용하는 방법이 있습니다. 여기서는 OkHttp 나 Volly를 사용할 수 있습니다.

    - Volley

        ```Java
        RequestQueue queue = Volley.newRequestQueue(this);
        String url ="http://www.google.com";

        StringRequest stringRequest = new StringRequest(Request.Method.GET, url,
                    new Response.Listener<String>() {
            @Override
            public void onResponse(String response) {
                // Do something with response
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {}
        });
        queue.add(stringRequest);
        ```
    - OkHttp

        ```Java
        OkHttpClient client = new OkHttpClient();
        Request request = new Request.Builder().url("http://publicobject.com/helloworld.txt").build();

        client.newCall(request).enqueue(new Callback() {
            @Override
            public void onResponse(Call call, final Response response){
                throws IOException {
                    try {
                        String responseData = response.body().string();
                        JSONObject json = new JSONObject(responseData);
                        final String owner = json.getString("name");
                    } catch (JSONException e) {
                    }
                }
            }
        });
        ``` 

5. Process results 
    1. Parse Results

    결과는 helper 클래스들을 통해 parsing 할 수 있습니다.

    - JSONObject, JSONArray
    - XMLPullParser

    


    - JSONObject

        ```JSON
        {
            "population":1252000000,
            "country":"India",
            "cities":["New Delhi","Mumbai","Kolkata","Chennai"]
        }
        ```

        ```Java
        JSONObject jsonObject = new JSONObject(response);
        String nameOfCountry = (String) jsonObject.get("country");  
        long population = (Long) jsonObject.get("population");  
        JSONArray listOfCities = (JSONArray) jsonObject.get("cities"); 
        Iterator<String> iterator = listOfCities.iterator();  
        while (iterator.hasNext()) {  
            // do something  
        }  
        ```

        또다른 JSON을 다루는 예입니다.

        ```JSON
        {
            "menu": {
                "id": "file",
                "value": "File",
                "popup": {
                    "menuitem": [
                        {"value": "New", "onclick": "CreateNewDoc()"},
                        {"value": "Open", "onclick": "OpenDoc()"},
                        {"value": "Close", "onclick": "CloseDoc()"}    
                        ]  
                }   
            }
        }
        ```

        ```Java
        //Get "onclick" value of the 3rd item in the "menuitem" array
        JSONObject data = new JSONObject(responseString);
        JSONArray menuItemArray = data.getJSONArray("menuitem");
        JSONObject thirdItem = menuItemArray.getJSONObject(2);
        String onClick = thirdItem.getString("onclick");
        ```
