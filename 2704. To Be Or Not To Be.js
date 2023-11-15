/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    const toBe = function(val2){
        if(val === val2){
            return(true)
        }else{
            throw new Error("Not Equal")
        }
    }
    const notToBe = function(val2){
        if(val !== val2){
            return(true)
        }else{
            throw new Error("Equal")
        }
    }

    return {toBe,notToBe}
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */
// 测试中使用了链式调用, 也就是说返回对象会直接运行下一个指令, 也就是测试中的toBe和notToBe。
// 为了实现这个效果, expect需要返回一个对象, 对象有两个属性分别是题目中给出的两个判断函数。