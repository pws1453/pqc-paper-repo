import csv

csvfile = "abstracts.csv"


def parser(bigdict, abstract, year):
    wordlist = ["the","in","and","with","few","around","per","cannot","do","like","reduce","where","is",\
        "been","years","effort","internet","computer","work","finally","future","problems","how","our"\
            ,"have","seen","such","however","seeks","useful","problem","above","providing","presents","argument"\
                ,"a","of","are","can","on","an","as","this","to","or","for","be"]
    ab = abstract.split(" ")
    for word in ab:
        word = word.replace(",","")
        word = word.replace("”","")
        word = word.replace("’","")
        word = word.replace(".","")
        word = word.replace(")","")
        word = word.replace("(","")
        word = word.replace(":","")
        word = word.replace(";","")
        word = word.replace("[","")
        word = word.replace("]","")
        word = word.strip()
        with open("blocklist.txt") as f:
            lit = f.readlines()
            for lword in lit:
                lword = lword.replace(",","")
                lword = lword.replace(".","")
                lword = lword.replace(")","")
                lword = lword.strip()
                wordlist.append(lword)

            if year not in bigdict.keys():
                bigdict[year] = dict()
            if word not in wordlist and not word.isdigit() and word != "":
                if word in bigdict[year].keys():
                    bigdict[year][word] = bigdict[year][word] + 1
                else:
                    bigdict[year][word] = 1
                wordlist.append(word)
    return bigdict


def abstractSan(abstract):
    abstract = abstract.strip()
    abstract = abstract.lower()
    abstract = abstract.replace("blockchains","blockchain")
    abstract = abstract.replace("zero knowledge","zero-knowledge")
    abstract = abstract.replace("post quantum","post-quantum")
    abstract = abstract.replace("postquantum","post-quantum")
    abstract = abstract.replace("crystals kyber","crystals-kyber")
    abstract = abstract.replace("crystals dilithium","crystals-dilithium")
    abstract = abstract.replace("digital signature","digital-signature")
    abstract = abstract.replace("digitalsignature","digital-signature")
    abstract = abstract.replace("quantum crypto","quantum-crypto")
    abstract = abstract.replace("digital signatures","digital-signatures")
    return abstract

def main():
    frequencydict = dict()
    with open(csvfile) as f:
        read = csv.reader(f)
        for row in read:
            abstract = row[0]
            rabstract = abstractSan(abstract)
            year = row[1]
            parser(frequencydict,rabstract,year)
    for year in frequencydict.keys():
        orderlist = []
        leng = len(frequencydict[year].values())
        print(f"{year}: {leng}")
        for word in frequencydict[year].keys():
            if frequencydict[year][word] > 1:
                with open(f"unsorted-sanitized/{year}.csv","a") as f:
                    f.write(f"{word}, {frequencydict[year][word]}\n")


if __name__ == "__main__":
    main()