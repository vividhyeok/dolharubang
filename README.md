# dolharubang

Jeju 감성 돌하르방 데이트 VN (Ren'Py).

## 특징
- 모듈화된 상태 시스템 (`systems/state.rpy`)
- 숫자 기반 맵 자동 등록 시스템 (`systems/maps.rpy`)
- Day 루프에서 자동 다음 미해금 맵/랜덤 후보 선택
- 호감도(aff), 돈(money) 관리 및 선택지 영향
- 간단 HUD (`screens/hud.rpy`)
- 엔딩 분기 (true/meme/normal)

## 실행
1. Ren'Py 런처에서 프로젝트 디렉토리 선택
2. Launch (Shift+R로 빠른 리로드)

## 맵 추가 방법 (폭발적 확장)
파일 규칙: `game/maps/map_XXX.rpy`
```renpy
init python:
    register_map("006", desc="설명")

label map_006:
    n "장면 텍스트"
    menu:
        "선택지A":
            $ add_aff(+2)
        "선택지B":
            if can_pay(1000):
                $ pay(1000); $ add_aff(-3)
            else:
                n "돈 부족"
    $ mark_map_finished("006")
    $ gst.day += 1
    jump day_loop
```

## 구조 개요
- `game/routes/dayloop.rpy` : 메인 흐름(splash → epilogue → prologue → day_loop)
- `game/maps/map_XXX.rpy` : 개별 데이트 씬
- `game/systems/maps.rpy` : 맵 레지스트리와 선택 로직
- `game/screens/map_picker.rpy` : 랜덤 후보 선택 UI
- `game/systems/state.rpy` : GST 클래스 & persistent flags
- `game/routes/endings.rpy` : 엔딩 분기

## 상태 변수
| 이름 | 설명 |
|------|------|
| gst.day | 현재 일수 |
| gst.money | 보유 금액 |
| gst.aff | 호감도 (0~100 클램프) |
| persistent.maps_seen | 본 맵 id 집합 |
| persistent.seen_epilogue | 에필로그 봤는지 |
| persistent.seen_intro | 프롤로그 봤는지 |

## 커맨드 메모 (초기 push)
```bash
git init
git add .
git commit -m "Initial commit: dolharubang core systems and maps"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/dolharubang.git
git push -u origin main
```

### 이미 너무 많은 파일이 잡혔다고 느낄 때
실제 추적 파일 수 확인:
```powershell
git ls-files | Measure-Object -Line
```
Ren'Py 컴파일 산출물(*.rpyc 등)이 실수로 커밋되었다면 .gitignore 추가 후 제거:
```powershell
git rm --cached -r game/cache
git rm --cached *.rpyc *.rpymc *.rpyb
git commit -m "Remove compiled Ren'Py artifacts"
```
현재 레포는 약간의 소스 + 에셋만 추적 중(100개 안팎)이며 10k 이상이 아님. OneDrive 동기화 팝업이나 에디터 탐색기가 전체 동기화 파일 수를 보여 혼동될 수 있습니다.

## 라이선스
추후 결정 (예: MIT, CC-BY-NC 등). 현재는 미정.

## 다음 아이디어
- 호감도 구간별 변형 대사
- 맵 잠금(조건부 접근) 시스템
- Codex 화면 확장 (맵/힌트 기록)
- CG/이미지 연동
