/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let res = [];
    arr.forEach((item, index)=>{
        res[index] = fn(item, index)
    })
    // 为了写循环, 也可以使用for(let i = 0; i < arr.length; i++)的形式

    return res;
};