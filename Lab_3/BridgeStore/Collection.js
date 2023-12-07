// Абстрактний клас Collection
export default class Collection {
    constructor(collection) {
      this.collection = collection;
    }
  
    getCollection() {
      return this.collection;
    }
  }

module.exports = Collection;

