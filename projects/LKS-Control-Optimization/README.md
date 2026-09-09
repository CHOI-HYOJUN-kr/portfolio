# LKS · 제어 구조 비교

차선유지 제어기에서 **추종오차와 조향 입력의 관계**를 비교한 MATLAB/Simulink 프로젝트입니다.

**개인 과제 · 2026년 1학기 · 차량 모델 시뮬레이션** · LQR / MATLAB·Simulink / Python

- **담당:** A/B/C 제어 구조 구성, Q/R·8개 평가 지표 설정, 결과 비교·해석.
- **문제 → 판단:** 복잡한 C가 유리할 것이라는 예상을 동일 조건의 B/C 비교로 검토했습니다.
- **확인:** 곡선 RMS는 **B 3.68 mm / C 10.29 mm**로 B가 더 작았습니다.

[비교 CSV](data/reported_metrics.csv) · [판단과 평가식](docs/analysis.md) · [재계산](#직접-확인하기) · [English](#english-overview)

<picture>
  <source media="(max-width: 600px)" srcset="figures/structure-comparison-mobile.png">
  <img src="figures/structure-comparison.png" alt="80 km/h, 초기 횡오차 1 m 시뮬레이션. B의 곡선 RMS 3.68 mm, C는 10.29 mm. 두 막대는 0에서 시작합니다.">
</picture>

## 무엇을 비교했는가

| 구조 | 구성 | 곡선 RMS | 평가 J |
| --- | --- | ---: | ---: |
| A | 상태 피드백 + 적분 | 203.60 mm | 1385.110 |
| B | 상태 피드백 + 곡률 앞먹임 | **3.68 mm** | **0.682** |
| C | 상태 피드백 + 적분 + 곡률 앞먹임 | 10.29 mm | 5.662 |

조건은 **80 km/h 정속, 초기 횡오차 1 m**, 곡선 평가 구간 35~56.1 s입니다. 원래 수동 설정에서 B의 RMS와 J가 C보다 작았습니다. 지속 측풍이나 모델 불일치를 추가한 비교는 아니므로, 적분 제어가 일반적으로 불필요하다는 결론으로 확장하지 않았습니다. [당시 시간응답](figures/abc_curve_error.png)

## 판단 기준: 오차와 조향을 함께 보기

Q/R로 오차와 입력의 비중을 조절하기 위해 LQR을 선택했습니다. 결과의 순위는 추종성·조향·차량 응답의 **8개 지표를 정규화한 평가 J**로 비교했습니다. 이 J는 LQR 설계 비용과 별도로 계산합니다.

보고서의 Q/R 선택값은 B보다 최대 조향각이 **5.42° → 3.89°**로 작지만, 곡선 RMS는 **3.68 → 5.92 mm**로 커집니다. J=0.559를 모든 지표의 개선으로 해석하지 않았습니다.

<details>
<summary>보고서 선택값과 B의 trade-off 보기</summary>

![B와 보고서 선택값 비교. 선택값의 조향각은 작고 곡선 RMS는 큼](figures/tradeoff.png)

보고서의 선택값과 대조한 저장 시뮬레이션 지표로 그린 비교입니다. 추종오차와 조향 입력의 차이를 함께 보여줍니다.

</details>

**당시 수행 절차:** 보고서와 경험 기록을 기준으로, 5,000개 시뮬레이션 결과로 Random Forest를 학습하고 20,000개 Q/R 후보의 평가 J를 예측한 뒤 상위 20개 후보를 Simulink에서 재실행했습니다. Random Forest는 **후보 선별용 대리모델**로 사용했고, 최종값은 시뮬레이션 결과로 판단했습니다. [평가식·후보 탐색](docs/analysis.md)

**현재 공개 범위:** 저장 지표 4행의 J 재계산과 그래프 재생성을 제공합니다. 당시 전체 탐색을 다시 실행하는 구성은 포함하지 않습니다. [실행 방법과 재현 범위](docs/reproducibility.md)

## 직접 확인하기

portfolio 저장소 루트에서:

```sh
cd projects/LKS-Control-Optimization
python tools/verify_metrics.py
```

공개 CSV 4행에서 J를 재계산합니다. Python 표준 라이브러리만 필요합니다. Simulink를 다시 실행하는 도구는 아닙니다.

[원본 정밀도의 CSV](data/reported_metrics.csv) → [단위·지표 정의](data/README.md) → [재계산 코드](tools/verify_metrics.py)

그래프는 저장된 수치로 다시 그렸으며 실차 결과는 없습니다. 수업 기반 모델·원본 코드의 권한과 작성 범위가 확정되지 않아 이 저장소에는 선별 결과와 새 산술 검토 도구를 제공합니다.

## English overview

<details>
<summary>LQR structures, evaluation criteria and a steering/tracking trade-off</summary>

An individual MATLAB/Simulink study at 80 km/h with an initial lateral error of 1 m. I configured three control structures, chose Q/R and eight evaluation metrics, and compared the results.

Under the original manual settings, feedback plus curvature feedforward (B) produced lower curve RMS than the same structure with integral action (C): 3.68 vs 10.29 mm. The reported Q/R selection reduced peak steering from B's 5.42° to 3.89°, while increasing curve RMS to 5.92 mm. A lower evaluation cost did not mean every metric improved.

The report and experience record describe a workflow using 5,000 simulation results to train a Random Forest surrogate, predict evaluation J for 20,000 Q/R candidates and rerun the top 20 in Simulink. The surrogate screened candidates; the final choice used simulation results.

This repository supports cost recalculation from four stored metric rows and plot regeneration. It does not include the complete original search environment. These are model simulation results, with no vehicle testing.

</details>

[자료 출처·도구 작성 범위](SOURCES.md) · [다른 프로젝트](../../README.md)
