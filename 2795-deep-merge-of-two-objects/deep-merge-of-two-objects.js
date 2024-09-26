var deepMerge = function(A, B) {
    // Handle both arrays
    if (Array.isArray(A) && Array.isArray(B)) {
        let maxLen = Math.max(A.length, B.length);
        let mergedArr = [];
        for (let i = 0; i < maxLen; i++) {
            if (i < A.length && i < B.length) {
                mergedArr.push(deepMerge(A[i], B[i])); // Recursive deep merge for array elements
            } else if (i < A.length) {
                mergedArr.push(A[i]);
            } else {
                mergedArr.push(B[i]);
            }
        }
        return mergedArr;
    }

    // Handle objects
    else if (typeof A === 'object' && A !== null && typeof B === 'object' && B !== null && !Array.isArray(A) && !Array.isArray(B)) {
        let mergedObj = {};
        let keys = new Set([...Object.keys(A), ...Object.keys(B)]); // Union of all keys in A and B
        keys.forEach(key => {
            if (key in A && key in B) {
                mergedObj[key] = deepMerge(A[key], B[key]);
            } else if (key in A) {
                mergedObj[key] = A[key];
            } else {
                mergedObj[key] = B[key];
            }
        });
        return mergedObj;
    }

    // Handle primitive types
    return B;
};

// // Test case
// let A = [{}, 2, 3];
// let B = [[], 5];
// console.log(deepMerge(A, B));  // Output: [[], 5, 3]
