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
    (status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "Ready for 2nd Offshore Review", "waiting for dev"))
    # AND NOT
    # (status in ("Ready for 2nd Offshore Review", "In 2nd Offshore Review") and labels in (Delivered_By_NICA))
)
AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate < startOfDay())
    # OR
    # (labels in (Delivered_By_NICA) AND duedate < startOfDay(6))
)
```

All Due Today Jobs

```sh {"id":"01HQ3DWQ01YKAQDHFY3HT140R8"}
project = MTP  AND Division = east AND labels not in (training) 
AND 
(
    (status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "Ready for 2nd Offshore Review", "waiting for dev"))
    # AND NOT
    # (status in ("Ready for 2nd Offshore Review", "In 2nd Offshore Review") and labels in (Delivered_By_NICA))
)

AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate = startOfDay()) 
    # OR 
    # (labels in (Delivered_By_NICA) AND duedate = startOfDay(6))
)
```

All due Tomorrow

```python {"id":"01HQ3KMZKW2G5B1SGD2GECGG9F"}
project = MTP  AND Division = east AND labels not in (training) 
AND 
(
    (status in ("In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Ready for Estimating", Rework, "In 2nd Offshore Review", "Ready for 2nd Offshore Review", "waiting for dev"))

)

AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate = startOfDay(1))

)
```

EG-E-All late jobs

```python {"id":"01HQ81BXTS6JZKPG6DFA7SVN1E"}
project = MTP  AND Division = east AND labels not in (training) 
AND 
(
    "Drafter/Estimator" in (membersOf(Offshore-Egypt))
    or
    "2nd Reviewer Offshore"  in (membersOf(Offshore-Egypt))
    or
    "Reviewer Offshore"  in (membersOf(Offshore-Egypt))
    or
    (
        status = "Ready for Estimating"
        and 
        (
            "Drafter/Estimator" in  (EMPTY, "Select User")
            or
            "2nd Reviewer Offshore"  in  (EMPTY, "Select User")
            or
            "Reviewer Offshore"  in  (EMPTY, "Select User")
        )
    )
)
AND 
(
    (status in ("Ready for Estimating", "In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Rework", "In 2nd Offshore Review", "Ready for 2nd Offshore Review", "waiting for dev"))
)
AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate < startOfDay())
)
```

EG-E-All Today jobs

```python {"id":"01HQ81BZHTGNAHWBT3EETSRBEF"}
project = MTP  AND Division = east AND labels not in (training)
AND 
(
    "Drafter/Estimator" in (membersOf(Offshore-Egypt))
    or
    "2nd Reviewer Offshore"  in (membersOf(Offshore-Egypt))
    or
    "Reviewer Offshore"  in (membersOf(Offshore-Egypt))
    or
    (
        status = "Ready for Estimating"
        and 
        (
            "Drafter/Estimator" in  (EMPTY, "Select User")
            or
            "2nd Reviewer Offshore"  in  (EMPTY, "Select User")
            or
            "Reviewer Offshore"  in  (EMPTY, "Select User")
        )
    )
)
AND 
(
    (status in ("Ready for Estimating", "In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Rework", "In 2nd Offshore Review", "Ready for 2nd Offshore Review", "waiting for dev"))
)

AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
AND 
(
    (duedate = startOfDay()) 
)
```

EG-E-All Tomorrow jobs

```python {"id":"01HQ81C0W3FB3GCGB125YE0Q9P"}
    project = MTP  AND Division = east AND labels not in (training)
    AND 
    (
        "Drafter/Estimator" in (membersOf(Offshore-Egypt))
        or
        "2nd Reviewer Offshore"  in (membersOf(Offshore-Egypt))
        or
        "Reviewer Offshore"  in (membersOf(Offshore-Egypt))
        or
        (
            status = "Ready for Estimating"
            and 
            (
                "Drafter/Estimator" in  (EMPTY, "Select User")
                or
                "2nd Reviewer Offshore"  in  (EMPTY, "Select User")
                or
                "Reviewer Offshore"  in  (EMPTY, "Select User")
            )
        )
    )
    AND 
    (
        (status in ("Ready for Estimating", "In Progress", "Rework from QA", "Ready for Offshore Review", "In Offshore Review", "Ready for Project Creation", "Rework", "In 2nd Offshore Review", "Ready for 2nd Offshore Review", "waiting for dev"))
    )

    AND "Scheduling Type" != Exterior AND "Company Name" != "BFS - NicaES"  AND labels != ebn 
    AND 
    (
        (duedate = startOfDay(1))
        or 
        # (status was changed from "ready for estimating" to "in progress" after -3d) lessa bgrb hna fl goz2 da
    )
