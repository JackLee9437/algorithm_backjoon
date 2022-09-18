from sys import setrecursionlimit
setrecursionlimit(int(1e9))

def solution(words, queries):
    fortrie = {}
    revtrie = {}
    for word in words :
        if len(word) not in fortrie :
            fortrie[len(word)] = {"count": 0, "children" : {}}
            revtrie[len(word)] = {"count": 0, "children" : {}}
        fortrie[len(word)]["count"] += 1
        revtrie[len(word)]["count"] += 1
        cur = fortrie[len(word)]["children"]
        for c in word :
            if c not in cur :
                cur[c] = {"count" : 0, "children" : {}}
            cur[c]["count"] += 1
            cur = cur[c]["children"]
        cur = revtrie[len(word)]["children"]
        for i in range(len(word)-1, -1, -1) :
            c = word[i]
            if c not in cur :
                cur[c] = {"count" : 0, "children" : {}}
            cur[c]["count"] += 1
            cur = cur[c]["children"]

    def find(query, index, length, cur) :
        ret = 0
        if query[index] == "?" :
            ret = cur["count"]
        else :
            if query[index] in cur["children"] :
                ret = find(query, index+1, length, cur["children"][query[index]])
        return ret
    
    answer = []
    for query in queries :
        if len(query) not in fortrie :
            answer.append(0)
        else :
            if len(query) == query.count("?") :
                answer.append(fortrie[len(query)]["count"])
            else :
                if query[0] == "?" :
                    answer.append(find(query[::-1], 0, len(query), revtrie[len(query)]))
                else :
                    answer.append(find(query, 0, len(query), fortrie[len(query)]))
    return answer