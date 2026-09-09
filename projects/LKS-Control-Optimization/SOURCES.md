# 자료 출처

| 공개 파일 | 원본과 처리 |
| --- | --- |
| `data/reported_metrics.csv` A/B/C | 개인 과제 `figures/abc_compare.csv`의 3행, 수치 유지 |
| 같은 CSV Reported ML | 보고서 선택값과 대조한 보관 시뮬레이션 지표; 원본 수치 유지 |
| `figures/abc_curve_error.png` | 개인 과제 `fig_abc_ds_curve.png`, 기존 portfolio_export에서 보존; SHA-256으로 원본 대조 |
| `figures/structure-comparison*.png` | 공개 CSV의 B/C 곡선 RMS, 0 기준의 가로 막대. 모바일본도 같은 값 |
| `figures/tradeoff.png` | B와 보고서 선택값의 곡선 RMS·최대 조향각. 공개 CSV의 재시각화 |
| 평가식 | 최종 보고서 §4·6·7 및 `LKSUtils.calcCost`와 대조 |
| 당시 Q/R 탐색 절차 | 최종 보고서와 경험 기록: 5,000개 결과 → Random Forest → 20,000개 후보 → 상위 20개 Simulink 재실행 |
| 보고서 선택값의 추가 확인 | 보관 시뮬레이션 데이터의 Q/R·지표와 보고서 선택값 대조 |
| `tools/`, `tests/` | 2026-09-09 Codex와 작성한 공개용 산술 검토·시각화 도구 |

개인 수행 범위와 당시 탐색 절차는 최신 경험 기록과 최종 보고서에 근거합니다. 차량 모델·수업 코드·원본 Office/PDF·전체 탐색 데이터는 이번 공개 범위에 포함하지 않습니다. 공개 도구는 저장 지표의 산술 정합성과 시각화를 확인하며, 원본 시뮬레이션 재실행이나 모델 정확도 검증을 수행하지 않습니다.