```

ETA sheet

```python
project = MTP and labels not in (training) and "Scheduling Type" = Estimating and  duedate >= 2023-1-1 and status in ("In Progress", "Ready for Offshore Review", "In Offshore Review", "Ready for 2nd Offshore Review", "In 2nd Offshore Review", "Rework from QA", Rework) and
(
    # Anyone working on the east pod projects
    (
        Division = East 
        and 
        (
            "Drafter/Estimator" in (membersOf(Offshore-Egypt)) 
            or
            "Reviewer Offshore" in (membersOf(Offshore-Egypt)) 
            or
            "2nd Reviewer Offshore" in (membersOf(Offshore-Egypt))
        )
    )
    or 
    # Anyone from the east pod working on a pod different than the eastpod
    (
        Division != East
        and
        (
            "Drafter/Estimator" in (Mahmoud.Burhamy, Nada.Hanafy, Ahmed.Tarek,Zeyad.Al-Houssainy, Ahmed.Abdelsatar, Ahmed.Khaled, Hayat.Magdy, Toka.Mohamed , AbdelRahman.Elsayed ,Mohamed.Badawy , Abdelrahman.Shenhaby ,  Ola.Salaheldeen , Ahmed.Hesham ,  Enas.Ahmed , Bassant.Mohamed , Aya.Hesham ,  Mohamed.Elwany , Rowan.Mohamed , Reem.AbdelKhalek , Mahmoud.Yasser , Lara.Mohamed , AsmaaAbd.Elrehim , Abdullatif.Muhammed , Hebatullah.Ashraf , Radwa.Saady , Mostafa.Zeidy , Sara.AlGhonaimy, Sara.Yassin , Nada.Mohamed , Ahmed.Ali ,  Menna.Youssef , Menna.Ibrahim , Nadia.Aly , Hagar.Magdi , Sarah.Alattar , Yasmine.Mohsen , Amira.Said, Esraa.Ayman , Toqaallah.Khaled ,  Farah.Hazem ,Engy.Ibrahim , Hebatullah.Zein ,Mohab.Kobisy, Basher.Badawy ,Rewaa.Mohamed  , Mohamed.Kotb ,Rowana.Fathy , Hesham.Elzalabany , Donia.Hassan , Omnia.SalahEldeen, Amr.Abdelkarim , Fatma.Mofeed , Noha.Mostafa , Mai.Ahmed ,  Mariam.Douban , Mayar.Amr,Mustafa.Madboly, AbdelRahman.Elsayed, Rana.Elsayed,Essam.Galal, Yosra.Helal, Alaa.Esmail, Mohamed.Rashad, Lamis.Waheeb ,Mohamed.Amer,Sara.Ragab,Toka.Salah , Aya.Ehab, Mahmoud.Yasser , Mohamed.Badawy)
            or
            "Reviewer Offshore" in (Mahmoud.Burhamy, Nada.Hanafy, Ahmed.Tarek,Zeyad.Al-Houssainy, Ahmed.Abdelsatar, Ahmed.Khaled, Hayat.Magdy, Toka.Mohamed , AbdelRahman.Elsayed ,Mohamed.Badawy , Abdelrahman.Shenhaby ,  Ola.Salaheldeen , Ahmed.Hesham ,  Enas.Ahmed , Bassant.Mohamed , Aya.Hesham ,  Mohamed.Elwany , Rowan.Mohamed , Reem.AbdelKhalek , Mahmoud.Yasser , Lara.Mohamed , AsmaaAbd.Elrehim , Abdullatif.Muhammed , Hebatullah.Ashraf , Radwa.Saady , Mostafa.Zeidy , Sara.AlGhonaimy, Sara.Yassin , Nada.Mohamed , Ahmed.Ali ,  Menna.Youssef , Menna.Ibrahim , Nadia.Aly , Hagar.Magdi , Sarah.Alattar , Yasmine.Mohsen , Amira.Said, Esraa.Ayman , Toqaallah.Khaled ,  Farah.Hazem ,Engy.Ibrahim , Hebatullah.Zein ,Mohab.Kobisy, Basher.Badawy ,Rewaa.Mohamed  , Mohamed.Kotb ,Rowana.Fathy , Hesham.Elzalabany , Donia.Hassan , Omnia.SalahEldeen, Amr.Abdelkarim , Fatma.Mofeed , Noha.Mostafa , Mai.Ahmed ,  Mariam.Douban , Mayar.Amr,Mustafa.Madboly, AbdelRahman.Elsayed, Rana.Elsayed,Essam.Galal, Yosra.Helal, Alaa.Esmail, Mohamed.Rashad, Lamis.Waheeb ,Mohamed.Amer,Sara.Ragab,Toka.Salah , Aya.Ehab, Mahmoud.Yasser , Mohamed.Badawy) 
            or
            "2nd Reviewer Offshore" in (Mahmoud.Burhamy, Nada.Hanafy, Ahmed.Tarek,Zeyad.Al-Houssainy, Ahmed.Abdelsatar, Ahmed.Khaled, Hayat.Magdy, Toka.Mohamed , AbdelRahman.Elsayed ,Mohamed.Badawy , Abdelrahman.Shenhaby ,  Ola.Salaheldeen , Ahmed.Hesham ,  Enas.Ahmed , Bassant.Mohamed , Aya.Hesham ,  Mohamed.Elwany , Rowan.Mohamed , Reem.AbdelKhalek , Mahmoud.Yasser , Lara.Mohamed , AsmaaAbd.Elrehim , Abdullatif.Muhammed , Hebatullah.Ashraf , Radwa.Saady , Mostafa.Zeidy , Sara.AlGhonaimy, Sara.Yassin , Nada.Mohamed , Ahmed.Ali ,  Menna.Youssef , Menna.Ibrahim , Nadia.Aly , Hagar.Magdi , Sarah.Alattar , Yasmine.Mohsen , Amira.Said, Esraa.Ayman , Toqaallah.Khaled ,  Farah.Hazem ,Engy.Ibrahim , Hebatullah.Zein ,Mohab.Kobisy, Basher.Badawy ,Rewaa.Mohamed  , Mohamed.Kotb ,Rowana.Fathy , Hesham.Elzalabany , Donia.Hassan , Omnia.SalahEldeen, Amr.Abdelkarim , Fatma.Mofeed , Noha.Mostafa , Mai.Ahmed ,  Mariam.Douban , Mayar.Amr,Mustafa.Madboly, AbdelRahman.Elsayed, Rana.Elsayed,Essam.Galal, Yosra.Helal, Alaa.Esmail, Mohamed.Rashad, Lamis.Waheeb ,Mohamed.Amer,Sara.Ragab,Toka.Salah , Aya.Ehab, Mahmoud.Yasser , Mohamed.Badawy)
        )
    )
)

