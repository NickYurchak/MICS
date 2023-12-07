import ClothingType from './ClothingType';
// Клас для конкретного типу одягу (Рубашка)
export default class Shirt extends ClothingType {
    constructor() {
      super('Рубашка');
    }
  }

module.exports = Shirt;

