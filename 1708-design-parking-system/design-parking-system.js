/**
 * @param {number} big
 * @param {number} medium
 * @param {number} small
 */
var ParkingSystem = function(big, medium, small) {
    this.carTypeMap = {
        1: "big",
        2: "medium",
        3: 'small'
    }
    this.cache = {big, medium, small}
};

/** 
 * @param {number} carType
 * @return {boolean}
 */
ParkingSystem.prototype.addCar = function(carType) {
    const carSize = this.carTypeMap[carType]
    if (this.cache[carSize] >= 1) {
        this.cache[carSize] -= 1
        return true
    }
    return false
};

/** 
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new ParkingSystem(big, medium, small)
 * var param_1 = obj.addCar(carType)
 */