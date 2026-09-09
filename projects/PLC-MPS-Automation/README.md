# PLC · MPS 자동 적재

공급 → 컨베이어 이송 → Pick → 적재를 연결한 **교육용 실물 MPS 제어 프로젝트**입니다.

**개인 과제 · 2026년 1학기** · Mitsubishi Q Series / 2축 서보 / GX Works2 / GP-Pro EX

- **담당:** 자동·수동 시퀀스, 위치결정, HMI 6화면, 오류 표시와 재개 흐름.
- **문제 → 변경:** 8번째 적재 실패 지점을 찾기 어려웠던 구조를 STEP·완료조건 중심으로 다시 구성했습니다.
- **확인:** 순차·지그재그 각 8개 적재, 중단 후 수량·인덱스를 유지한 재개.

[13초 동작 미리보기](#demo) · [제어 구조](docs/control-design.md) · [결과 근거](docs/results.md) · [English](#english-overview)

<img src="assets/mps-overview.jpg" width="800" alt="최종 시연의 8개 적재 장면. 교육용 MPS의 2축 서보와 적재 팔레트">

## 동작 보기

<a name="demo"></a>

**공급과 이동 → Pick → Place → 최종 적재** 순서로 보세요. 4개 핵심 구간을 연결한 13초·2배속 미리보기입니다.

[![공정 4장면을 표시한 2배속 GIF. 클릭하면 원속도 MP4 파일로 이동합니다](assets/process-preview.gif)](assets/process-demo-1x.mp4)

[원속도 MP4 · 46초 · 무음](assets/process-demo-1x.mp4) · [정지 화면](assets/process-poster.jpg) · [구간별 관찰 포인트](docs/results.md#영상-읽기)

MP4는 저장소 파일 링크입니다. GitHub에서 재생 화면이 나오지 않으면 다운로드해 볼 수 있습니다. 영상의 구간 사이에는 컷이 있으며, 순차·지그재그 비교나 Resume의 근거는 아래 제어 기록에 따로 연결했습니다.

## 무엇을 바꿨는가

**1. 실패 위치를 찾을 수 있는 시퀀스**

타이머 중심으로 이어붙인 공정을 STEP 릴레이와 완료비트로 나눴습니다. 현재 STEP을 D300으로 함께 표시하고, D320 오류 코드와 HMI 진단 화면으로 정지 위치를 확인하도록 했습니다.

**2. 간섭하지 않는 두 동작만 중첩**

STEP30에서 공급과 POS_PICK 이동을 겹쳤습니다. Pick은 **공급 완료 + 컨베이어 안정화 + 서보 이동 완료**를 모두 확인한 뒤 시작합니다. [STEP별 완료조건과 Busy Seen 수정](docs/control-design.md)

**3. Reset과 Resume 분리**

전체 초기화와 상태 유지 재개를 나눴습니다. 중단 후에는 완료 수량과 다음 적재 위치를 보존하고, HMI 수동운전으로 장비·공작물 상태를 확인·조정한 뒤 자동운전을 이어갔습니다.

## 결과와 기술 자료

8개 적재와 재개 흐름은 최종 보고서·수행 기록에 근거합니다. 보고서의 시간 비교 **12:00 → 10:25**는 [측정 조건의 확인 범위](docs/results.md)에 따로 정리했습니다.

| 읽고 싶은 내용 | 자료 |
| --- | --- |
| STEP, 위치 테이블, 부분 병렬화, 재개 조건 | [제어 설계](docs/control-design.md) |
| 시연 구간, 적재 패턴, 결과의 근거 | [결과와 영상](docs/results.md) |
| 장비·개발 환경, 공개 파일로 확인 가능한 범위 | [환경과 재현 범위](docs/environment.md) |

X2는 신규 공정 명령을 막는 소프트웨어 중단입니다. 이동 중 서보의 감속 정지나 하드웨어 안전 기능을 검증한 프로젝트는 아닙니다. 자동 전이 일부는 내부 비트·타이머를 사용합니다.

## English overview

<details>
<summary>Physical MPS sequencing, partial parallelization and restart behavior</summary>

An individual coursework project controlling an educational MPS from feeding to an eight-part stack. I worked on automatic/manual sequences, servo positioning, six HMI screens, diagnostics and restart behavior.

After an eighth-part positioning failure became difficult to locate, I rebuilt the sequence around explicit steps and completion conditions. I overlapped feeding with travel to the pick position, then joined the completion conditions before picking. Reset and Resume were separated: completed count and stack index were retained, with operator checks and manual repositioning before restart.

Sequential and zigzag eight-part stacking and the restart workflow were checked on the physical training machine. The demo above contains four labeled excerpts; the MP4 preserves the source speed. The report's timing comparison lacks retained repeat-measurement conditions. The software stop does not establish a hardware safety function.

</details>

[자료 출처·작성 범위](SOURCES.md) · [다른 프로젝트](../../README.md)
