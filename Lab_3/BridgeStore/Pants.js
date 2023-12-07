import ClothingType from './ClothingType';
// Клас для конкретного типу одягу (Штани)
export default class Pants extends ClothingType {
    constructor() {
      super('Штани');
    }
  }
module.exports = Pants;

