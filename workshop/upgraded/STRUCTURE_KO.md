# 업그레이디드 폴더 구조 설명

이 디렉터리는 레거시 프로젝트(`legacy` 폴더)의 모든 파일과 폴더를 동일하게 복사하여 생성된 업그레이드 작업 공간입니다.

## 주요 폴더 및 파일
- `MANIFEST.in`, `README.rst`, `setup.py`, `distribute_setup.py`, `distribute-0.6.10.tar.gz`: 프로젝트 메타 및 설치 관련 파일
- `docs/`: Sphinx 기반 문서 폴더
  - `build/`: 빌드된 문서(html, doctrees 등)
  - `source/`: 문서 소스(rst, conf.py 등)
- `guachi/`: 주요 Python 모듈 및 테스트 코드
  - `__init__.py`, `config.py`, `database.py`: 설정 및 DB 연동 코드
  - `tests/`: 유닛 및 통합 테스트
- `guachi.egg-info/`: 패키징 정보

## 활용 방법
- 이 폴더에서 최신 Python 버전으로 코드 업그레이드, 리팩터링, 테스트, 문서화 작업을 진행할 수 있습니다.
- 원본 레거시 코드와 구조가 동일하므로, 변경 전후 비교 및 기능 검증이 용이합니다.

---

이 파일은 `/workspaces/github-copilot-upgrading/workshop/upgraded` 폴더의 구조와 역할을 설명합니다.