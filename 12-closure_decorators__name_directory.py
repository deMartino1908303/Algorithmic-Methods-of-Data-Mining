def person_lister(f):
    def inner(people):
        # complete the function
        people.sort(key=lambda x: int(x[2]))
        names = []
        for person in people:
            if person[-1] == "M":
                tmp = "Mr. " + person[0] + " " + person[1]
                names.append(tmp)
            if person[-1] == "F":
                tmp = "Ms. " + person[0] + " " + person[1]
                names.append(tmp)
        return names
    return inner
