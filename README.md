## How to edit xml to csv

xml 파일을 열면 filename 속성과 여러개의 object속성이 보인다.  
object속성에는 bndbox속성이 있는데,  
네개의 요소, xmin, xmax, ymin, ymax, 네개의 값은 필요한 값이다.  
다음으로 필요한 값은 filename속성의 값과 size속성의 width, height 값이 필요하다.  
필요한 값들은 읽어온 뒤 다음과 같은 순서로 나열해 모든xml정보를 하나의 csv파일로 만들면 된다.  
아래 예시 참고
  
  |행번호|filename|width|height|name|xmin|ymin|xmax|ymax|
  |-----|-------|---|---|----------|----|----|----|----|
  |1행|0.jpg|4128|2322|10c|2546|375|2902|535|
  |2행|0.jpg|4128|2322|10c|1566|1343|1930|1503|
  |3행|1.jpg|3728|1237|kh|3672|1237|4369|2389|
  
  위는 단순한 예시로 1행,2행 등 행구분 번호는 생략한다.
  들어가야하는 정보는 filename, width, height, class, xmin, ymin, xmax, ymax 이다.
  class안에는 <object>태그의 <name>속성의 값이 들어간다.
