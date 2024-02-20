---
runme:
  id: 01HQ3DSM5N14JWXND65H9HVEEE
  version: v3
---

All Late Jobs

```sh {"id":"01HQ3DSP17VKN8CEP8TSYC10GM"}
project = MTP  AND Division = east AND labels not in (training) 
AND 
(
    (status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "waiting for dev"))
    AND NOT
    (status in ("Ready for 2nd Offshore Review", "In 2nd Offshore Review") and labels in (Delivered_By_NICA))
)
AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate < startOfDay())
    OR
    (labels in (Delivered_By_NICA) AND duedate < startOfDay(6))
)
```

All Due Today Jobs

```sh {"id":"01HQ3DWQ01YKAQDHFY3HT140R8"}
project = MTP  AND Division = east AND labels not in (training) 
AND 
(
    (status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "waiting for dev"))
    AND NOT
    (status in ("Ready for 2nd Offshore Review", "In 2nd Offshore Review") and labels in (Delivered_By_NICA))
)

AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate = startOfDay()) 
    OR 
    (labels in (Delivered_By_NICA) AND duedate = startOfDay(6))
)
```

All due Tomorrow

```sh {"id":"01HQ3KMZKW2G5B1SGD2GECGG9F"}
project = MTP  AND Division = east AND labels not in (training) 
AND 
(
    (status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "waiting for dev"))
    AND NOT
    (status in ("Ready for 2nd Offshore Review", "In 2nd Offshore Review") and labels in (Delivered_By_NICA))
)

AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate = startOfDay(1))
    OR 
    (labels in (Delivered_By_NICA) AND duedate = startOfDay(7))
)
```

due tomorrow that is need to be neglected but we need to get the "1d" and "2d" data from it... it's a data where i can get a number of days. 
example: duedate > 1d means thee due date is from tomorrow

```sh {"id":"01HQ3KRD3BPX0RE8MX1QWTMM3A"}
project = MTP AND labels not in (training) AND "Scheduling Type" = Estimating AND status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "waiting for dev") AND "Scheduling Type" in (Estimating) AND due <= 1d AND due > endOfDay() AND "Company Name" != "BFS - NicaES" AND Division = east OR project = MTP AND status in ("Ready for 2nd Offshore Review") AND labels != Delivered_By_NICA AND "Scheduling Type" in (Estimating) AND due <= 1d AND due > endOfDay() AND "Company Name" != "BFS - NicaES" AND Division = east AND status in ("In 2nd Offshore Review", "Ready for 2nd Offshore Review") AND labels not in (Delivered_By_NICA) ORDER BY status ASC
```