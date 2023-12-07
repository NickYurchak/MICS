import ClothingType from './ClothingType';
// Клас для конкретного типу одягу (Светер)
export default class Sweater extends ClothingType {
    constructor() {
      super('Светер');
    }
  }

module.exports = Sweater;

