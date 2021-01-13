x='The action begins with an invocation: “Lithuania! My homeland!… ”Which expresses the poets longing for the country of his childhood. Only those who lose their homeland can appreciate it. It describes the beauty of the Lithuanian land and addresses directly to Our Lady of Ostra Brama, the patron of Nowogrodek. She expresses the hope that she will help all emigrants expelled from the country return to their home. He draws attention to the Niemen, fertile fields and lush plants. Among such nature, in a birch grove stood a beautiful wooden but underpinned manor house - Soplicowo. A young man, Tadeusz, who finished his education in a big city, just joined him. He recognizes all the furnishings and nooks of the manor house. Tadeusz walked around the chambers, looked at various pictures on the walls and headed for the room where he lived as a child [line 81]. It turned out to be occupied by a woman. He recognized it by the dresses spread out. Standing in the window, he saw a garden with beautiful and colorful beds [94]. He saw a young girl with a slender figure and long flowing hair, dressed in white robes - this was the first meeting with Zosia [117]. She danced around the garden, then ran across a plank against the window into the room. When she saw Tadeusz, she was ashamed and ran away after a while.'
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
