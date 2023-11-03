def find_index(elements: list, value):
    return elements.index(value)

def find_item(elements, value):
    results = []
    for i, item in enumerate(elements):
        if item == value:
            results.append([i])
        elif isinstance(elements[i], list):
            for ii in find_item(elements[i], value):
                results.append([i] + ii)
    return results

def main():
    print(find_item([1,[0,1],[0,2,[0,1,2]]],1))
    result = find_item([[[1,2,3],2,[1,3]],[1,2,3]], 2)
    print(result)
    assert result == [[0,0,1],[0,1],[1,1]]
    results = find_item([])
    

if __name__ == "__main__":
    main()