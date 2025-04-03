# 이미지 슬라이드쇼 프로그램

이 프로그램은 선택한 폴더 내의 이미지들을 슬라이드쇼 형식으로 볼 수 있는 간단한 윈도우 프로그램입니다.

## 주요 기능

- 폴더 내 이미지 자동 로드
- 이전/다음 버튼으로 이미지 탐색
- 키보드 화살표 키로 이미지 탐색
- 창 크기에 맞는 자동 이미지 리사이즈
- 다양한 이미지 형식 지원

## 설치 방법

1. Python이 설치되어 있지 않다면 [Python 공식 웹사이트](https://www.python.org/downloads/)에서 다운로드하여 설치합니다.
2. 필요한 패키지를 설치합니다:
   ```
   pip install -r requirements.txt
   ```
   또는
   ```
   pip install Pillow
   ```

## 사용 방법

1. `image_slideshow.py` 파일을 실행합니다.
2. "폴더 선택" 버튼을 클릭하여 이미지가 있는 폴더를 선택합니다.
3. "이전"과 "다음" 버튼을 사용하여 이미지를 탐색합니다.
4. 키보드의 왼쪽/오른쪽 화살표 키를 사용하여 이미지를 탐색할 수도 있습니다.

## 지원하는 이미지 형식

- JPG/JPEG
- PNG
- GIF
- BMP

## 시스템 요구사항

- Windows 10 이상
- Python 3.6 이상
- Pillow 라이브러리

## 라이선스

이 프로젝트는 MIT 라이선스로 배포됩니다.

## 기여하기

1. 이 저장소를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/amazing-feature`).
3. 변경사항을 커밋합니다 (`git commit -m 'Add some amazing feature'`).
4. 브랜치에 푸시합니다 (`git push origin feature/amazing-feature`).
5. Pull Request를 생성합니다. 