File System Implementation
=====
# 1. File-System Structure



# 2. File-System Implementation

# 3. Directory Implementation

# 4. Allocation Methods

## Contiguous
파일을 디스크에 연속적으로 저장해보자

![contiguous](./image/contiguous_allocation.png)

아 연속적으로 저장하고 싶은데 다른 파일이 이미 그 공간을 차지하고 있네 그러면 어떻게 하지?? 다른 방법이 없을까?

## Linked
파일을 연속적으로 저장할 때 발생하는 문제점을 해결하기 위해 파일 조각을 연결시켜서 임의의 위치에도 저장할 수 있도록 하는 방법
![linked](./image/linked_allocation.png)

## Indexed
파일 조각들의 위치를 나타내는 테이블을 통해 파일을 가져오자
![indexed](./image/index_allocation.png)

## Mapping
![mapping](./image/mapping_allocation.png)

UNIX의 UFS는 이러한 방식을 사용한다.

# 5. Free-Space Management

# 6. Efficiency and Performance

# 7. Recovery

# 8. NFS

# 9. Example: WAFL File System