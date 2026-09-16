# 저장 지표

`reported_metrics.csv`에는 보관된 시뮬레이션 지표의 원본 수치를 4행으로 정리했습니다. A/B/C는 제어 구조를 비교한 결과이며, Reported ML은 저장된 지표를 보고서의 Q/R 선택값과 대조한 결과입니다. `source_kind`로 제어 구조 비교 결과(`saved_ABC_comparison`)와 보고서·보관 데이터에서 확인한 선택값(`report_and_existing_dataset_rank`)을 구분합니다.

| 열 | 단위·설명 |
| --- | --- |
| under | m, t≤5 s의 반대방향 최대 횡오차 |
| curveRMS / curveBIAS | m, 35~56.1 s RMS / 평균의 절댓값 |
| settle10 | s, ±0.10 m 정착시간 |
| dfmax | deg, 최대 전륜 조향각 |
| dfrate | deg/s, 조향률 RMS |
| yawmax | deg/s, 최대 yaw rate |
| aymax | m/s², 최대 횡가속도 |
| J_reported | 무차원 비교 점수 |

수치는 반올림하지 않고 원본 정밀도로 저장했으며, README와 그림에 표시할 때만 읽기 좋게 반올림했습니다. 실험 표본이나 합성 데이터를 추가하지 않았습니다.
