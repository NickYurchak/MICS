import ClothingType from './ClothingType';
// Клас для конкретного типу одягу (Футболка)
export default class TShirt extends ClothingType {
    constructor() {
      super('Футболка');
    }
  }

module.exports = TShirt;

