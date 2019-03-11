
List=[1,2,3,4,5,6]

item=6

Found = False

while not Found and first <= top
    Midpoint <- (First + Last) DIV 2
    If List[Midpoint] = ItemSought Then
        ItemFound <- True
    Else
        If First >= Last Then
            SearchFailed <- True
        Else
            If List[Midpoint] > ItemSought Then
                Last <- Midpoint - 1
            Else
                First <- Midpoint + 1
            EndIf
        EndIf
    EndIf

