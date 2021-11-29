import fitz

doc = fitz.open("sample-tech-arch.pdf")
for page in doc:
    ### SEARCH
    keywords = ["Java", "Python", "framework", "security"]
    text_instances = []
    for key in keywords:
        print(key)
        text_instances.extend(page.search_for(key))

    ### HIGHLIGHT
    print (len(text_instances))
    for inst in text_instances:
        highlight = page.add_highlight_annot(inst)
        highlight.update()


### OUTPUT
doc.save("output.pdf", garbage=4, deflate=True, clean=True)