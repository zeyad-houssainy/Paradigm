project = MTP and labels not in (training) and "Scheduling Type" = Estimating and status in ("In Offshore Review", "In 2nd Offshore Review") and 
(
    "reviewer offshore" in (membersOf(Offshore-Egypt))
    or 
    "2nd Reviewer Offshore" in (membersOf(Offshore-Egypt))
)
and 
(
    (labels not in (Delivered_By_NICA) and duedate > startOfDay())
    or
    (labels in (Delivered_By_NICA) and duedate > startOfDay(5))
)
