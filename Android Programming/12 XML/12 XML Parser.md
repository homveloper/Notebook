12 XML Parser
===

# DOM(Document Object Model)

모든 문서를 파싱하며, 그 결과를 트리로 표현합니다. DOM은 XML 문서를 탐색하거나 수정할 수 있습니다. 문서를 계층적인 트리 구조로 표현을 합니다. 

## 특징

- DOM은 언어 중립적입니다.
- Java의 명명법과는 좀 다릅니다.
- 어떤 언어든 쉽게 변경이 가능합니다.

## 사용

1. XML과 관련된 패키지를 import 합니다.
2. DocumentBuilder를 만듭니다.

```Java
DocumentBuilderFactorty factory = DocumentBuilderFactory.newInstance();
DocumentBuilder builder = factory.newDocumentBuilder();
```

3. 파일이나 stream으로 Document를 만듭니다.

```Java
Document document = builder.parse(new File(file))
```

4. root 요소를 추출합니다.

```Java
Element root = document.getDocumentElement();
```

5. 속성을 검사합니다.

6. sub-elements를 검사합니다.

## 예제 example.xml

여기서 Food 목록을 가져와 보겠습니다.

```Java
Element root = document.getDocumentElement();
NodeList foods = root.getElementsByTagName("food");
 
for(Node food : foods){
    sysout(food.getAttribute("name"))
    sysout(food.getAttribute("price"))
    sysout(food.getAttribute("description"))
}

```

# SAX : 멈추기 전까지 게속 파싱을 합니다.
