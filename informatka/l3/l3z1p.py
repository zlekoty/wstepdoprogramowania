x='Akcja rozpoczyna się inwokacją: „Litwo! Ojczyzno moja!…”, która wyraża tęsknotę poety za krajem lat dzieciństwa. Tylko ten, kto straci ojczyznę, jest w stanie ją doceniać. Opisuje urodę ziemi litewskiej i zwraca się bezpośrednio do Matki Boskiej Ostrobramskiej, patronki Nowogródka. Wyraża nadzieję, iż pomoże Ona wszystkim emigrantom wygnanym z kraju wrócić do swego domu. Zwraca uwagę na Niemen, pola urodzajne i bujne rośliny. Wśród takiej przyrody, w brzozowym gaju stał piękny drewniany, ale podmurowany dworek szlachecki- Soplicowo. Zajechał właśnie do niego młodzian – Tadeusz, który ukończył naukę w wielkim mieście. Rozpoznaje wszelkie sprzęty i zakątki dworku.Tadeusz chodził po komnatach, oglądał różne obrazki wiszące na ścianach i zmierzał do pokoju, w którym mieszał w dzieciństwie [wiersz 81]. Okazało się, iż jest on zajęty przez kobietę. Poznał to po rozłożonych sukienkach. Stając w oknie, zobaczył ogród a w nim przepiękne i kolorowe grządki [94]. Widział młodą dziewczynę o wysmukłej figurze i rozwianych długich włosach ubraną w białe szaty – to pierwsze spotkanie z Zosią [117]. Pląsała po ogrodzie, potem po desce opartej o okno wbiegła do pokoju. Zobaczywszy Tadeusza, zawstydziła się i po chwili uciekła.'
x=x.upper()
x1=list(x)
d=dict()
for a in x1:
    if a in d:
        d[a]=d[a]+1
    if a not in d:
        d[a]=1
del d[' ']
z=0
x2=sorted(d, key=d.get, reverse=True)
for b in x2:
    if z<10:
        print(b,d[b],'*'*d[b])
        z=z+1
    else:
        break
