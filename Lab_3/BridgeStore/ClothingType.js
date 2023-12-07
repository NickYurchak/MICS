// Абстрактний клас ClothingType
export default class ClothingType {
    constructor(type) {
      this.type = type;
    }
  
    getType() {
      return this.type;
    }
  }

module.exports = ClothingType;

