def list_benifits():
    return "More organized code","more readable code","Easier code reuse","allowing programmers to share and connect code together!"

def build_sentence(benifit):
    return "%s is a benefit of functions!" %benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functios()
