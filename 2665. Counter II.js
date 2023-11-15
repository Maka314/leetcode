/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    hotInit = init;
    const increment = function(){
        hotInit += 1;
        return hotInit;
    }
    const decrement = function(){
        hotInit -= 1;
        return hotInit;
    }
    const reset = function(){
        hotInit = init;
        return hotInit;
    }

    return{increment,decrement,reset}
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */