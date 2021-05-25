// expand(3, 2) returns "($1, $2), ($3, $4), ($5, $6)" 
function expand(rowCount, columnCount, startAt = 1, data_types = []) {
    var index = startAt
    return Array(rowCount).fill(0).map((v) => `(${Array(columnCount).fill(0).map((v, idx)=> {
        if (data_types[idx])
            return `$${index++}::${data_types[idx]}`;
        return `$${index++}`;
    }).join(", ")})`).join(", ")
}

// flatten([[1, 2], [3, 4]]) returns [1, 2, 3, 4]
function flatten(arr) {
    var newArr = []
    arr.forEach(v => v.forEach(p => newArr.push(p)))
    return newArr
}

exports.expand = expand;
exports.flatten = flatten;